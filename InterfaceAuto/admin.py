from django.contrib import admin
from .models import UserInfo,OrgInfo,ProjectInfo,resultInfo,resultMapInfo,UserOrgMapInfo
# Register your models here.
class UserInfoAdmin(admin.ModelAdmin):
    list_display = ('id','name','passwd','email','regDate',)
class OrgInfoAdmin(admin.ModelAdmin):
    list_display = ('orgId','orgName','orgParentId',)
class ProjectInfoAdmin(admin.ModelAdmin):
    list_display = ('id','proName','proDesc',)
class resutlInfoAdmin(admin.ModelAdmin):
    list_display = ('id','desc','res','retCode','name','url','retContent',)
class resultMapInfoAdmin(admin.ModelAdmin):
    list_display = ('id','orgId','proId','userId','resultId',)
class UserOrgMapInfoAdmin(admin.ModelAdmin):
    list_display = ('id','orgId','userId',)

admin.site.register(UserInfo,UserInfoAdmin)
admin.site.register(OrgInfo,OrgInfoAdmin)
admin.site.register(ProjectInfo,ProjectInfoAdmin)
admin.site.register(resultInfo,resutlInfoAdmin)
admin.site.register(resultMapInfo,resultMapInfoAdmin)
admin.site.register(UserOrgMapInfo,UserOrgMapInfoAdmin)

