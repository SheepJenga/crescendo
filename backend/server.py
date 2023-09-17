# load env vars
import dotenv
dotenv.load_dotenv()

from flask import Flask, render_template, session, abort, redirect, request
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
    create_user(crescendo_clients, "test", "test", "test@gmail.com", "test")
    return "Hello World <a href='/login'> <button>Login</button> </a>"

@app.route("/login")
def login():
    authorization_url, state = flow.authorization_url()
    session["state"] = state
    print(state)
    return redirect(authorization_url)

@app.route("/logout")
def logout():
    session.clear()
    return redirect("/")

@app.route("/callback")
def callback():
    flow.fetch_token(authorization_response=request.url)

    if not session["state"] == request.args["state"]:
        abort(500) # States doesn't match

    credentials = flow.credentials
    request_session = requests.session()
    cached_session = cachecontrol.CacheControl(request_session)
    token_request = google.auth.transport.requests.Request(session=cached_session)
    print(credentials)

    id_info = id_token.verify_oauth2_token(
        id_token=credentials._id_token,
        request=token_request,
        audience=os.environ["GOOGLE_CLIENT_ID"],
        clock_skew_in_seconds=10
    )

    session["google_id"] = id_info.get("sub")
    session["name"] = id_info.get("name")

    return redirect("/protected_area")


@app.route("/protected_area")
@login_is_required
def protected_area():
    return "Protected! <a href='/logout'> <button>Logout</button> </a>"

if __name__ == "__main__":
    app.run(port=8080, debug=True)