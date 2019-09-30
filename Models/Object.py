from pydantic import BaseModel
from datetime import datetime


class Object(BaseModel):
    Name: str
    FileSize: int = 0
    Upload_at: datetime = datetime.now()
    Update_at: datetime = datetime.now()
    Status: str
    UploaderId: str
    DownloadCount: int = 0
    MimeType: str = None
    UploadMethod: str = None
    PermissionLevel: str = 'Public'
    Category: str = "Default"
    FileExtension: str = None
