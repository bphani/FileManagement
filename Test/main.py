import datetime
import re
import requests


b = str(datetime.datetime.now())

result = re.sub("[^0-9]",'_',b)
print(result)


def upload_file():
    a = requests.post("http://chichiapp.ir:3005/upload/data-form/",data={
        "PermissionLevel":"Public"

    },files={"file":open("./1.jpg",'rb')},headers={
        "Id":"5d87e194549ae0267b5268cc",
        "Token":"6109bfa925d615dc888c94d1ba858bad960f3dcb95a69453bd6dd1ba8acc4c49"
    }).content
    print(a)

def test():
    a = requests.post("http://chichiapp.ir:3005/ehsan/taghavi/fucking-test",data={"Taghavi":"amin"})
    print(a.content)


if __name__ == '__main__':
    test()