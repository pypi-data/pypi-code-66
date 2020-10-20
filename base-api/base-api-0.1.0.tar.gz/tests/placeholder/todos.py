from baseapi.apis import RestApi


class TodosApi(RestApi):
    def list_todos(self):
        return self.get('/todos')

    def _just_a_test(self):
        # Shouldn't be exposed.
        pass
