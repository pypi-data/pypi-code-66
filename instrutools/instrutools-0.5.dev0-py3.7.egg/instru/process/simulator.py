import time
from .thread import Thread, register_thread, unregister_thread

simulator = None

simulator_dict = {}

def is_simulator_running():
    global simulator    
    return simulator and simulator.isrunning()

def start_simulator():
    global simulator    
        
    simulator = Simulator()        
    simulator.start()
    register_thread(simulator)
    

def stop_simulator():
    global simulator
    simulator.kill()
    unregister_thread(simulator)
    simulator = None

def add_simulator_callback(delay, callback):
    global simulator
    if simulator is None or not simulator._livesignal:
        raise ValueError('simulator is not running')
    simulator.callbacks[time.time()+delay] = callback
    
class Simulator(Thread):
    _livesignal = True
    callbacks = None
    
    def __init__(self, delay=0.1):
        self.callbacks = {}
        self.delay = delay
        Thread.__init__(self)
    
    def kill(self):
        self._livesignal = False
    
    def run(self):
        self.callbacks = {}
        callbacks = self.callbacks
        delay = self.delay 
        self._livesignal = True
        while self._livesignal:
            t_start = time.time()
            for t, callback in list(callbacks.items()):
                if t<t_start:
                    callback()
                    callbacks.pop(t)
            time.sleep(delay)