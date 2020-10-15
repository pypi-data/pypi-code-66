from flask import Flask
from flask_restful import Api

from FlaskSSL.api.routes import routes

# Initialization
application = Flask(__name__)
api = Api(application)

# Routing
for route in routes:
    api.add_resource(*route)


def main():
    application.run(host='0.0.0.0', port=5000, debug=True)


if __name__ == '__main__':
    main()
