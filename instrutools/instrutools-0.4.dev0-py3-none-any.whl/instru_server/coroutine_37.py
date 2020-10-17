import asyncio
import json

#signal.signal(signal.SIGINT, sigint_handler)

def coroutine(process):
    async def receive(websocket, path, process=process):                             
        async for smsg in websocket:
            msg = json.loads(smsg)
            
            proc = msg['process']
            cmd = msg['cmd']
            args = msg.get('args', {})
            timeout = msg.get('timeout', None)
            
            result = process(proc, cmd, args, timeout)
            await websocket.send(json.dumps(result))
    return receive
