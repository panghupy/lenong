from django.db import models


# Create your models here.
class UserInfo(models.Model):
    uname = models.CharField(verbose_name='用户名', max_length=30,unique=True)
    upassword = models.CharField(verbose_name='密码', max_length=50)
    uemail = models.EmailField(verbose_name='邮箱')
    ureceive = models.CharField(verbose_name='收件人', max_length=50, default='')
    uaddress = models.CharField(verbose_name='地址', max_length=100, default='')
    uzip_code = models.CharField(verbose_name='邮编', max_length=30, default='')
    uphone = models.CharField(verbose_name='手机号', max_length=11, default='')

    class Meta:
        verbose_name = '用户'
        verbose_name_plural = verbose_name
