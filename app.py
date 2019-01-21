import sys
from client import Client
from tusclient.storage.filestorage import FileStorage
from tusclient.exceptions import TusUploadFailed


request_headers = {
    "Authorization": 'Basic xxyyZZAAbbCC=',
    "X-Client-Version": '1',
    "X-Country": '2',
    "X-Lang": '3',
    "X-Platform": '4',
    "X-FileType": '5'
}

url = 'http://0.0.0.0:1080/files/'
# url = 'http://www.susufqx.cn:1080/files/'


def run_main():
    fp = 'db/key_url.json'
    my_client = Client(
        url, headers=request_headers)

    if len(sys.argv) == 1:
        return

    file_path = sys.argv[1]  # file path to be inputted manualy
    file_all = file_path.split('/')[-1]
    n_t = file_all.split('.')
    file_name = n_t[0]
    file_type = n_t[1] if len(n_t) == 2 else ''
    # chunk_size = 20000

    file_storage = FileStorage(fp)
    try:
        my_uploader = my_client.uploader(file_path=file_path,
                                         # chunk_size=chunk_size,
                                         metadata={
                                             "fileName": file_name,
                                             "fileType": file_type
                                         },
                                         retry_delay=5,
                                         store_url=True,
                                         url_storage=file_storage)

    except Exception as e:
        print("[ERROR]", e)
        return

    my_uploader.upload()


run_main()
