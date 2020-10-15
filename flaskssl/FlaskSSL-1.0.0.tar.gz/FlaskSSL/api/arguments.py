from flask_restful.reqparse import RequestParser


# Arguments
parser = RequestParser()
parser.add_argument('domain', action='append')
parser.add_argument('email', type=str)
parser.add_argument('staging', type=int, default=0)


def parse_args():
    """Parse arguments and extract data."""
    return parser.parse_args()
