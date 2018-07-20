from django.db import models

# Create your models here.
class OrgInfo(models.Model):
    org_id=models.IntegerField(auto_created=True)
    org_name=models.CharField(max_length=20)
    org_parent_id=models.IntegerField()
    def __str__(self):
        return self.org_name


class UserInfo(models.Model):
    id=models.IntegerField(auto_created=True,primary_key=True)
    name=models.CharField(max_length=30)
    passwd=models.CharField(max_length=8)
    email=models.CharField(max_length=50)
    regDate=models.DateField()
    orgId=models.ForeignKey(OrgInfo,on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class ProjectInfo(models.Model):
    pro_name=models.CharField(max_length=50)
    pro_des=models.CharField(max_length=200)
    def __str__(self):
        return self.pro_name


