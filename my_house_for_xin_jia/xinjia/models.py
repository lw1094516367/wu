from django.db import models
from django import forms


class RegisterForm(forms.Form):
    gender = (
        ('male', "男"),
        ('female', "女"),
    )
    username = forms.CharField(label="用户名", max_length=128, widget=forms.TextInput(attrs={'class': 'form-control'}))
    password1 = forms.CharField(label="密码", max_length=256, widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    password2 = forms.CharField(label="确认密码", max_length=256, widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    email = forms.EmailField(label="邮箱地址", widget=forms.EmailInput(attrs={'class': 'form-control'}))
    sex = forms.ChoiceField(label='性别', choices=gender)


class ShowInfo(models.Model):
    id = models.IntegerField(primary_key=True)
    title = models.CharField(max_length=255)
    imageurls = models.CharField(db_column='imageUrls', max_length=1000)  # Field name made lowercase.
    publishtime = models.CharField(db_column='publishTime', max_length=255)  # Field name made lowercase.
    address = models.CharField(max_length=255)
    phone = models.CharField(max_length=255)

    # 定义默认输出格式
    def __str__(self):
        return "%s:%s:%s:%s:%s:%s" % (self.id, self.title, self.imageurls, self.publishtime, self.address, self.phone)

    class Meta:
        managed = False
        db_table = 'show_info'
        verbose_name = '浏览房产信息'
        verbose_name_plural = '房产信息管理'


class User(models.Model):
    id = models.IntegerField(primary_key=True)
    username = models.CharField(db_column='UserName', max_length=255)  # Field name made lowercase.
    phone = models.CharField(db_column='Phone', max_length=255)  # Field name made lowercase.
    sex = models.IntegerField()
    authortriy = models.IntegerField(db_column='Authortriy')  # Field name made lowercase.
    passWord = models.CharField(db_column='passWord', max_length=255)  # Field name made lowercase.
    createtime = models.CharField(db_column='createTime', max_length=255)  # Field name made lowercase.

    # 定义默认输出格式
    def __str__(self):
        return "%s:%s:%s:%s:%s:%s:%s" % (self.id, self.username, self.phone, self.sex, self.authortriy,
                                      self.passWord, self.createtime)

    class Meta:
        managed = False
        db_table = 'user'
        verbose_name = '浏览用户信息'
        verbose_name_plural = '用户信息管理'

