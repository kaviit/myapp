"""Python web api application"""

from flask import Flask, jsonify, render_template, abort  # import objects from the flask model
from flask.logging import create_logger
import helper, logging

app_details = helper.get_details()
SERVICENAME = app_details["service_name"]
VERSION = app_details["version"]
PORT = app_details["service_port"]
GIT_COMMIT_SHA = app_details["git_commit_sha"]

app = Flask(__name__, template_folder="templates")  # define app using flask
log = create_logger(app)
app.config["JSON_SORT_KEYS"] = False   

logging.basicConfig(
    level=logging.INFO, format="%(asctime)s %(levelname)s : %(message)s"
)

@app.route("/", methods=["GET"])
def home():
    """Index page of web api"""
    return render_template('index.html')

@app.route("/info", methods=["GET"])
def api_info():
    """ Function to provide GET http request for api calls"""
    log_level = logging.getLevelName(log.getEffectiveLevel())
    try:
       response = {
        "service_name": SERVICENAME,
        "version": VERSION,
        "git_commit_sha": GIT_COMMIT_SHA,
        "environment" : {
        "service_port": PORT, 
        "log_level": log_level,
        }
       }
       return jsonify(response)
    except:
        log.error("Exception at api info request")
        abort(500)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=PORT) 

