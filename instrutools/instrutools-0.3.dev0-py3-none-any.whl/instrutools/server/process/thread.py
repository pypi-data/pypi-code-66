import threading
import time

class Thread(threading.Thread):
    _livesignal = True
    def __init__(self):
        self._livesignal = True
        self._lock = False
        threading.Thread.__init__(self)
     
    def kill(self):
        self._livesignal = False
     
    def isrunning(self):
        return self._livesignal
    

class FuncThread(Thread):
    def __init__(self, func, description="", delay=1.0):
        self.func = func
        self.delay = delay
        self.description = description
        Thread.__init__(self)
        
    def run(self):
        delay = self.delay 
        func = self.func
        self._livesignal = True
        while self._livesignal:
            stime = time.time()  
            try:    
                func()
            except Exception as er:
                print("BUG: thread %s!"%self.description, er)
                        
            etime = time.time()
            #print("done in", etime-stime, "s")
            time.sleep(max(delay - (etime-stime), 0.001 ))
        

def func_thread(func, name="", delay=1.0):
    thread = FuncThread(func, name=name, delay=delay)
    register_thread(thread)
    return thread
    
    
_thread_loockup = set()
def register_thread(thread):
    global _thread_loockup
    _thread_loockup.add(thread)
 
def unregister_thread(thread):     
    try:
        _thread_loockup.remove(thread)
    except KeyError:
        pass
 
def kill_all_threads():
    for thread in _thread_loockup:
        thread.kill()
