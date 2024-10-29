# from django.db import models
# import uuid
# # Create your models here.
# class Basemodel(models.Model):
#     uid=models.UUIDField(primary_key=True,editable=False,default=uuid.uuid4())
#     created_at=models.DateField(auto_created=True)
#     updated-at=models.DateField(auto_now=True)

#     class Meta:
#         abstract= True    



# class JOBSLISTING(models.Model):
#     job_title=models.CharField(max_length=100)
#     job_description=models.CharField(max_length=500)
#     job_area=models.CharField(max_length=100)
#     job_pincode=models.IntegerField(max_length=10)
from django.db import models
import uuid

# Create your models here.
class BaseModel(models.Model):
    uid = models.UUIDField(primary_key=True, editable=False, default=uuid.uuid4)  # Use the function without parentheses
    created_at = models.DateField(auto_now_add=True)  # Use auto_now_add for creation timestamp
    updated_at = models.DateField(auto_now=True)  # Correct the attribute name

    class Meta:
        abstract = True


class JOBSLISTING(BaseModel):  # Inherit from BaseModel
    job_title = models.CharField(max_length=100)
    job_description = models.CharField(max_length=500)
    job_area = models.CharField(max_length=100)
    job_pincode = models.PositiveIntegerField()  # Use PositiveIntegerField without max_length
