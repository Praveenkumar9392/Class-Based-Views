# import boto3
# from django.conf import settings
# from io import BytesIO

# class AmazonS3:
#     def __init__(self, bucket_name):
#         self.client = boto3.client('s3', region_name=settings.AWS_S3_REGION_NAME, aws_access_key_id=settings.AWS_ACCESS_KEY_ID, aws_secret_access_key=settings.AWS_SECRET_ACCESS_KEY)
#         self.bucket_name = bucket_name

#     def upload_file(self, file_content, object_name, content_type=None):
#         extra_args = {'ContentType': content_type} if content_type else {}
#         self.client.upload_fileobj(BytesIO(file_content), self.bucket_name, object_name, ExtraArgs=extra_args)

#     def download_file(self,object_name, file_name):
#         self.client.download_file(self.bucket_name, object_name, file_name)

#     def create_bucket(self):
#         self.client.create_bucket(Bucket=self.bucket_name)    
        
#     def list_objects(self):
#         response = self.client.list_objects(Bucket=self.bucket_name)
#         return response.get('Contents', [])    

#     def delete_object(self, object_name):
#         self.client.delete_object(Bucket=self.bucket_name, Key=object_name)

#     def get_object_metadata(self, object_name):
#         response = self.client.head_object(Bucket=self.bucket_name, Key=object_name)
#         return response

#     def generate_presigned_url(self, object_name, expiration=3600):
#         url = self.client.generate_presigned_url(
#             'get_object',
#             Params={'Bucket': self.bucket_name, 'Key': object_name},
#             ExpiresIn=expiration
#         )
#         return url

#     def generate_presigned_url_post(self, object_name, fields=None, conditions=None, expiration=3600):
#         url = self.client.generate_presigned_post(
#             self.bucket_name,
#             object_name,
#             Fields=fields,
#             Conditions=conditions,
#             ExpiresIn=expiration
#         )
#         return url
    
#     def create_folder(self, folder_name):
#         object_name = f"{folder_name}/"
#         self.client.put_object(Bucket=self.bucket_name, Key=object_name)
        
#     def delete_folder_if_empty(self, folder_name):
#         objects = self.list_objects()
#         folder_objects = [obj['Key'] for obj in objects if obj['Key'].startswith(folder_name)]

#         visible_objects = [obj for obj in folder_objects if not obj.endswith('/')]
        
#         if not visible_objects:
#             for obj in folder_objects:
#                 self.client.delete_object(Bucket=self.bucket_name, Key=obj)
#             return 'empty'
#         else:
#             return 'not_empty'

#     def search_files_with_name(self, file_name):
#         objects = self.list_objects()
#         matching_files = [obj for obj in objects if file_name.lower() in obj['Key'].lower()]
#         return matching_files
    
#     def folder_exists(self, folder_name):
#         response = self.client.list_objects(Bucket=self.bucket_name, Prefix=folder_name)
#         return 'Contents' in response
    
#     def move_to_trash(self, object_name, trash_folder='trash'):
#         trash_object_name = f"{trash_folder}/{object_name}"

#         self.client.copy_object(
#             Bucket=self.bucket_name,
#             CopySource={'Bucket': self.bucket_name, 'Key': object_name},
#             Key=trash_object_name)

#         self.client.delete_object(Bucket=self.bucket_name, Key=object_name)

# class AmazonS3New:
#     def __init__(self):
#         self.client = boto3.client('s3', region_name=settings.AWS_S3_REGION_NAME, aws_access_key_id=settings.AWS_ACCESS_KEY_ID, aws_secret_access_key=settings.AWS_SECRET_ACCESS_KEY)

#     def create_bucket(self,bucket_name):
#         self.client.create_bucket(Bucket=bucket_name,CreateBucketConfiguration={'LocationConstraint': settings.AWS_S3_REGION_NAME})
        