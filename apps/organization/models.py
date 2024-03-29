from django.db import models
from datetime import datetime

from DjangoUeditor.models import UEditorField


# Create your models here.


# 城市信息
class CityDict(models.Model):
    name = models.CharField(max_length=20, verbose_name=u"城市")
    desc = models.CharField(max_length=200, verbose_name=u"描述")
    add_time = models.DateTimeField(default=datetime.now, verbose_name="添加时间")

    class Meta:
        verbose_name = u"城市"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


# 课程机构
class CourseOrg(models.Model):
    name = models.CharField(max_length=50, verbose_name=u"机构名称")
    desc = UEditorField(verbose_name=u'机构描述', width=600, height=300, imagePath="org/ueditor/", filePath="org/ueditor/",
                        default='')
    tag = models.CharField(max_length=5, verbose_name=u'机构标签', default='全国知名')
    category = models.CharField(default=u"gx", max_length=20, verbose_name=u"机构类别",
                                choices=(('pxjg', u'培训结构'), ('gr', u'个人'), ('gx', u'高校')))
    click_nums = models.IntegerField(default=0, verbose_name=u"点击数")
    fav_nums = models.IntegerField(default=0, verbose_name=u"收藏数")
    image = models.ImageField(upload_to="org/%Y/%m", verbose_name=u"logo", max_length=100)
    address = models.CharField(max_length=150, verbose_name=u"机构地址")
    city = models.ForeignKey(CityDict, verbose_name=u"所在城市", on_delete=models.CASCADE)
    students = models.IntegerField(default=0, verbose_name=u"学习人数")
    course_nums = models.IntegerField(default=0, verbose_name=u"课程数")
    add_time = models.DateTimeField(default=datetime.now, verbose_name=u'添加时间')

    class Meta:
        verbose_name = u"课程机构"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name

    def get_teacher_nums(self):
        # 获取课程机构的讲师数量
        return self.teacher_set.all().count()

    def get_course_nums(self):
        # 获取课程数
        return self.course_set.all().count()

    def get_org_course(self):
        # 经典课程
        return self.course_set.all().order_by("-students")[:3]


# 讲师信息
class Teacher(models.Model):
    org = models.ForeignKey(CourseOrg, verbose_name=u"所属机构", on_delete=models.CASCADE)
    name = models.CharField(max_length=50, verbose_name=u"教师名称")
    work_years = models.IntegerField(default=0, verbose_name=u"工作年限")
    work_company = models.CharField(max_length=50, verbose_name=u"就职公司")
    work_position = models.CharField(max_length=50, verbose_name=u"公司职位")
    points = models.CharField(max_length=50, verbose_name=u"教学特点")
    click_nums = models.IntegerField(default=0, verbose_name=u"点击数")
    fav_nums = models.IntegerField(default=0, verbose_name=u"收藏数")
    age = models.IntegerField(default=18, verbose_name=u"年龄")
    image = models.ImageField(default='', upload_to="teacher/%Y/%m", verbose_name=u"头像", max_length=100)
    add_time = models.DateTimeField(default=datetime.now, verbose_name=u'添加时间')

    class Meta:
        verbose_name = u"教师"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name

    def get_course_nums(self):
        return self.course_set.all().count()
