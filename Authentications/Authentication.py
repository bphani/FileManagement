from fastapi import Depends, FastAPI, Header, HTTPException
from Bridges.AuthenticationService import is_auth


def is_login(id: Header(...), token:Header(...)):
    result = is_auth(id, token)
    if result:
        return result
    else:
        raise HTTPException(status_code=403, detail="Login Required")

