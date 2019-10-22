from fastapi import APIRouter, File, UploadFile, Form, Header, Depends
from Classes.UploadHandler import UploadHandler
from Models.ResponseModels import UploadFileResponse
from Authentications.Authentication import is_login, get_token_header
from starlette.requests import Request

upload_route = APIRouter()


# todo : adding upload properties
# todo : check user permission for uploading form server

@upload_route.post('/upload/data-form/', dependencies=[Depends(is_login)],
                   tags=["UPLOAD"],
                   response_model=UploadFileResponse)
async def upload_file_form_data(request: Request, file: UploadFile = File(...), PermissionLevel: str = Form(...)):
    return UploadHandler.upload_file(file, file.filename, PermissionLevel, request.headers["Id"], 0, "ProductImage")
