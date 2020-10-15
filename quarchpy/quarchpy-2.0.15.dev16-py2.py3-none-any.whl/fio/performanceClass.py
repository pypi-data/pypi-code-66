'''
Implements basic control over lspci utilities, so that we can identify and check the
status of PCIe devices on the host system
'''

import subprocess
import platform
import time
import os
import re
import sys
import ctypes
import csv
from abc import ABC, abstractmethod
from os.path import exists

try:
    import pandas as pd
except:
    pass
import json
from enum import Enum

from quarchpy.disk_test import driveTestConfig
from quarchpy.user_interface import*


class AbstractPerformance(ABC):

    @abstractmethod
    def start_workload(self, workload_file_path=None, output_file_path="workload_output.txt", workload_args_dict=None,
                       output_data=None, run_async=False, suspend_streams_till_end=False):
        """
            Base function for starting a workload

            Parameters
            ----------

            workload_file_path : string, optional

                Specifies a path to a file containing the workload details

            output_file_path : string, optional

                specifies a path to the output file for workload results
                    - If file does not exist, this will be created in a temp folder
                    - Results will overwrite current contents.

            workload_args_dict : dictionary, optional

                Dictionary containing major workload arguments when a workload file is not used.
                These are automatically parsed later into specific program arguments.

                Argument List:

                read_percentage         : int       : Percentage workload for writing operations. Remainder will be
                                                        read operations

                sequential              : boolean   : Specifies whether write / read is sequential or random
                                                        Default True

                workload_file_size      : string    : Size of file I/O created from workload
                blocksize               : string    : Size of chunks of IO

                runtime                 : int       : Run time of workload (Seconds)
                rampup_time             : int       : Ramp up time of workload (Seconds)
                iodepth                 : string    : IO depth to use

                run_directory           : filePath  : Directory to run workload in

            output_data : dict

                Dictionary containing the requested data to be returned from the workload.

                Argument List:

                summary_data            : List<string>{             : List of data items to be returned at workload end
                                            'read_iops'
                                            'write_iops'

                                            'find:field1:field2:field3' # can be used to grab any argument specified
                                                                        fields indicate key of dictionary

                high_res_data    : List<string>{             : List of high resolution timings
                                            'high_res_iops'
                                            'high_res_lat'          # Adds clat, slat and lat outputs

                stream_data             : List<string>{             : List of stream data returned during workload
                                            'stream_read_iops'
                                            'stream_write_iops'

                                            'stream:field1:field2'  # can be used to grab any argument during stream

                stream_resolution       : Dict <key, Resoltuion>    : Specify the stream and resolution required
                                                                    Will default to FIO defaults if invalid resolution

                                            'high_res_data_res' : int (mS)      # default : all recorded log entries
                                            'stream_data_res'   : int (S)       # default : 1 second resolution

                stream_workload_callbacks      : Dict <Key, Function> {
                                            Accepted keys:

                                            'workload_start_callback' : Takes a start 'time' (unix) and optional 'data'
                                                        value, normally a string to identify the workload
                                            'workload_end_callback'   : Takes a 'time' (unix) and a optional 'data'
                                                        value, normally a string to identify the workload
                                            'stream_data_callback' : Takes a dictionary
                                                    will return requested output data at seconds intervals during W/L


            run_async : boolean, optional

                Specifies whether the workload should be started asynchronously (returning before complete)
                If true, start_workload returns a process tracking object to monitor its state

            suspend_streams_till_end : boolean, optional

                If true, no real time streaming of data to the stream_data_callback will occur, this will be held until
                the end of the workload to minimise processing on the host system

        """
        pass

