from quarchpy.device import quarchDevice
from quarchpy.qps import toQpsTimeStamp
import os, time, datetime, sys, logging

if sys.version_info[0] < 3:
    from StringIO import StringIO
else:
    from io import StringIO

current_milli_time = lambda: int (round (time.time() * 1000))
current_second_time = lambda: int (round (time.time()))

# Using standard Unix time,  milliseconds since the epoch (midnight 1 January 1970 UTC)
# Should avoid issues with time zones and summer time correction but the local and host
# clocks should still be synchronised
def qpsNowStr():
    return current_milli_time()                          # datetime supports microseconds


class quarchQPS(quarchDevice):
    def __init__(self, quarchDevice):

        self.quarchDevice = quarchDevice
        self.ConType = quarchDevice.ConType
        self.ConString = quarchDevice.ConString

        self.connectionObj = quarchDevice.connectionObj
        self.IP_address = quarchDevice.connectionObj.qps.host
        self.port_number = quarchDevice.connectionObj.qps.port

    def getCanStream(self):

        # Check if stream is supported by testing for the enable command
        command_response = self.sendCommand("conf stream enable?")
        if ("FAIL" in command_response):
            return False
        else:
            return True


    def startStream(self, directory):
        if not self.getCanStream():
            raise Exception("This device does not support streaming.")
            return
        else:
            return quarchStream(self.quarchDevice, directory)
    

