""" provide an image of a remote database 

For the moment, this is brutal, the full database is updated every seconds. 
Running server and client on my local computer, it takes ~12ms to update

on the client side: 
>>> db = DataBaseImage()
>>> db.start_monitoring()

The DataBaseImage object is however readonly, it is expected that on client 
we are setting database value with 
>>> send_message('db', 'set', {'values':[(K1,V1), K2,V3), ...]})
"""
from ..database.db import DataBase, path_join
from ..process.thread import Thread, register_thread, unregister_thread
import time

class DataBaseImage(DataBase):
    """ DataBaseImage works like a DataBase except that this is a copy of a server DataBase
    
    The DataBaseImage is readonly and allows to have a full representation of the 
    system running on the server from the client
    
    Args:
        client: a `Client` object communicating with server 
    
    Methods:
        All methods of DataBase, plus:
            start_monitoring(): will run a thread that update the full database 
                                periodicaly 
            stop_monitoring(): stop the monitor thread 
            is_monitored(): true if the monitor thread is running             
    """
    _monitor_thread = None
    client = None
    def __init__(self, client):
        self.client = client
        DataBase.__init__(self, {})    
    
    def set(self, key, value):
        """ DataBaseImage is readonly use the client.db_set instead """
        raise KeyError("The local image of the database is readonly")
    
    def update(self, __d__={}, **kwargs):
        """ DataBaseImage is readonly use the client.db_set instead """
        raise KeyError("The local image of the database is readonly")
        
    def start_monitoring(self, delay=1.0):
        """ start the monitoring thread of the database. 
        
        For each cycle of period DELAY the full database is updated. 
        """
        if self._monitor_thread is not None:
            self._monitor_thread.kill()
        self._monitor_thread = DictMonitorThread(self.client, self._d, delay=delay)        
        self._monitor_thread.start()
        register_thread(self._monitor_thread)
        
    def stop_monitoring(self):
        """ stop the monitoring thread if exists 
        
        if thread is not running do nothing
        """
        if self._monitor_thread is not None:
            self._monitor_thread.kill()
            unregister_thread(self._monitor_thread)
        self._monitor_thread = None
    
    def is_monitored(self):
        """ return True if the monitoring thread is running """
        return self._monitor_thread is not None and self._monitor_thread._livesignal
    
    def selfupdate(self, key_list=None):
        """ update the database from the server
        
        Args:
            key_list: None or list 
                if None, the full DataBase is updated
                if a list update the DataBase points given in the list 
        """  
        try:
            if key_list is None:            
                res = self.client.send("db", "_flush")
            else:
                res = self.client.send("db", "_query",  {"keywords":list(key_list)})            
        except Exception as er:
            raise RuntimeError("cannot retrieve data base values ! %s"%er)
        else:
            if res['status']:
                raise RuntimeError("cannot retrieve data base values {rtype} {message}".format(**res))                
            else:                
                self._d.update(res['return'])

class DataBaseImageRW(DataBaseImage):
    def set(self, key, value):
        """ Update the server value retrieve it and update locally """
        r = self.client.send("db", "_set", {'values':[[path_join(key),value]]})
        if r['status']:
            raise KeyError("{message}".format(**r))
        self._d.update( r['return'] )        
    
    def update(self, __d__={}, **kwargs):
        """  """
        d = {path_join(key):value for key,value in dict(__d__, **kwargs).items()}
        r = self.client.send("db", "_set", {'values':d})
        if r['status']:
            raise KeyError("{message}".format(**r))
        self._d.update( r['return'] )

class DictMonitorThread(Thread):
    def __init__(self, client, d, delay=1.0):
        self.client = client
        self.delay = delay 
        self.d = d
        Thread.__init__(self)
        
    def run(self):                        
        while self._livesignal:   
            stime = time.time()         
            try:            
                res = self.client.send("db", "_flush")
            except Exception as er:
                print("BUG: cannot retrieve data base values !", er)
            else:
                if res['status']:
                    print("BUG: cannot retrieve data base values {rtype} {message}".format(**res))
                    
                else:
                    self.d.update(res['return'])
            etime = time.time()
            #print("done in", etime-stime, "s")
            time.sleep(max(self.delay - (etime-stime), 0.001 ))
    
    