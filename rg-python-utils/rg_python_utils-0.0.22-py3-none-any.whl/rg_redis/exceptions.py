class _Exception(Exception):

    def __init__(self, error: str, exception_type: str = None, json_data_received: dict = None, **kwargs):
        self.error = error
        self.extra_args = {"error": error, "exception_type": exception_type}
        self.json_data_received = json_data_received

        if kwargs:
            for key, value in kwargs.items():
                if key == 'kwargs':
                    continue
                self.extra_args[key] = value

    def get_dict(self) -> dict:
        if self.json_data_received:
            self.extra_args["json_data_received"] = self.json_data_received

        return self.extra_args


class RedisSettingsNotFoundException(_Exception):
    def __init__(self, redis_settings_name: str):
        msg = 'Redis Settings not declared in settings.py file, please add settings for: ' + redis_settings_name
        _Exception.__init__(self, msg, exception_type='RedisSettingsNotFoundException')


class RedisConnectionNotInitialize(_Exception):
    def __init__(self, redis_settings_name: str):
        msg = 'Redis Connection  not initialized/ready for rg_redis instance: ' + redis_settings_name
        _Exception.__init__(self, msg, exception_type='RedisConnectionNotReadyException')


class RGRedisException(Exception):
    pass
