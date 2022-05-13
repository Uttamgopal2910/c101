import dropbox
class TransferData:
    def __init__(self,access_token):
        self.access_token = access_token
    def upload_file(self, file_from, file_to):
        dbx=dropbox.Dropbox(self.access_token)

        f=open(file_from,"rb")
        dbx.files_upload(f.read(),file_to)

def main():
    access_token='sl.BHiMhKAbf8MbPDt_DER9_efLHVpPWGPUydmnvt4ymBvXxKhMkKfUERpH_LoFz72ErbvhTVR15kW2Fhq3ibEw--YJo2Vd6fYZtN0xTDGLntzpgu2palauLkD9dbXv3Wk1fTLcGwo'
    transferData=TransferData(access_token)

    file_from=input("enterthefilepathtotransfer:-")
    file_to=input("enterthefullpathtouploadthedropbox:-")

    transferData.upload_file(file_from,file_to)
    print("filehasbeenmoved")

main()
        