import websockets
async def _send_msg(msg, uri):    
    """ open connection send message and return the query """    
    async with websockets.connect(uri) as websocket:                                            
        await websocket.send(msg)        
        result = await websocket.recv()
        return result