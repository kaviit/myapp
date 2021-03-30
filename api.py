"""Python web api application"""

from flask import Flask, jsonify  # import objects from the flask model
import helper, logging

app_details = helper.get_details()
SERVICENAME = app_details["service_name"]
VERSION = app_details["version"]
PORT = app_details["service_port"]
LOG_LEVEL = app_details["log_level"]
GIT_COMMIT_SHA = app_details["git_commit_sha"]

app = Flask(__name__)  # define app using flask
app.config["JSON_SORT_KEYS"] = False   

logging.basicConfig(
    level=logging.INFO, format="%(asctime)s %(levelname)s : %(message)s"
)

@app.route("/", methods=["GET"])
def test():
    return jsonify({"message": "it works!"})


@app.route("/info", methods=["GET"])
def api_info():
    """ Function to provide GET http request for api calls"""
    try:
       response = {
        "service_name": SERVICENAME,
        "version": VERSION,
        "git_commit_sha": GIT_COMMIT_SHA,
        "environment" : {
        "service_port": PORT, 
        "log_level": LOG_LEVEL,
        }
       }
       return jsonify(response)
    except:
        logging.error("Exception at api info request")
        abort(500)

if __name__ == "__main__":
    app.run(
        debug=True, host="0.0.0.0", port=PORT
    )  # run app on service_port in debug mode

