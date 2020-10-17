from semaphore_client import Configuration, ApiClient, Login, api


class TestHelper:


    def __init__(self, semaphore_base_url=None,semaphore_username=None,semaphore_password=None):
        if not semaphore_base_url:
            self.semaphore_base_url = 'http://127.0.0.1:3000/api'
        if not semaphore_username:
            self.semaphore_username = 'admin'
        if not semaphore_password:
            self.semaphore_password = 'password'
        self.init_semaphore_client()



    def init_semaphore_client(self):
        configuration = Configuration()
        configuration.host = self.semaphore_base_url
        configuration.username = self.semaphore_username
        configuration.password = self.semaphore_password
        self.api_client = ApiClient(configuration=configuration)
        self.authentication_api = api.AuthenticationApi(api_client=self.api_client)
        self.default_api = api.DefaultApi(api_client=self.api_client)
        self.project_api = api.ProjectApi(api_client=self.api_client)
        self.user_api = api.UserApi(api_client=self.api_client)
        self.projects_api = api.ProjectsApi(api_client=self.api_client)