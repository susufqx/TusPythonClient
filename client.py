from tusclient.client import TusClient
from uploader import MyUploader


class Client(TusClient):
    def __init__(self, url, headers=None):
        super().__init__(url, headers=headers)

    def uploader(self, *args, **kwargs):
        """
        Rewrite this function
        """
        kwargs['client'] = self
        return MyUploader(*args, **kwargs)
