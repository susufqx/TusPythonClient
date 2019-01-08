import time
from tusclient.uploader import Uploader
from tusclient.exceptions import TusCommunicationError


class MyUploader(Uploader):
    def __init__(self, file_path=None, file_stream=None, url=None, client=None,
                 chunk_size=None, metadata=None, retries=0, retry_delay=30,
                 store_url=False, url_storage=None, fingerprinter=None, log_func=None):
        super().__init__(file_path=file_path, file_stream=file_stream, url=url, client=client,
                         chunk_size=chunk_size, metadata=metadata, retries=retries, retry_delay=retry_delay,
                         store_url=store_url, url_storage=url_storage, fingerprinter=fingerprinter, log_func=log_func)

    def _retry_or_cry(self, error):
        time.sleep(self.retry_delay)
        try:
            self.offset = self.get_offset()
        except TusCommunicationError as e:
            print("[ERROR]: ", error)
            self._retry_or_cry(e)
        else:
            self._do_request()
