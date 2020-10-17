import json

class DataSource:

    @classmethod
    def run(cls):
        quiz = ''
        json_data = {}
        has_finish = True
        all_data = {}

        with open('server/assets/data_source_quiz.json', 'r') as src:
            data = src.read()
            all_data = json.loads(data)

        for item in all_data.keys() :
            quiz = all_data[item]
            values = cls.simple_quiz(quiz)
            json_data[item] = values

        with open(f'server/data_source.json', 'w') as src:
            data_ftd = {
                "host": json_data['host'],
                "user": json_data['user'],
                "password": json_data['password'],
                "dbname": json_data['dbname'],
                "datasource": json_data['datasource'],
            }
            json.dump(data_ftd, src, indent=4)
    
    @classmethod
    def simple_quiz(cls, data):
        resp = input(data)
        return resp