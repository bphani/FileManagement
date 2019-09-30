from fastapi import APIRouter
from Classes.DownloadHandler import DownloadHandler

download_route = APIRouter()


@download_route.get("/download/{file_id}", tags=["DOWNLOAD"])
def download_file(file_id):
    return DownloadHandler.download(file_id)
