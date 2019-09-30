from DataBase.DB import files_collection
from bson.objectid import ObjectId
from starlette.responses import FileResponse
from Classes.FileActionTools import FileTools
from Classes.Tools import Tools


class DownloadHandler:
    @staticmethod
    def download(file_id):
        try:
            file = files_collection.find_one({'_id': ObjectId(file_id)}, {"Name", "MimeType"})
            path = FileTools.save_file_path(file["Name"])
            return FileResponse(path, media_type=file['MimeType'])
        except Exception as ex:
            return Tools.Result(False,ex.args)
