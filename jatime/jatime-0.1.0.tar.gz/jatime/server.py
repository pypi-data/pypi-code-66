from flask import Flask, jsonify, request
from werkzeug.exceptions import BadRequest

from jatime import __copyright__, __description__, __license__, __title__, __version__
from jatime.analyzer import analyze

app = Flask("jatime")
app.config["JSON_AS_ASCII"] = False


@app.route("/")
def root():
    return jsonify(
        {
            "name": __title__,
            "description": __description__,
            "version": __version__,
            "license": __license__,
            "copyright": __copyright__,
        }
    )


@app.route("/analysis")
def get_analysis():
    string = request.args.get("string", None)
    if string is None:
        raise BadRequest("Parameter `string` is required.")
    # TODO: allow base time to be specified.
    return jsonify(analyze(string))


@app.after_request
def edit_header(response):
    response.headers["Access-Control-Allow-Origin"] = "*"
    return response


@app.errorhandler(Exception)
def handle_exception(e):
    return jsonify({"error": e.name, "details": e.description}), e.code
