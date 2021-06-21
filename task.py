import cv2
import dropbox
import time
import random
starttime=time.time()

class TransferData:
    def __init__(self, access_token):
        self.access_token = access_token

    def upload_file(self, file_from, file_to):
        """upload a file to Dropbox using API v2
        """
        dbx = dropbox.Dropbox(self.access_token)

        with open(file_from, 'rb') as f:
            dbx.files_upload(f.read(), file_to)
    
def uploadfile():
    access_token="sl.Ay0vun7zcxRN386zxf8onDgow2eww3nzl3C3XW3g8GN9ASGk9bAA2_aX3aBGRq0mkYuWax6xFx_iULIW40LrgRZPvbSOG5oPXCaCz0JIMPK1WLw9MlqC1Bo9Dj4TqTtPAEyPY9x6IZY"
    transferData = TransferData(access_token)
    file_from = "test.txt"
    file_to="/testFolder/"
    dbx = dropbox.Dropbox(access_token)
    transferData.upload_file(file_from, file_to)
    with open(file_from, 'rb') as f: 
        dbx.files_upload(f.read(), file_to,mode=dropbox.files.WriteMode.overwrite) 
        print("file uploaded")
def main():
    while(True):
        if((time.time()-starttime)>=5000):
          
            uploadfile()
main()