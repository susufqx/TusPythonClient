import sys
from client import Client
from tusclient.storage.filestorage import FileStorage
from tusclient.exceptions import TusUploadFailed


def run_main():
    fp = 'db/key_url.json'
    my_client = Client(
        'http://0.0.0.0:1080/files/', headers={'Authorization': 'Basic xxyyZZAAbbCC='})

    if len(sys.argv) == 1:
        return

    file_path = sys.argv[1]  # file path to be inputted manualy
    file_all = file_path.split('/')[-1]
    n_t = file_all.split('.')
    file_name = n_t[0]
    file_type = n_t[1] if len(n_t) == 2 else ''
    chunk_size = 100000

    file_storage = FileStorage(fp)
    my_uploader = my_client.uploader(file_path=file_path,
                                     chunk_size=chunk_size,
                                     metadata={
                                         "fileName": file_name,
                                         "fileType": file_type
                                     },
                                     retry_delay=5,
                                     store_url=True,
                                     url_storage=file_storage)

    my_uploader.upload()
    if my_uploader.verify_upload():
        print("FILE HAS BEEN UPLOADED SUCCESSFULLY!")


run_main()

# Here we need to change Uploader._retry_or_cry func
'''
def go():
    try:
        run_main()
    except TusUploadFailed as e:
        go()


go()
'''
