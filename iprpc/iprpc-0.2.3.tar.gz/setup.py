# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['iprpc']

package_data = \
{'': ['*']}

install_requires = \
['jsonschema>=3.2.0,<4.0.0',
 'pydantic>=1.4,<2.0',
 'strict-rfc3339>=0.7,<0.8',
 'tinyrpc>=1.0.4,<2.0.0']

extras_require = \
{'aioapp': ['aioapp-http>=0.0.1b6,<0.0.2'],
 'aiohttp': ['aiohttp>=3.4.4,<4.0.0']}

setup_kwargs = {
    'name': 'iprpc',
    'version': '0.2.3',
    'description': 'InPlat JSON RPC library',
    'long_description': 'IPRPC\n=====\n\nБиблиотека для разбора json-rpc подобных запросов, их валидации и вызова методов.\n\nПример использования::\n\n    from iprpc import method, MethodExecutor\n\n    class Handler:\n        @method()\n        async def sum(self, a: int, b: int) -> int:\n            return a + b\n\n    executor = MethodExecutor(Handler())\n    res = await executor.call(b\'{"method":"sum","params":{"a":1,"b":2}}\')\n    assert res.result == 3\n    assert res.error is None\n\n    res = await executor.call(b\'{"method":"sum","params":{"a":"NaN","b":2}}\')\n    assert res.result is None\n    assert res.error is not None\n    print(res.error)\n    >> InvalidArguments(Exception(\'value is not a valid integer in a\',),)\n\niprpc.MethodExecutor видит только те методы, которые отмечены декоратором iprpc.method.\nЕсли требуется дать сложное имя метода(например использовать спецсимволы в названии),\nто в декораторную функцию необходимо передать аргумент name с названием метода::\n\n    class Handler:\n        @method(name="math.sum")\n        async def sum(self, a: int, b: int) -> int:\n            return a + b\n\nПри этом вызвать метод передав в него имя метода соответствующее название функции\npython уже не получится. Т.е., в примере выше, вызов\n`{"method":"sum","params":{"a":1,"b":2}`\nзавершится ошибкой.\nНужно^ `{"method":"math.sum","params":{"a":1,"b":2}`\n\nСтруктура запроса\n-----------------\n\nПо-умолчанию структура запроса должна соответствовать следующей JSON схеме::\n\n    {\n        "type": "object",\n        "required": [ "method" ],\n        "properties": {\n            "method": {\n                "type": "string"\n            },\n            "params": {\n                "type": "object"\n            }\n        }\n    }\n\nСтруктура может быть изменена. Ключи объека запроса с именем метода или/и параметрами\nмогут иметь другие значения.\nДля этого нужно в MethodExecutor передать аргумент method_key или/и params_key::\n\n    executor = iprpc.MethodExecutor(TestHandler(), method_key=\'name\', params_key=\'args\')\n    await executor.call(b\'{"name":"sum","args":{"a":1,"b":2}}\')\n\nТакже аргументы метода можно передавать в корне запроса. Для этого params_key должен\nбыть равен None::\n\n    executor = iprpc.MethodExecutor(TestHandler(), params_key=None)\n    await executor.call(b\'{"method":"sum","a":1,"b":2}\')\n\n\nВалидация с помощью JSON Schema\n-------------------------------\n\nДля задания правил валидации нужно передать в декоратор список правил.\nПравила представляют собой словарь, где ключ - это имя аргумента, а значение - это\njson схема.\nПример::\n\n    class Handler:\n\n        @method(validators={"a": {"type": "integer"},"b": {"type": "integer"}})\n        async def sum(self, a, b):\n            return a + b\n\n\n\nВалиация с помощью pydantinc\n----------------------------\n\nВалидация происходит автоматически если есть аннотации типов в объявлении метода.\nНапример::\n\n    class Handler:\n        @method()\n        async def sum(self, a: int, b: int):\n            return a + b\n\nПри этом в запросе можно передавать значение в виде строки или другого совместимого\nтипа, значение будет автоматически преобразовано(если это возможно).\n\n\nСериализация результата\n-----------------------\n\nРезультат вызываемой функции будет преобразован к простым типам данных для\nдальнейшей сериализация в JSON.\nНапример, если метод возвращает объект datetime, то он будет преобразован в строку в iso формате.\nДля большей информации см. функцию `pydantic.json.pydantic_encoder`\n\nСложный пример::\n\n    from pydantic import BaseModel\n\n    class User(BaseModel):\n        id: int\n        name: str\n\n    class Handler:\n        @method()\n        async def rename(self, model: User, name: str) -> User:\n            model.name = name\n            return model\n\n    executor = MethodExecutor(Handler())\n    r = await executor.call(b\'{"method":"rename","params":{"model": {"id": 1, "name": "Jhon Snow"},"name": "Jon Snow"}}\'\n    print(r.result)\n    >> {\'id\': 1, \'name\': \'Jon Snow\'}\n\n\nJSON-RPC 2.0\n------------\n\nПример::\n\n    from iprpc import method, JsonRpcError, JsonRpcExecutor\n\n    class Handler:\n        @method()\n        async def do_something(self, arg1: str):\n            return arg1\n\n    executor = JsonRpcExecutor(Handler())\n\n    request = (\n        b\'{"jsonrpc": "2.0", "id": 1, \'\n        b\'"method": "do_something", "params": {"arg1": 123}}\'\n    )\n    resp = await executor.execute(request)\n\n    print(\'<< %s\' % resp)\n    << b\'{"jsonrpc": "2.0", "id": 1, "result": "123"}\'\n',
    'author': 'Konstantin Stepanov',
    'author_email': None,
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://gitlab.app.ipl/inplat/iprpc/',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'extras_require': extras_require,
    'python_requires': '>=3.6,<4.0',
}


setup(**setup_kwargs)
