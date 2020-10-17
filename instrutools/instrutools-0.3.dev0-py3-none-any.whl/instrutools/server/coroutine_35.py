import asyncio
import json

def coroutine(process):
    @asyncio.coroutine
    def receive(websocket, path, process=process):                             
        for smsg in websocket:                              
            msg = json.loads(smsg)
            
            proc = msg['process']
            cmd = msg['cmd']
            args = msg.get('args', {})
            timeout = msg.get('timeout', None)
            
            result = process(proc, cmd, args, timeout)
            yield from websocket.send(json.dumps(result))
    return receive
