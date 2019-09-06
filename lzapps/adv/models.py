from django.db import models
from datetime import datetime


# Create your models here.
class AdCategory(models.Model):
    id = models.CharField(primary_key=True, max_length=36)
    name = models.CharField(max_length=40, null=True, blank=True, verbose_name=u'广告位')
    ad_type = models.CharField(max_length=10, verbose_name=u'广告类型', default='static', blank=True, null=True,
                               choices=(('static', '静态'), ('flow', '滚动'), ('flash', '焦点图')))
    local_div = models.CharField(max_length=20, null=True, blank=True, verbose_name=u'位置')  # 位置
    widthorspeed = models.CharField(max_length=5, null=True, blank=True,
                                    verbose_name=u'宽度/速度')  # 若类型为flash此值代表宽，若为flow此值代表滚动速度
    heightorvisiable = models.CharField(max_length=5, null=True, blank=True,
                                        verbose_name=u'高度/条数')  # 若类型为flash此值代表高，若为flow此值代表条数
    direction = models.CharField(max_length=5, null=True, blank=True, verbose_name=u'方向')  # 代表flow类型的滚动方向上下还是左右

    class Meta:
        verbose_name = u'广告位'
        verbose_name_plural = verbose_name
        managed = False
        db_table = 'center_ad_category'

    def __str__(self):
        return self.name


class Advment(models.Model):
    id = models.CharField(primary_key=True, max_length=36)
    link_name = models.CharField(max_length=50, null=True, blank=True, verbose_name=u'广告名称')
    photo_url = models.ImageField(upload_to='media/adv/%Y/%M', max_length=100, null=True, blank=True,
                                  verbose_name=u'图片')
    link_url = models.CharField(max_length=100, null=True, blank=True, verbose_name=u'外连接')
    operate_time = models.DateTimeField(default=datetime.now, verbose_name=u'添加时间')
    sign = models.BooleanField(default=True, verbose_name=u'是否启用')  # 是否启用
    local_on_page = models.IntegerField(default=1, verbose_name=u'显示顺序')
    ad_category = models.ForeignKey('AdCategory', models.DO_NOTHING, verbose_name=AdCategory.name)

    class Meta:
        verbose_name = u'广告'
        verbose_name_plural = verbose_name
        managed = False
        db_table = 'center_advertisment'

    def __str__(self):
        return self.link_name
