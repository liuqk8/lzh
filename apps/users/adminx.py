# -*- coding:utf-8 -*-
__date__ = '2019/2/25 0025 16:05'
__author__ = 'liuqikui'

import xadmin
from xadmin import views
from xadmin.plugins.auth import UserAdmin
from .models import EmailVerifyRecord, Banner, UserProfile



# 基础配置
class BaseSetting(object):
    # 主题功能
    enable_themes = True
    use_bootswatch = True


class GlobalSettings(object):
    site_title = u"后台管理系统"
    site_footer = u"廉政中国网"
    # 收缩app
    menu_style = "accordion"


class UserProfileAdmin(UserAdmin):
    list_display = ('username', 'nick_name', 'email', 'gender', 'birday')


class EmailVerifyRecordAdmin(object):
    pass


class BannerAdmin(object):
    pass


xadmin.site.unregister(UserProfile)
# xadmin.site.register(EmailVerifyRecord, EmailVerifyRecordAdmin)
# xadmin.site.register(Banner, BannerAdmin)
xadmin.site.register(UserProfile, UserProfileAdmin)
# 主题注册
xadmin.site.register(views.BaseAdminView, BaseSetting)
# 界面部分设置
xadmin.site.register(views.CommAdminView, GlobalSettings)
