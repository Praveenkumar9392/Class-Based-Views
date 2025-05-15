from django.db import models
from django.core.files.storage import default_storage
from simple_history.models import HistoricalRecords
from masters.models import BaseModel

class MediaFolder(BaseModel):
    name = models.CharField(max_length=255)
    parent_folder = models.ForeignKey('self', null=True, blank=True, related_name='subfolders', on_delete=models.SET_NULL)
    
    history = HistoricalRecords(inherit=True)

    def __str__(self):
        return self.name

    def get_s3_folder_path(self):
        folder_path = self.name
        current_folder = self.parent_folder
        while current_folder:
            folder_path = f"{current_folder.name}/{folder_path}"
            current_folder = current_folder.parent_folder
        return folder_path

class MediaItem(BaseModel):
    name = models.CharField(max_length=200, null=True, blank=True)
    folder = models.ForeignKey(MediaFolder, null=True, blank=True, related_name='media_items', on_delete=models.SET_NULL)
    history = HistoricalRecords(inherit=True)
    
    def get_image_upload_path(instance, filename):
        if instance.folder:
            folder_path = instance.folder.get_s3_folder_path()
            return f"{folder_path}/{filename}"
        else:
            return filename

    image = models.ImageField(upload_to=get_image_upload_path)
    is_trash = models.BooleanField(default=False)
    

    def save(self, *args, **kwargs):
        if not self.name and self.image:  
            self.name = self.image.name
        super(MediaItem, self).save(*args, **kwargs)

    # def __str__(self):
    #     return "{}".format(self.image.url)
    def __str__(self):
        if self.image:
            return "{}".format(self.image.url)
        else:
            return "No image associated with this MediaItem"
