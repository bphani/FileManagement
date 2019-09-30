from pydantic import BaseModel


class UploadFileResponse(BaseModel):
    UploadId: str
