from django.db import models

# Create your models here.
class Axf_User(models.Model):

    u_username = models.CharField(max_length=30, verbose_name="用户名", unique=True, db_index=True)
    u_password = models.CharField(max_length=255, verbose_name="密码")
    u_email = models.EmailField(verbose_name="邮箱")

    def to_dict(self):
        return {
            'id': self.id,
            'u_username': self.u_username,
            'u_password': self.u_password,
            'u_email': self.u_email,
        }