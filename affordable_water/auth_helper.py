from requests_oauthlib import OAuth2Session
from .settings import MS_APP_ID, MS_APP_SECRET, MS_AUTHORITY, MS_AUTHORIZE_ENDPOINT, MS_REDIRECT, MS_SCOPES, MS_TOKEN_ENDPOINT
import os

# This is necessary because Azure does not guarantee
# to return scopes in the same case and order as requested
os.environ['OAUTHLIB_RELAX_TOKEN_SCOPE'] = '1'
os.environ['OAUTHLIB_IGNORE_SCOPE_CHANGE'] = '1'

def get_sign_in_url():
    # Initialize the OAuth client
    aad_auth = OAuth2Session(MS_APP_ID, scope=MS_SCOPES, redirect_uri=MS_REDIRECT)

    sign_in_url, state = add_auth.authorization_url(MS_AUTHORIZE_ENDPOINT, prompt='login')

    return sign_in_url, state

def get_token_from_code(callback_url, expected_state):
    # Initialize the OAuth client
    aad_auth = OAuth2Session(MS_APP_ID, state=expected_state, scope=MS_SCOPES, redirect_uri=MS_REDIRECT)

    token = aad_auth.fetch_token(MS_TOKEN_ENDPOINT, client_secret=MS_APP_SECRET, authorization_reponse=callback_url)

    return token