class quarchStream(quarchQPS):
    def __init__(self, quarchQPS, directory):
        self.connectionObj = quarchQPS.connectionObj
        
        self.IP_address = quarchQPS.connectionObj.qps.host
        self.port_number = quarchQPS.connectionObj.qps.port

        self.ConString = quarchQPS.ConString
        self.ConType = quarchQPS.ConType
        
        time.sleep(1)
      
        #check to see if any invalid file entries
        newDirectory = self.failCheck(directory)
        
    def failCheck(self, newDirectory):
        validResponse = False

        while (validResponse == False):
            #send the command to start stream
            response = self.connectionObj.qps.sendCmdVerbose( "$start stream " + str(newDirectory))
            #if the stream fails, loop until user enters valid name
            if "Fail" in response:
                print (response + ", Please enter a new file name:")
                #grab directory bar end file / folder
                path = os.path.dirname(newDirectory)
                #get a new file name
                if sys.version_info.major==3:                    
                    newEnd = input()
                else:
                    newEnd = raw_input()
                #append user input to directory
                newDirectory = path.replace("\\\\","\\") + newEnd
            else:
                validResponse = True;
        return newDirectory

    def get_stats(self):
        """
                      Returns the QPS annotation statistics grid information as a pandas dataframe object

                                  Returns
                                  -------
                                  df = : dataframe
                                      The response text from QPS. If successful "ok. Saving stats to : file_name" otherwise returns the exception thrown
        """
        try:
            import pandas as pd
            pd.set_option('max_columns', None)
            pd.set_option('display.width', 1024)
        except:
            logging.warning("pandas not imported correctly")
            pass
        time.sleep(1) #TODO remove this sleep, just for demo purposes sb db
        command_response = self.connectionObj.qps.sendCmdVerbose("$get stats")
        if "fail" in command_response.lower():
            raise Exception(command_response)
        test_data = StringIO(command_response)
        df = pd.read_csv(test_data, sep=",")
        return df

    def stats_to_CSV(self, file_name=""):
        """
        Saves the statistics grid to a csv file

                    Parameters
                    ----------
                    file-name= : str, optional
                        The absolute path of the file you would like to save the csv to. If left empty then a filename will be give.
                        Default location is the path of the executable.
                    Returns
                    -------
                    command_response : str or None

                        The response text from QPS. If successful "ok. Saving stats to : file_name" otherwise returns the exception thrown
        """
        command_response = self.connectionObj.qps.sendCmdVerbose("$stats to csv \""+file_name+"\"")
        #TODO check for FAIl message and raise appropriate exception
        if "fail" in command_response.lower():
            raise Exception(command_response)
        return command_response

    def get_custom_stats_range(self, start_time, end_time):
        """
                      Returns the QPS statistics information over a specific time ignoring any set annotations.

                                Parameters
                                ----------
                                start_time = : str
                                    The time in seconds you would like the stats to start this can be in integer or sting format.
                                    or using the following format to specify daysDhours:minutes:seconds.milliseconds
                                    xxxDxx:xx:xx.xxxx
                                end_time = : str
                                    The time in seconds you would like the stats to stop this can be in integer or sting format
                                    or using the following format to specify daysDhours:minutes:seconds.milliseconds
                                    xxxDxx:xx:xx.xxxx
                                Returns
                                -------
                                df = : dataframe
                                    The response text from QPS. If successful "ok. Saving stats to : file_name" otherwise returns the exception thrown
        """
        try:
            import pandas as pd
            pd.set_option('max_columns', None)
            pd.set_option('display.width', 1024)
        except:
            logging.warning("pandas not imported correctly")
            pass
        command_response = self.connectionObj.qps.sendCmdVerbose("$get custom stats range " + start_time+ " " + end_time)
        if "fail" in command_response.lower():
            raise Exception(command_response)
        test_data = StringIO(command_response)
        df = pd.read_csv(test_data, sep=",")
        return df

    def takeSnapshot(self):
        """
                      Triggers QPS take snapshot function and saves it in the streams directory.
        """
        self.connectionObj.qps.sendCmdVerbose("$take snapshot")
        
    def addAnnotation(self, title, annotationTime = 0, extraText="", yPos="", titleColor ="", annotationColor = "", annotationType = "", annotationGroup =""):
        """
                    Adds a custom annotation to stream with given parameters.

                    Parameters
                    ----------
                    title= : str
                        The title appears next to the annotation in the stream
                    extraText= : str, optional
                        The additional text that can be viewed when selecting the annotation
                    yPos : str, optional
                        The percetange of how high up the screen the annotation should appear 0 is the bottom and 100 the top
                    titleColor : str, optional
                        The color of the text next to the annotation in hex format 000000 to FFFFFF
                    annotationColor : str, optional
                        The color of the annotation marker in hex format 000000 to FFFFFF
                    annotationGroup : str, optional
                        The group the annotation belongs to
                    annotationTime : int, optional
                        The time in milliseconds after the start of the stream at which the annotation should be placed. 0 will plot the annotation live at the most recent sample

                    Returns
                    -------
                    command_response : str or None

                        The response text from QPS. "ok" if annotation successfully added
            """
        annotationString = "<"

        if annotationTime == 0:
            # Use current time
            annotationTime = qpsNowStr()
        else:
            # Convert timestamp to QPS format
            annotationTime = toQpsTimeStamp(annotationTime)

        if title != "":
            annotationString += "<text>" + str(title) + "</text>"
        if extraText != "":
            annotationString += "<extraText>" + str(extraText) + "</extraText>"
        if yPos != "":
            annotationString += "<yPos>" + str(yPos) + "</yPos>"
        if titleColor != "":
            annotationString += "<textColor>" + str(titleColor) + "</textColor>"
        if annotationColor != "":
            annotationString += "<color>" + str(annotationColor) + "</color>"
        if annotationGroup != "":
            annotationString += "<userType>" + str(annotationGroup) + "</userType>"
        annotationString += ">"
        # command is sent on newline so \n needs to be chnaged to \\n which is changed back just before printing in qps.
        annotationString = annotationString.replace("\n", "\\n")

        annotationType = annotationType.lower()
        if annotationType == "" or annotationType == "annotation":
            annotationType = "annotate"
        elif annotationType == "comment":
            pass # already in the correct format for command
        else:
            retString = "Fail annotationType must be 'annotation' or 'comment'"
            logging.warning(retString)
            return retString


        logging.debug("Time sending to QPS:" + str(annotationTime))
        return self.connectionObj.qps.sendCmdVerbose("$" +annotationType+" "+str(annotationTime)+" "+annotationString)

    def addComment(self, title, commentTime = 0, extraText="", yPos="", titleColor ="", commentColor = "", annotationType = "", annotationGroup =""):
        #Comments are just annotations that do not affect the statistics grid.
        #This function was kept to be backwards compatible and is a simple pass through to add annotation.
        if annotationType == "":
            annotationType = "comment"
        return self.addAnnotation(title = title, annotationTime=commentTime, extraText=extraText, yPos=yPos, titleColor=titleColor, annotationColor=commentColor, annotationType=annotationType, annotationGroup=annotationGroup)


    def createChannel(self, channelName, channelGroup, baseUnits, usePrefix):
        #Conditions to convert false / true inputs to specification input
        if usePrefix == False: 
            usePrefix = "no"
        if usePrefix == True:
            usePrefix = "yes"

        return self.connectionObj.qps.sendCmdVerbose("$create channel " + channelName + " " + channelGroup  + " " + baseUnits + " " + usePrefix)

    def hideChannel(self, channelSpecifier):
        return self.connectionObj.qps.sendCmdVerbose("$hide channel " + channelSpecifier)

    def showChannel(self, channelSpecifier):
        return self.connectionObj.qps.sendCmdVerbose("$show channel " + channelSpecifier)

    def myChannels(self):
        return self.connectionObj.qps.sendCmdVerbose("$channels")

    def channels(self):
        return self.connectionObj.qps.sendCmdVerbose("$channels").splitlines()
             
    def stopStream(self):
        return self.connectionObj.qps.sendCmdVerbose("$stop stream")

    def hideAllDefaultChannels(self):
        self.hideChannel ("3v3:voltage")
        self.hideChannel ("5v:voltage")
        self.hideChannel ("12v:voltage")
        self.hideChannel ("3v3:current")
        self.hideChannel ("5v:current")
        self.hideChannel ("12v:current")
        self.hideChannel ("3v3:power")
        self.hideChannel ("5v:power")
        self.hideChannel ("12v:power")
        self.hideChannel ("tot:power")
            

    #function to add a data point the the stream
    #time value will default to current time if none passed
    def addDataPoint(self, channelName, groupName, dataValue, dataPointTime = 0):
        if dataPointTime == 0:
            dataPointTime = qpsNowStr()
        else:
            dataPointTime = toQpsTimeStamp (dataPointTime)

        #print ("printing command:  $log " + channelName + " " + groupName + " " + str(dataPointTime) + " " + str(dataValue))
        self.connectionObj.qps.sendCmdVerbose("$log " + channelName + " " + groupName + " " + str(dataPointTime) + " " + str(dataValue))