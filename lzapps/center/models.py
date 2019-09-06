from django.db import models
from datetime import datetime
from users.models import UserProfile


class CenterArticle(models.Model):
    title = models.CharField(max_length=100, blank=False, null=False, verbose_name=u'文章标题')
    leader = models.CharField(max_length=100, blank=True, null=True, default='', verbose_name=u'引题')
    author = models.CharField(max_length=20, blank=True, null=True, default='', verbose_name=u'作者')
    data_entry_staffer = models.CharField(max_length=20, blank=True, null=True, verbose_name=u'录入')
    editor = models.CharField(max_length=20, blank=True, null=True, verbose_name=u'编辑')
    facade_pic_url = models.ImageField(upload_to='media/articles/%Y/%M', max_length=100, blank=True, null=True,
                                       verbose_name=u'外挂图')
    article_pic = models.ImageField(upload_to='media/articles/%Y/%M', max_length=100, blank=True, null=True,
                                    verbose_name=u'文章内图')
    clicknum = models.IntegerField(default=0, verbose_name=u'点击数')
    managing_editor = models.CharField(max_length=20, blank=True, null=True, verbose_name=u'责任编辑')
    filelink = models.CharField(max_length=100, blank=True, null=True, verbose_name=u'文章地址')
    videolink = models.ImageField(upload_to='media/articles/%Y/%M', max_length=100, blank=True, null=True,
                                  verbose_name=u'视频链接')
    contentpart = models.CharField(max_length=252, blank=True, null=True, verbose_name=u'文章摘要')
    date_created = models.DateTimeField(default=datetime.now, verbose_name=u'创建时间')
    last_update = models.DateTimeField(default=datetime.now, verbose_name=u'更新时间')
    date_issued = models.DateTimeField(default=datetime.now, verbose_name=u'发布时间')
    hit = models.IntegerField(default=500, verbose_name=u'点击数')
    hothit = models.IntegerField(default=0, verbose_name=u'焦点图',
                                 choices=((0, '不是焦点图'), (1, '首页焦点图'), (2, '二级页面的焦点图'), (3, '三级页面的焦点图')))
    is_avail = models.BooleanField(default=False, verbose_name=u'是否发布')
    is_audited = models.BooleanField(default=False, verbose_name=u'是否审核')
    has_article_pic = models.BooleanField(default=False, verbose_name=u'是否包含图片')
    source = models.CharField(max_length=20, blank=True, null=True, verbose_name=u'文章来源', default=u'网络摘录')
    keyword = models.CharField(max_length=252, blank=True, null=True, verbose_name=u'关键字')
    reserve = models.CharField(max_length=252, blank=True, null=True, verbose_name=u'备注')
    temp_content = models.CharField(max_length=10, blank=True, null=True, verbose_name=u'文章内容')
    important_opt = models.BooleanField(default=False, verbose_name=u'是否突出显示')
    quick_response_code = models.BooleanField(default=False, verbose_name=u'返回码')
    program = models.ForeignKey('Program', models.DO_NOTHING, verbose_name=u'栏目')
    # owner = models.ForeignKey('UserProfile', models.DO_NOTHING, verbose_name=u'所有者')

    class Meta:
        verbose_name = u'文章'
        verbose_name_plural = verbose_name
        managed = False
        db_table = 'center_article'

    def __str__(self):
        return self.title


class Program(models.Model):
    program_title = models.CharField(max_length=20, verbose_name=u'栏目名称', default="", null=False, blank=False)
    program_desc = models.CharField(max_length=50, verbose_name=u'栏目描述', default="", null=True, blank=True)
    isleaf = models.BooleanField(default=True, verbose_name=u'是否为终节点')
    is_avail = models.BooleanField(default=True, verbose_name=u'是否可用')
    is_show = models.BooleanField(default=False, verbose_name=u'是否在前台页面显示')
    # is_next_channel = models.BooleanField(default=False,verbose_name=u'是否为子频道')
    domain_name = models.CharField(max_length=50, verbose_name=u'栏目类', default="", null=True, blank=True)
    date_created = models.DateTimeField(default=datetime.now, verbose_name=u'创建时间')
    skin = models.CharField(max_length=20, verbose_name=u'栏目SKIN', null=True, blank=True)
    sort_field = models.IntegerField(default=1, verbose_name=u'排序权重')
    frequency = models.IntegerField(default=1, verbose_name=u'使用频率')
    category = models.IntegerField(verbose_name=u'栏目类别', choices=((1, '省(直辖市)'), (2, '地市(区县)'), (3, '频道')), default=1)
    program_level = models.IntegerField(default=1, verbose_name=u'栏目级别')
    first_letter = models.CharField(max_length=6, verbose_name=u'栏目首字母', default="", null=True, blank=True)
    special_url = models.CharField(max_length=100, verbose_name=u'栏目外链接', default="", null=True, blank=True)
    program_pic_url = models.ImageField(upload_to="media/images/adv/", max_length=100, default="", null=True,
                                        blank=True)
    is_channel = models.BooleanField(default=False, verbose_name=u'是否为子频道')
    parent = models.ForeignKey('self', models.DO_NOTHING, default="", null=True, blank=True, verbose_name=u'父栏目')


    class Meta:
        verbose_name = u'栏目列表'
        verbose_name_plural = verbose_name
        managed = False
        db_table = 'center_program'

    def __str__(self):
        return self.program_title


class CenterHeadLine(models.Model):
    article: CenterArticle = models.ForeignKey(CenterArticle, models.DO_NOTHING, verbose_name=u'链接文章')
    operate_time = models.DateTimeField(default=datetime.now, verbose_name=u'创建时间')
    photo_url = models.ImageField(upload_to='media/headline/%Y/%M', max_length=100, blank=True, null=True)
    sign = models.BooleanField(default=True, verbose_name=u'是否显示')
    site = models.IntegerField()
    title = models.CharField(max_length=60, null=True, blank=True, verbose_name=u'头条标题')
    top_program_id = models.BigIntegerField(blank=True, null=True)

    class Meta:
        verbose_name=u'头条'
        verbose_name_plural=verbose_name
        managed = False
        db_table = 'center_head_line'

