from pydantic import BaseModel


class UploadFileResponse(BaseModel):
    UploadId: str = "Uploaded File Id"
