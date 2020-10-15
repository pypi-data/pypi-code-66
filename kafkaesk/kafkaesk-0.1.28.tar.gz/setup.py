# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['kafkaesk', 'kafkaesk.ext', 'kafkaesk.ext.logging']

package_data = \
{'': ['*']}

install_requires = \
['aiokafka>=0.6.0,<0.7.0',
 'jsonschema>=3.2.0,<4.0.0',
 'kafka-python>=2.0.1,<3.0.0',
 'opentracing>=2.3.0,<3.0.0',
 'orjson>=3.0.0,<4.0.0',
 'prometheus_client>=0.8.0,<0.9.0',
 'pydantic>=1.5.1,<2.0.0']

entry_points = \
{'console_scripts': ['kafkaesk = kafkaesk.app:run']}

setup_kwargs = {
    'name': 'kafkaesk',
    'version': '0.1.28',
    'description': 'Easy publish and subscribe to events with python and Kafka.',
    'long_description': '# kafkaesk\n\nThis project is meant to help facilitate easily publishing and subscribing to events with python and Kafka.\n\nGuiding principal:\n - simple http, language agnostic contracts built on top of kafka.\n\nAlternatives:\n - pure aiokafka: can be complex to scale correctly\n - guillotina_kafka: complex, tied to guillotina\n - faust: requires additional data layers, not language agnostic\n - confluent kafka + avro: close but ends up being like grpc. compilation for languages. No asyncio.\n\n(consider this python project as syntatic sugar around these ideas)\n\n## Publish\n\nusing pydantic but can be done with pure json\n\n```python\nimport kafkaesk\nfrom pydantic import BaseModel\n\napp = kafkaesk.Application()\n\n@app.schema("Content", version=1, retention=24 * 60 * 60)\nclass ContentMessage(BaseModel):\n    foo: str\n\n\nasync def foobar():\n    # ...\n    # doing something in an async func\n    await app.publish("content.edited.Resource", data=ContentMessage(foo="bar"))\n```\n\n\n## Subscribe\n\n\n```python\nimport kafkaesk\nfrom pydantic import BaseModel\n\napp = kafkaesk.Application()\n\n@app.schema("Content", version=1, retention=24 * 60 * 60)\nclass ContentMessage(BaseModel):\n    foo: str\n\n\n@app.subscribe(\'content.*\')\nasync def get_messages(data: ContentMessage):\n    print(f"{data.foo}")\n\n```\n\n\n## Avoiding global object\n\nIf you do not want to have global application configuration, you can lazily configure\nthe application and register schemas/subscribers separately.\n\n```python\nimport kafkaesk\nfrom pydantic import BaseModel\n\nrouter = kafkaesk.Router()\n\n@router.schema("Content", version=1, retention=24 * 60 * 60)\nclass ContentMessage(BaseModel):\n    foo: str\n\n\n@router.subscribe(\'content.*\')\nasync def get_messages(data: ContentMessage):\n    print(f"{data.foo}")\n\n\nif __name__ == \'__main__\':\n    app = kafkaesk.Application()\n    app.mount(router)\n    kafkaesk.run(app)\n\n```\n\n\nOptional consumer injected parameters:\n\n- schema: str\n- record: aiokafka.structs.ConsumerRecord\n\nDepending on the type annotation for the first parameter, you will get different data injected:\n\n- `async def get_messages(data: ContentMessage)`: parses pydantic schema\n- `async def get_messages(data: bytes)`: give raw byte data\n- `async def get_messages(record: aiokafka.structs.ConsumerRecord)`: give kafka record object\n- `async def get_messages(data)`: raw json data in message\n\n\n## kafkaesk contract\n\nThis is just a library around using kafka.\nKafka itself does not enforce these concepts.\n\n- every message must provide a json schema\n- messages produced will be validated against json schema\n- each topic will have only one schema\n- a single schema can be used for multiple topics\n- consumed message schema validation is up to the consumer\n- messages will be consumed at least once. Considering this, your handling should be idempotent\n\n### message format\n\n```json\n{\n    "schema": "schema_name:1",\n    "data": { ... }\n}\n```\n\n\n# Worker\n\n```bash\nkafkaesk mymodule:app --kafka-servers=localhost:9092\n```\n\nOptions:\n\n - --kafka-servers: comma separated list of kafka servers\n - --kafka-settings: json encoded options to be passed to https://aiokafka.readthedocs.io/en/stable/api.html#aiokafkaconsumer-class\n - --topic-prefix: prefix to use for topics\n - --replication-factor: what replication factor topics should be created with. Defaults to min(number of servers, 3).\n\n\n## Application.publish\n\n- stream_id: str: name of stream to send data to\n- data: class that inherits from pydantic.BaseModel\n- key: Optional[bytes]: key for message if it needs one\n\n## Application.subscribe\n\n- stream_id: str: fnmatch pattern of streams to subscribe to\n- group: Optional[str]: consumer group id to use. Will use name of function if not provided\n\n\n## Application.schema\n\n- id: str: id of the schema to store\n- version: Optional[int]: version of schema to store\n- streams: Optional[List[str]]: if streams are known ahead of time, we can pre-create them before we push data\n- retention: Optional[int]: retention policy in seconds\n\n\n## Application.configure\n\n- kafka_servers: Optional[List[str]]: kafka servers to connect to\n- topic_prefix: Optional[str]: topic name prefix to subscribe to\n- kafka_settings: Optional[Dict[str, Any]]: additional aiokafka settings to pass in\n- replication_factor: Optional[int]: what replication factor topics should be created with. Defaults to min(number of servers, 3).\n\n## Dev\n\n```bash\npoetry install\n```\n\nRun tests:\n\n```bash\ndocker-compose up\nKAFKA=localhost:9092 poetry run pytest tests\n```\n\n# Extensions\n## Logging\nThis extension includes classes to extend python\'s logging framework to publish structured log messages to a kafka topic.  This extension is made up of three main components: an extended `logging.LogRecord`, a custom `logging.Formatter`, and a some custom `logging.Handler`s.\n\nSee `logger.py` in examples directory.\n\n### Log Record\n`kafkaesk.ext.logging.record.factory` is a function that will return `kafkaesk.ext.logging.record.PydanticLogRecord` objects.  The `factory()` function scans through any `args` passed to a logger and checks each item to determine if it is a subclass of `pydantid.BaseModel`.  If it is a base model instance and `model._is_log_model` evaluates to `True` the model will be removed from `args` and added to `record._pydantic_data`.  After that `factory()` will use logging\'s existing logic to finish creating the log record.\n\nThe `factory()` function is automatically passed to `logging.setLogRecordFactory` when a `kafkaesk.ext.logging.formatter.PydanticFormatter` instance is created.\n\n### Formatter\n`kafkaesk.ext.logging.formatter.PydanticFormatter` is responsible for parsing all information in a log record and returning a `kafkaesk.logging.formatter.PydanticLogModel` instance.  The formatter will build the return message in two passes.  The first pass looks at `formatter.format_class` and attempts to create an instance of that class utilizing the log record\'s `__dict__`.  The second pass creates a standard dictionary from all models present in a log record\'s `_pydantic_data` property.  These results are then merged together and used to create a new `PydanticLogModel` instance which is returned to the handler.\n\n### Handler\nThis extensions ships with two handlers capable of handling `kafkaesk.ext.logging.formatter.PydanticLodModel` classes: `kafakesk.ext.logging.handler.PydanticStreamHandler` and `kafkaesk.ext.logging.handler.PydanticKafkaeskHandler`.  \n\nThe stream handler is a very small wrapper around `logging.StreamHandler`, the signature is the same, the only difference is that the handler will attempt to convert any pydantic models it receives to a json string.\n\nThe kafkaesk handler has a few more bits going on in the background.  The handler has two required inputs, a `kafkaesk.app.Application` instance and a stream name.  Once initialized any logs emitted by the handler will be saved into an internal queue.  There is a worker task that handles pulling logs from the queue and writing those logs to the specified topic.\n\n# TODO\n\n(or a todo here)\n\n- [ ] be able to handle manual commit use-case\n- [ ] be able to reject commit/abort message handling\n\n# Naming things\n\nIt\'s hard and "kafka" is already a fun name. Hopefully this library isn\'t literally "kafkaesque" for you.\n',
    'author': 'vangheem',
    'author_email': 'vangheem@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.7,<4.0',
}


setup(**setup_kwargs)
