from django.db import models

# Create your models here.
class OrgInfo(models.Model):
    orgId=models.IntegerField(auto_created=True)
    orgName=models.CharField(max_length=20)
    orgParentId=models.IntegerField()
    def __str__(self):
        return self.orgName


class UserInfo(models.Model):
    id=models.IntegerField(auto_created=True,primary_key=True)
    name=models.CharField(max_length=30)
    passwd=models.CharField(max_length=8)
    email=models.CharField(max_length=50)
    regDate=models.DateField()
    def __str__(self):
        return self.name


class ProjectInfo(models.Model):
    id = models.IntegerField(auto_created=True, primary_key=True)
    proName=models.CharField(max_length=50)
    proDesc=models.CharField(max_length=200)
    def __str__(self):
        return self.proName


class resultInfo(models.Model):
    id = models.IntegerField(auto_created=True, primary_key=True)
    desc=models.CharField(max_length=50)
    res = models.CharField(max_length=50)
    retCode = models.CharField(max_length=50)
    name = models.CharField(max_length=50)
    url = models.CharField(max_length=50)
    retContent = models.CharField(max_length=10000)
    def __str__(self):
        return self.desc


class resultMapInfo(models.Model):
    id=models.IntegerField(auto_created=True, primary_key=True)
    orgId = models.ForeignKey(OrgInfo, on_delete=models.CASCADE)
    proId = models.ForeignKey(ProjectInfo, on_delete=models.CASCADE)
    userId = models.ForeignKey(UserInfo, on_delete=models.CASCADE)
    resultId=models.ForeignKey(resultInfo, on_delete=models.CASCADE)
    def __str__(self):
        return str(self.id)


class UserOrgMapInfo(models.Model):
    id=models.IntegerField(auto_created=True, primary_key=True)
    userId=models.ForeignKey(UserInfo, on_delete=models.CASCADE)
    orgId=models.ForeignKey(OrgInfo, on_delete=models.CASCADE)
    def __str__(self):
        return str(self.id)

