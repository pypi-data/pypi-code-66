from FlaskSSL.api.controllers import *


# Routing
routes = [
    (Test, '/'),
    (Help, '/help'),
    (Cert, '/cert')
]
