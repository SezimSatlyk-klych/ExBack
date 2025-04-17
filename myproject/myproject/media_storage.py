from storages.backends.s3boto3 import S3Boto3Storage

class MediaStorage(S3Boto3Storage):
    bucket_name = 'media'
    default_acl = None
    file_overwrite = False
    custom_domain = None
    
    def url (self, name):
        return f"http://localhost:9000/media/{name}" 