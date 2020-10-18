import asyncio
import json

#signal.signal(signal.SIGINT, sigint_handler)

def coroutine(process):
    async def receive(websocket, path, process=process):                             
        async for smsg in websocket:
            msg = json.loads(smsg)
            
            cmd = msg['cmd']
            args = msg['args']
            
            result = process(cmd, *args)
            await websocket.send(json.dumps(result))
    return receive
