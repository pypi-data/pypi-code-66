import websockets
import asyncio

@asyncio.coroutine 
def _send_msg(msg, uri):    
    """ open connection send message and return the query """    
    with websockets.connect(uri) as websocket:                                            
        yield from  websocket.send(msg)        
        result = yield from websocket.recv()
        return result