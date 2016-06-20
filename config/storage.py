# coding=utf-8
from django.core.files.storage import get_storage_class
from storages.backends.s3boto import S3BotoStorage


class CachedS3BotoStorage(S3BotoStorage):
    def __init__(self, *args, **kwargs):
        super(CachedS3BotoStorage, self).__init__(*args, **kwargs)
        StorageClass = get_storage_class('compressor.storage.CompressorFileStorage')
        self.local_storage = StorageClass()

    def save(self, name, content, max_length=None):
        self.local_storage._save(name, content, max_length)
        return super(CachedS3BotoStorage, self).save(name, self.local_storage._open(name), max_length)
