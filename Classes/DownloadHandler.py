from DataBase.DB import files_collection
from bson.objectid import ObjectId
from starlette.responses import FileResponse
from Classes.FileActionTools import FileTools


class DownloadHandler:
    @staticmethod
    def download(file_id):
        file = files_collection.find_one({'_id': ObjectId(file_id)}, {"Name", "MimeType"})
        path = FileTools.save_file_path(file["Name"])
        return FileResponse(path, media_type=file['MimeType'])
