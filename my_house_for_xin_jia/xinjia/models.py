from django.db import models


class ShowInfo(models.Model):
    title = models.CharField(max_length=255)
    imageurls = models.CharField(db_column='imageUrls', max_length=1000)  # Field name made lowercase.
    publishtime = models.CharField(db_column='publishTime', max_length=255)  # Field name made lowercase.
    address = models.CharField(max_length=255)
    phone = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'show_info'


class User(models.Model):
    username = models.CharField(db_column='UserName', max_length=255)  # Field name made lowercase.
    phone = models.CharField(db_column='Phone', max_length=255)  # Field name made lowercase.
    sex = models.IntegerField()
    authortriy = models.IntegerField(db_column='Authortriy')  # Field name made lowercase.
    idcard = models.CharField(db_column='idCard', max_length=255)  # Field name made lowercase.
    createtime = models.CharField(db_column='createTime', max_length=255)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'user'

