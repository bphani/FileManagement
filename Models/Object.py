from pydantic import BaseModel
from datetime import datetime


class Object(BaseModel):
    Name: str
    FileSize: int = 0
    Upload_at: datetime
    Update_at: datetime
    Status: str
    UploaderId: str
    DownloadCount: int = 0
    MimeType: str = None
    UploadMethod: str = None
    PermissionLevel: str = 'Public'
