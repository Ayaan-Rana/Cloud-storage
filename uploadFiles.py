import dropbox

class TransferData:
    def __init__(self,access_token):
        self.access_token=access_token

    def upload_file(self, fileFrom, fileTo):
        dbx= dropbox.Dropbox(self.access_token)