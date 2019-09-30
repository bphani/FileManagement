from datetime import datetime
from Models.Object import Object
from fastapi import UploadFile
import re
import json

with open('./Configs/Configs.json') as f:
    configs = json.load(f)
file_dirs = configs["UploadFolderLocation"]


class FileTools:

    @staticmethod
    def file_name_generator(file_extension):
        # mime-type
        file_extension = str(file_extension).split('/')[1]
        new_file_name = str(datetime.now())
        result = re.sub("[^0-9]", '_', new_file_name)
        return f"{result}.{file_extension}"

    @staticmethod
    def save_file_path(file_name):
        return f"{file_dirs}/{file_name}"

    @staticmethod
    def save_file(file_value: UploadFile, file_name):
        path = FileTools.save_file_path(file_name)
        file = open(path, 'wb')
        contents = file_value.file.read()
        file.write(contents)
        file.close()
