from django.db import models
from django import forms


# Create your models here.


# 用户模型类
class User(models.Model,forms.Form):
    SEX = (
        ('M', '男'),
        ('F', '女'),
        ('U', '保密'),
    )

    # 姓名
    userName = models.CharField(max_length=20)
    # 性别（男，女，-）
    userSex = models.CharField(max_length=8, choices=SEX)
    # 职务
    userJob = models.CharField(max_length=20)
    # 机构名称
    mechanismName = models.CharField(max_length=50)
    # 机构资质或授权文件（上传文件不能大于5M）
    mechanismQuali = models.ImageField(max_length=5096)
    # 微信号
    wcID = models.IntegerField()
    # 微信二维码图片（图片上传只支持png或者jpg格式，图片命名：项目根目录/wechat/wc2d用户ID用户姓名.图片后缀名）
    wcImage = models.ImageField(max_length=5096)
    # 手机号码
    userPhone = models.IntegerField()
    # 电子邮箱
    userEmail = models.CharField()
    # 所在地区（省市区三级下拉列表）
    userAddress = forms.ChoiceField(label=u'队列')
    # 隐私设置（联系方式是否公开）
    privacySettings = models.BooleanField(default=False)
    # 注册时间
    # 审和状态（未审核，未通过，通过）
    # 审核意见
    # 所属联蒙群
