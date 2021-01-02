from django.db import models

# Create your models here.
class user(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    dept = models.CharField(max_length=20)
    isadmin = models.BooleanField()
class interviewer(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    phone = models.CharField(max_length=15)
class apt(models.Model):
    id= models.IntegerField(primary_key=True)
    nameofparam=models.CharField(max_length=50)
    feedback=models.TextField()
class gd(models.Model):
    uid=models.ForeignKey('user',on_delete=models.CASCADE)
    param1=models.IntegerField()
    param2=models.IntegerField()
    param3=models.IntegerField()
    param4=models.IntegerField()
    param5=models.IntegerField()
    interviewer1=models.ForeignKey('interviewer',related_name='interviewer1', on_delete=models.CASCADE)
    interviewer2=models.ForeignKey('interviewer',related_name='interviewer2',on_delete=models.CASCADE)
    feedback=models.TextField()
class pi(models.Model):
    uid=models.ForeignKey('user',on_delete=models.CASCADE)
    param1=models.IntegerField()
    param2=models.IntegerField()
    param3=models.IntegerField()
    param4=models.IntegerField()
    param5=models.IntegerField()
    param6=models.IntegerField()
    param7=models.IntegerField()
    param8=models.IntegerField()
    interviewer1=models.ForeignKey('interviewer',related_name='interviewer3', on_delete=models.CASCADE)
    interviewer2=models.ForeignKey('interviewer',related_name='interviewer4',on_delete=models.CASCADE)
    feedback=models.TextField()
class resume(models.Model):
    uid=models.ForeignKey('user',on_delete=models.CASCADE)
    feedback=models.TextField()
class essay(models.Model):
    uid=models.ForeignKey('user',on_delete=models.CASCADE)
    feedback=models.TextField()
class pt(models.Model):
    uid=models.ForeignKey('user',on_delete=models.CASCADE)
    pt_type=models.CharField(max_length=15)
    e_score=models.IntegerField()
    n_score=models.IntegerField()
    f_score=models.IntegerField()
    j_score=models.IntegerField()
    