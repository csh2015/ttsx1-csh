from django.db import models

# Create your models here.

# 创建模型类UserInfo
class UserInfo(models.Model):
    uname = models.CharField(max_length=20)
    upwd = models.CharField(max_length=40)
    def __str__(self):
        return "%d" % self.pk