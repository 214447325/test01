from django.db import models

# Create your models here.
class User(models.Model):
    # 姓名
    name = models.CharField(max_length=20)
    # 地址
    address = models.CharField(max_length=100)
    # 生日
    birthday = models.DateField()

    def getSelectAll(self):
        list = {}
        list['id'] = self.id
        list['name'] = self.name
        list['address'] = self.address
        list['birthday'] = str(self.birthday)
        return list