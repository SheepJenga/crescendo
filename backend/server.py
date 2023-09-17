# load env vars
import dotenv
dotenv.load_dotenv()

from flask import Flask, render_template, session, abort, redirect, request, jsonify
from flask_cors import CORS
from google_auth_oauthlib.flow import Flow

import pip._vendor.cachecontrol as cachecontrol
import os
import pathlib
import requests
import google
import google.oauth2.id_token as id_token

from clients import crescendo_clients
from service.create_user import create_user
import models


app = Flask(__name__)
app.secret_key = "Test-secret-key"
CORS(app) # This will enable CORS for all routes

os.environ["OAUTHLIB_INSECURE_TRANSPORT"] = "1"

client_secrets_file = os.path.join(pathlib.Path(__file__).parent, "client_secret.json")

flow = Flow.from_client_secrets_file(client_secrets_file=client_secrets_file,
                                     scopes=["https://www.googleapis.com/auth/userinfo.profile", "https://www.googleapis.com/auth/userinfo.email", "openid"],
                                     redirect_uri="http://127.0.0.1:8080/callback")

def login_is_required(function):
    def wrapper(*args, **kwargs):
        if "google_id" not in session:
            return abort(401) # Authorization required
        else:
            return function()
    
    return wrapper

@app.route("/", methods=["GET"])
def index():
    return "Hello World <a href='/login'> <button>Login</button> </a>"

# @app.route("/login")
# def login():
#     authorization_url, state = flow.authorization_url()
#     session["state"] = state

#     return redirect(authorization_url)

# @app.route("/logout")
# def logout():
#     session.clear()
#     return redirect("/")

# @app.route("/callback")
# def callback():
#     flow.fetch_token(authorization_response=request.url)

#     if not session["state"] == request.args["state"]:
#         abort(500) # States doesn't match

#     credentials = flow.credentials
#     request_session = requests.session()
#     cached_session = cachecontrol.CacheControl(request_session)
#     token_request = google.auth.transport.requests.Request(session=cached_session)

#     id_info = id_token.verify_oauth2_token(
#         id_token=credentials._id_token,
#         request=token_request,
#         audience=os.environ["GOOGLE_CLIENT_ID"],
#         clock_skew_in_seconds=10
#     )

#     session["google_id"] = id_info.get("sub")
#     session["name"] = id_info.get("name")
#     session["first_name"] = id_info.get("given_name")
#     session["last_name"] = id_info.get("family_name")
#     session["email"] = id_info.get("email")
#     session["profile_picture"] = id_info.get("picture")

#     return redirect("/finish_login")


@app.route("/login/<string:email>")
@login_is_required
def finish_login():
    user = create_user(crescendo_clients, session["first_name"], session["last_name"], session["email"], session["name"], session["profile_picture"])
    return jsonify({
        "id": user.id,
        "username": user.username,
        "email": user.email,
        "first_name": user.first_name,
        "last_name": user.last_name,
        "profile_picture": user.profile_picture,
        "creator_id": user.creator_id,
    })

@login_is_required
@app.route("/api/user/<int:user_id>")
def get_user(user_id):
    user = crescendo_clients.db_client.get_first(models.Account, conds={"id": user_id})
    return jsonify({
        "id": user.id,
        "username": user.username,
        "email": user.email,
        "first_name": user.first_name,
        "last_name": user.last_name,
        "profile_picture": user.profile_picture,
        "creator_id": user.creator_id,
    })

if __name__ == "__main__":
    app.run(port=8080, debug=True)