class FioPerformance ( AbstractPerformance ):

    def __init__(self):
        # Variables for FIO
        self.output_format = "json"             # argument cannot be specified in fio workload file
        self.job_name = []                      # overridden if the user specifies their own one

        # Output file names
        self.output_file = "fioOutput.txt"      # argument cannot be specified in fio workload file
        self.iops_log_output_file = None
        self.clat_log_output_file = None
        self.slat_log_output_file = None
        self.lat_log_output_file = None

        # Callback variables
        self.has_callbacks = False
        self.start_workload_callback = None
        self.end_workload_callback = None
        self.stream_data_callback = None

        # key locations:
        self.five_nines_str = "jobs:read:clat_ns:99.999000"
        self.four_nines_str = "jobs:read:clat_ns:99.990000"
        self.three_nines_str = "jobs:read:clat_ns:99.900000"
        self.write_iops_str = "jobs:write:iops"
        self.read_iops_str = "jobs:read:iops"

        # file Pre/post fixes
        self.iops_file_prefix = "quarch_iops"
        self.latency_file_prefix = "quarch_lat"

        # workload string
        self.command = ["fio"]


    def start_workload(self, workload_file_path=None, output_file_path=None, workload_args_dict=None,
                       output_data=None, run_async=False, suspend_streams_till_end=False):

        # assign callbacks to variables for dealing with stream data
        if output_data is not None and "stream_workload_callbacks" in output_data:
            self._assign_callbacks(output_data["stream_workload_callbacks"])
            self.has_callbacks = True

        # simplest start via this
        if workload_file_path is not None:
            # look for specific arguments
            if not self.__parse_file(workload_file_path):
                return False

        if output_file_path:
            # add the output file to path
            self.output_file = output_file_path
            self.command.append(self.__convert_arg_to_cmd("output", self.output_file))

        # format srguments for fio workload
        if workload_args_dict is not None:
            self.__parse_workload_dict(workload_args_dict)

        # Adding additional arguments as needed for output requested
        if output_data is not None:
            # requires an output file - if not already specified
            if not output_file_path:
                self.command.append( self.__convert_arg_to_cmd("output", self.output_file) )
            # json output is easiest format to parse
            self.command.append( self.__convert_arg_to_cmd("output-format", self.output_format) )
            self.__add_additional_output_args(output_data)

        # if there's no other arguments, just allow the fio command to run
        if len(self.command) > 1:
            if not self.job_name:
                self.command.append( self.__convert_arg_to_cmd("name", "quarch_job") )
            # FIO has some required arguments
            if not self.__has_required_args():
                # Should this return false or........ should it append the necessary arguments
                return False

        # Will return values or process dependant on async
        ret_value = None

        if not run_async:
            # start process and return outputs asked for
            if self.has_callbacks:
                #print(self.command)
                # if status interval hasn't already been specified, add it
                if not any("--status-interval=" in argument for argument in self.command):
                    self.command.append( self.__convert_arg_to_cmd("status-interval", 1 ) )

                # Start subprocess and pass down to lower level
                process = None
                try:
                    process = subprocess.Popen(self.command)
                except FileNotFoundError as error:
                    raise Exception(error)

                ret_value = self.__return_data(output_data, process)
            else:
                cmd = ' '.join(line for line in self.command)
                try:
                    subprocess.call(cmd)
                except FileNotFoundError as error:
                    raise Exception(error)
                ret_value = self.__source_output_data(output_data)

        else:
            # return fio running process
            if self.has_callbacks:
                raise Exception("callbacks ignored for async run")
            # Not executing as shell as string contains name of program to execute
            try:
                return subprocess.Popen(self.command)
            except FileNotFoundError as error:
                raise Exception(error)

        return ret_value

    def _assign_callbacks(self, output_data):
        # Assign the callbacks
        if "workload_start_callback" in output_data.keys() and callable(output_data["workload_start_callback"]):
            self.start_workload_callback = output_data["workload_start_callback"]
        if "workload_end_callback" in output_data.keys() and callable(output_data["workload_end_callback"]):
            self.end_workload_callback = output_data["workload_end_callback"]
        if "stream_data_callback" in output_data.keys() and callable(output_data["stream_data_callback"]):
            self.stream_data_callback = output_data["stream_data_callback"]


    def __parse_file(self, file):
        if not os.path.isfile(file):
            print("Workload file is not a valid file, argument skipped")
            return False

        f = open(file, "r")
        if f.mode == 'r':
            contents = f.read()
            contents = contents.split("\n")
            for row in contents:
                # Specifying a log file does not mean including it in the output
                if "write_iops_log" in row:
                    self.iops_log_output_file = row[row.index("=") + 1:] + "_iops.1.log"
                if "write_lat_log" in row:
                    self.lat_log_output_file = row[row.index("=") + 1:] + "_lat.1.log"
                    self.clat_log_output_file = row[row.index("=") + 1:] + "_clat.1.log"
                    self.slat_log_output_file = row[row.index("=") + 1:] + "_slat.1.log"
                if "[" in row[:1]:
                    if "global" not in str(row).lower():
                        self.job_name.append(row[1: int(len(row) - 1)])   # remove start and end bracket

        self.command.append(file)
        return True

    def __parse_workload_dict(self, workload_dict):
        sequential = True

        # not optimal - but performance at this point is not an issue
        for key, value in workload_dict.items():
            if key in "sequential" and bool(value) is False:
                if not isinstance(value, bool):
                    print("sequential value not of type 'bool', argument removed")
                    continue
                sequential = False

        # Parsing self.command line arguments for the information required
        for key, value in workload_dict.items():
            if key in "read_percentage":
                if not isinstance(value, int):
                    print("read_percentage value not of type 'bool', argument removed")
                    continue
                if int(value) == 100:
                    if not sequential :
                        self.command.append( self.__convert_arg_to_cmd("rw", "randread") )
                    else:
                        self.command.append( self.__convert_arg_to_cmd("rw", "read") )
                    continue
                if int(value) == 0:
                    if not sequential :
                        self.command.append( self.__convert_arg_to_cmd("rw", "randwrite") )
                    else:
                        self.command.append( self.__convert_arg_to_cmd("rw", "write") )
                    continue
                if 0 < int(value) < 100:
                    if not sequential :
                        self.command.append( self.__convert_arg_to_cmd("rw", "randrw") )
                    else:
                        self.command.append( self.__convert_arg_to_cmd("rw", "rw") )

                    # Percentage of a mixed workload that should be reads. Default: 50.
                    self.command.append( self.__convert_arg_to_cmd("rwmixread", value) )
                    continue

            if key in "workload_file_size":
                self.command.append( self.__convert_arg_to_cmd("size", value) )

            if key in "blocksize":
                self.command.append( self.__convert_arg_to_cmd("blocksize", value) )

            if key in "runtime":
                if not isinstance(value, int):
                    print("runtime value not of type 'int', argument removed")
                else:
                    self.command.append( self.__convert_arg_to_cmd("runtime", value) )
                    self.command.append( self.__convert_arg_to_cmd("time_based") )     # Iometer is time based too

            if key in "rampup_time":
                if not isinstance(value, int):
                    print("rampup_time value not of type 'int', argument removed")
                    continue
                self.command.append( self.__convert_arg_to_cmd("ramp_time", value) )

            if key in "queue_depth":
                self.command.append( self.__convert_arg_to_cmd("queue_depth", value) )
                
            if key in "run_directory":
                if not os.path.isfile(value):
                    print("run_directory value not of type 'file', argument removed")
                    continue
                self.command.append( self.__convert_arg_to_cmd("directory", value) )

        return

    def __source_output_data(self, output_data, json_data=None):

        # return true if user doesn't want outputs.
        if not output_data:
            return True

        ret_val = {}

        if not json_data:
            with open(self.output_file, 'r') as handle:
                fixed_json = ''.join(line for line in handle if not line.startswith('fio'))
                json_data = json.loads(fixed_json)

        # Get output data
        if json_data:
            # for key in output_data.keys():
            if "summary_data" in output_data:
                for value in output_data["summary_data"]:
                    if str(value) in "read_iops":
                        tempVal = self.__get_json_data(self.read_iops_str, json_data)
                        ret_val["read_iops"] = tempVal[self.read_iops_str]
                        continue

                    if str(value) in "write_iops":
                        tempVal = self.__get_json_data(self.write_iops_str, json_data)
                        ret_val["write_iops"] = tempVal[self.write_iops_str]
                        continue

                    if "find" in str(value)[:len("find")]:
                        myArray = value[value.find(":") + 1:]
                        ret_val.update(self.__get_json_data(myArray, json_data))
                        continue

                    ret_val.update({value: "Invalid Summary Data Key"})


            if "high_res_data" in output_data:
                ret_val["high_res_data"] = self.__return_high_res_data()

        # Return false if outputs have not been gathered as needed
        if not ret_val:
            return False

        return ret_val

    def __return_high_res_data(self):

        high_res_dictionary = {}

        latency_time_data = []# "time_lat_mS"]
        latency_data = []#"lat_log"]
        slatency_time_data = []#"time_slat_mS"]
        slatency_data = []#"slat_log"]
        clatency_time_data = []#"time_clat_mS"]
        clatency_data = []#"clat_log"]
        iops_time_data = []#"time_iops_mS"]
        iops_data = []#"iops_log"]

        if self.iops_log_output_file is not None:
            with open(self.iops_log_output_file) as f:
                temp = csv.reader(f)
                for row in temp:
                    latency_time_data.append(str(row[0]).strip())
                    latency_data.append(str(row[1]).strip())
                high_res_dictionary.update({"time_lat_mS": latency_time_data})
                high_res_dictionary.update({"lat_log": latency_data})

        if self.clat_log_output_file is not None:
            with open(self.clat_log_output_file) as f:
                temp = csv.reader(f)
                for row in temp:
                    clatency_time_data.append(str(row[0]).strip())
                    clatency_data.append(str(row[1]).strip())
                high_res_dictionary.update({"time_clat_mS": clatency_time_data})
                high_res_dictionary.update({"clat_log": clatency_data})

        if self.slat_log_output_file is not None:
            with open(self.slat_log_output_file) as f:
                temp = csv.reader(f)
                for row in temp:
                    slatency_time_data.append(str(row[0]).strip())
                    slatency_data.append(str(row[1]).strip())
                high_res_dictionary.update({"time_slat_mS": slatency_time_data})
                high_res_dictionary.update({"slat_log": slatency_data})

        if self.lat_log_output_file is not None:
            with open(self.lat_log_output_file) as f:
                temp = csv.reader(f)
                for row in temp:
                    iops_time_data.append(str(row[0]).strip())
                    iops_data.append(str(row[1]).strip())
                high_res_dictionary.update({"time_iops_mS": iops_time_data})
                high_res_dictionary.update({"iops_log": iops_data})

        return high_res_dictionary

    def __add_additional_output_args(self, outputs):

        for key, value in outputs.items():
            if str(key).lower() in "high_res_data":
                self.__add_additional_data_arguments(value)

            if str(key).lower() in "stream_resolution":
                self.__add_stream_resolutions(value)

        return

    def __add_stream_resolutions(self, stream_resolutions_dict):

        for key, value in stream_resolutions_dict.items():
            if str(key).lower() in "high_res_data_res":
                if not isinstance(value, int):
                    print("high_res_data value not of type 'int', argument removed")
                    continue
                if int(value) > 0:
                    self.command.append( self.__convert_arg_to_cmd("log_avg_msec", value) )

            if str(key).lower() in "stream_data_res":
                if int(value) < 1:
                    value = 1
                self.command.append( self.__convert_arg_to_cmd("status-interval", value) )

        return

    def __add_additional_data_arguments(self, stream_outputs):

        for data_value in stream_outputs:
            if str(data_value).lower() in "high_res_iops":
                # if user hasn't already specified iops file names, do so for them
                if not self.iops_log_output_file:
                    self.command.append( self.__convert_arg_to_cmd("write_iops_log", self.iops_file_prefix) )
                    self.iops_log_output_file = self.iops_file_prefix + "_iops.1.log"

            if str(data_value).lower() in "high_res_lat":
                # if user hasn't already specified latency file names, do so for them
                if not self.lat_log_output_file:
                    self.command.append( self.__convert_arg_to_cmd("write_lat_log", self.latency_file_prefix) )
                    self.lat_log_output_file = self.latency_file_prefix + "_lat.1.log"
                    self.clat_log_output_file = self.latency_file_prefix + "_clat.1.log"
                    self.slat_log_output_file = self.latency_file_prefix + "_slat.1.log"

        return

    def __convert_arg_to_cmd(self, string_argument, string_value=None):
        if string_value is not None:
            return "--" + str(string_argument) + "=" + str(string_value)
        else:
            return "--" + str(string_argument)

    def __has_required_args(self):
        required_args = ["--name=", "--size=", "--rw="]
        for elem in required_args:
            if not any(elem in argument for argument in self.command):
                return False
        return True

    def __follow(self, thefile, p):
        thefile.seek(0, 2)
        # flag for exiting the loop
        processCompleted = False

        while processCompleted == False:
            line = thefile.readline()

            # only exists if process is finished and no more data from file
            if p.poll() is not None and not line:
                # yield a specific string we can identify
                yield ("quarch_end_Process")
                processCompleted = True

            if not line:
                time.sleep(0.1)
                continue
            yield line

    def __return_data(self, output_data, process):

        ret_value = None

        output_file = self.output_file

        # isThreaded = True
        # checking to see if the first line of file needs to be skipped = Windows only
        # if os.name is "nt":
        #     isThreaded = False
        #     for i in arguments:
        #         # only needs to be skipped if the "thread" argument has not been issued
        #         if (str(i.lower()) == "thread"):
        #             isThreaded = True

        # variables for parsing json
        iterator = 0
        jobCount = 0
        jsonLines = ""
        openBracketCount = 0
        closeBracketCount = 0
        jsonobject = ""
        # Init the job end time to the current start time
        jobEndTime = int(round(time.time() * 1000))

        timeout = time.time()
        while not exists(output_file):
            if timeout - time.time() >= 5000:
                # Should i raise an error here?
                # raise Exception("Timed out waiting for file '" +output_file + "' to be created")
                return False
            print("Waiting for file creation or timeout")
            time.sleep(0.1)


        info_out = {}
        logfile = open(output_file, "r")
        loglines = self.__follow(logfile, process)

        for line in loglines:

            if "failed" in line:
                logfile.close()
                raise Exception(line)

            # skip the very first line -- (title line) --
            if iterator == 0:
                if line is "quarch_end_Process":

                    #raise Exception("Process yielded no usable data for callbacks")
                    #break
                    pass

                iterator = iterator + 1
                # marking threaded as true for remainder of read > Efficiency
                isThreaded = True
                continue

            # add to iterator - not needed, may be useful later
            iterator = iterator + 1

            # concat strings
            jsonLines += line

            # finding brackets withing json
            if '{' in line:
                openBracketCount = openBracketCount + 1
            if '}' in line:
                closeBracketCount = closeBracketCount + 1

            # an equal amount of brackets denotes the end of a json object
            if openBracketCount == closeBracketCount and openBracketCount is not 0:
                try:
                    # format into a json parsable string
                    TempJsonObject = jsonLines[0: jsonLines.rindex('}') + 1]

                    # parse json
                    jsonobject = json.loads(TempJsonObject)

                    # checking for first job
                    if (jobCount == 0):
                        # getting start time of job
                        startTime = (jsonobject['timestamp_ms'] - jsonobject['jobs'][0]['read']['runtime'])
                        if self.stream_data_callback:
                            self.start_workload_callback("Start time", startTime)

                    ret_val = {}

                    # Get output data
                    #for key in output_data.keys():
                    if "stream_data" in output_data:
                        for value in output_data["stream_data"]:
                            if str(value) in 'stream_read_iops':
                                tempVal = self.__get_json_data(self.read_iops_str, jsonobject)
                                ret_val["stream_read_iops"] = tempVal[self.read_iops_str]

                            if str(value) in 'stream_write_iops':
                                tempVal = self.__get_json_data(self.write_iops_str, jsonobject)
                                ret_val["stream_write_iops"] = tempVal[self.write_iops_str]

                    ret_val.update(self.__get_json_data("timestamp_ms", jsonobject))

                    if self.stream_data_callback:
                        self.stream_data_callback(ret_val)

                    # jsonLines variable is now all characters after last job + any new that come in
                    jsonLines = jsonLines[jsonLines.rindex('}') + 1:]

                    # add 1 to the job count
                    jobCount += 1

                    jobEndTime = str(jsonobject['timestamp_ms'])

                except:
                    # exception caused by not being able to find substring -- Last json object --
                    pass

                # looks for end of process and the specific string we return indicating end of file
                if process.poll() is not None:
                    if line is "quarch_end_Process":
                        time.sleep(0.1)
                        # fioCallbacks["TEST_END"](myStream, str(int(jobEndTime) + 1))
                        if self.end_workload_callback:
                            self.end_workload_callback("End time", str(int(jobEndTime) + 1))
                        # CLOSE FILE ON FINISH
                        logfile.close()

                        # add the rest of the output
                        ret_value = self.__source_output_data(output_data, jsonobject)

                        return ret_value

    def __get_json_data(self, string_key, json_data):
        self.ret_dict = {}

        # split into a string array if required.
        myArray = string_key
        if ":" in string_key:
            myArray = string_key.split(":")

        if isinstance(myArray, list):
            for item in myArray:
                # print(item)
                json_data = self.__parse_json(item, json_data, string_key)
        else:
            json_data = self.__parse_json(myArray, json_data, string_key)

        if not self.ret_dict:
            return {string_key: "Not Found"}

        return self.ret_dict

    def __parse_json(self, find_key, json_data, string_key):
        #print(type(json))
        #print(json)
        if isinstance(json_data, dict):
            for key, val in json_data.items():
                if find_key in key:
                    if not isinstance(val, list) and not isinstance(val, dict):
                        if find_key == str(key):
                            self.ret_dict = {string_key: val}
                            return
                    else:
                        return val
                    # if isinstance(v, list):
                    #   return v
        if isinstance(json_data, list):
            for list_item in json_data:
                ret = self.__parse_json(find_key, list_item, string_key)
                if ret is not None:
                    return ret

    def __get_csv_stats(self, csv_file, columns=None, max=False, mix=False, mean=False, std=False):

        loaded_csv = pd.read_csv(csv_file)
        column_data = ""
        if columns is not None:
            if type(columns) is list:
                for column in columns:
                    hi = loaded_csv[columns].describe()

        # print(hi['max'])

        pass

#
# def printList(dataList):
#     print("stream data callback")
#     # f = open("testingOutput.txt", "a+")
#     # for listItem in dataList:
#     #     f.write("\r\n")
#     #     for inneritem in listItem:
#     #         f.write(inneritem + ",")
#     print(dataList)
#
# def startFunc(a,b):
#     print("start callback")
# def endFunc(a,b):
#     print("end callback")


# def test_case_matt():
#     x = FioPerformance()
#     dict1 = {'read_percentage': 100, 'sequential': False, 'workload_file_size': '256mb', 'blocksize': '8k',
#              'runtime': '10', 'rampup_time': '10'}
#     inDir = "testingNewFio.ini"
#
#     output_data1 = {"summary_data": ["read_iops", "find:jobs:jobname"],
#                     "stream_data": ['stream_read_iops', 'stream_write_iops'],
#                     "stream_resolution": "1",
#                     "stream_workload_callbacks": {
#                         "workload_start_callback": startFunc,
#                         "workload_end_callback": endFunc,
#                         "stream_data_callback": printList}}
#
#     dataout = x.start_workload(workload_args_dict=dict1, workload_file_path=inDir, output_data=output_data1)
#     print("dataout")
#     print(dataout)







