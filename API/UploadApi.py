from fastapi import APIRouter, File, UploadFile ,Form, Header
from Classes.UploadHandler import UploadHandler
from Models.ResponseModels import UploadFileResponse

upload_route = APIRouter()
# todo : adding upload properties
# todo : check user permission for uploading form server

@upload_route.post('/upload/data-form/', tags=["UPLOAD"],response_model=UploadFileResponse)
async def upload_file_form_data(file: UploadFile = File(...)
                                ,PermissionLevel: str = Form(...),
                                Id: str = Header(None),
                                Token: str = Header(None)):
    return UploadHandler.upload_file(file,file.content_type,PermissionLevel,Id,0,"ProductImage")
