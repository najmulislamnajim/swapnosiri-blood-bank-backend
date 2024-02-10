from django.db import models

# Create your models here.
BLOOD_GROUP=[
    ('a+','a+'),
    ('a-','a-'),
    ('b+','b+'),
    ('b-','b-'),
    ('ab+','ab+'),
    ('ab-','ab-'),
    ('o+','o+'),
    ('o-','o-'),
]
class DonorModel(models.Model):
    name=models.CharField(max_length=50)
    email=models.CharField(max_length=50,unique=True)
    phone=models.CharField(max_length=20)
    image=models.ImageField(upload_to='donor/media/images/')
    blood_group=models.CharField(choices=BLOOD_GROUP,max_length=10)
    last_donate_date=models.DateField()
    
    def __str__(self):
        return f'{self.name}'
    
class DonationRequestModel(models.Model):
    donor=models.ForeignKey(DonorModel,on_delete=models.CASCADE)
    name=models.CharField(max_length=50)
    email=models.CharField(max_length=50,unique=True)
    phone=models.CharField(max_length=20)
    disease=models.TextField()
    location=models.CharField(max_length=50)
    