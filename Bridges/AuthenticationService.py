import requests
import json
import logging

debug = False
if debug:
    base_url = "http://localhost:3001"
else:
    base_url = "http://chichiapp.ir:30031"


def is_auth(user_id, token):
    try:
        content = requests.get('{0}/users/auth/check/{1}/{2}'.format(base_url,
                                                                     user_id,
                                                                     token)).content
        content = json.loads(content)

        if content["State"]:
            return True
        else:
            return False
    except Exception as ex:
        logging.warning(ex.args)
        return False
