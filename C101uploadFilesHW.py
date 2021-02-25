import dropbox

class TransferData:
    def __init__(self, tokenAccess):
        self.token = tokenAccess
    def upload(self, toFile, fromFile):
        dbx = dropbox.Dropbox(self.tokenAccess)
        f = open(fromFile,'rb')
        dbx.files_upload(f.read(),tokenAccess)

def main():
    tokenAccess = 'sl.Ar7fWneouAh5abL-6dzUiNHvhJhEdpv8J9Ff9N8_vc2_5JXs_e8FrG493rP0zxDd2VMangKY9TH_g_ouoj0leTLrWxWcAyf68cB95LMiulP-3hCecsP5Xerg37BzCy4IVCj-Ik8'
    transferData = TransferData(tokenAccess)
    fromFile = input("File to upload")
    toFile = input("Path to upload")
    transferData.upload(fromFile, toFile)
    print("File moved successfully")

main()