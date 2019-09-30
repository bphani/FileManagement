from datetime import datetime
from Models.Object import Object
from fastapi import File, UploadFile
import re
from DataBase.DB import files_collection
from Classes.FileActionTools import FileTools


class UploadHandler:
    @staticmethod
    def upload_file(file: UploadFile, file_extension, permission_level, uploader_id, file_size, category):
        # create safe and unique file name
        new_file_name = FileTools.file_name_generator(file_extension)
        # initialize file's model
        file_for_db = Object(Name=new_file_name, FileSize=int(file_size), FileExtension=file_extension,
                             PermissionLevel=permission_level, UploaderId=uploader_id,
                             Category=category, Status="Uploaded")
        # save file
        FileTools.save_file(file, new_file_name)

        # insert model to database
        item = files_collection.insert_one(file_for_db.__dict__)

        return {"Id": str(item.inserted_id)}
