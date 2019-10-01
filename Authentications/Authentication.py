from fastapi import Depends, FastAPI, Header, HTTPException
from Bridges.AuthenticationService import is_auth


def is_login(Id:str = Header(...), Token:str=Header(...)):
    result = is_auth(Id, Token)
    if result:
        return result
    else:
        raise HTTPException(status_code=403, detail="Login Required")


async def get_token_header(x_token: str = Header(...),x_id: str = Header(...)):
    if x_token != "fake-super-secret-token":
        raise HTTPException(status_code=400, detail="X-Token header invalid")
