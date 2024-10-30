from django.db import models
import uuid

# BaseModel as defined previously
class BaseModel(models.Model):
    uid = models.UUIDField(primary_key=True, editable=False, default=uuid.uuid4)
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)

    class Meta:
        abstract = True


class JOBSLISTING(BaseModel):  # Inherit from BaseModel
    job_title = models.CharField(max_length=100)
    job_description = models.CharField(max_length=500)
    job_area = models.CharField(max_length=100)
    job_pincode = models.PositiveIntegerField()
    job_image = models.ImageField(upload_to='job_images/', null=True, blank=True)  # Field to handle image upload
