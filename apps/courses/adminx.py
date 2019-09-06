# -*- coding:utf-8 -*-
__date__ = '2019/2/25 0025 16:56'
__author__ = 'liuqikui'

import xadmin
from .models import Course, CourseResource, Teacher, Lesson, Video


class CourseAdmin(object):
    pass


class CourseResourceAdmin(object):
    pass


class TeacherAdmin(object):
    pass


class LessonAdmin(object):
    pass


class VideoAdmin(object):
    pass


# xadmin.site.register(Course, CourseAdmin)
# xadmin.site.register(CourseResource, CourseResourceAdmin)
# xadmin.site.register(Teacher, TeacherAdmin)
# xadmin.site.register(Lesson, LessonAdmin)
# xadmin.site.register(Video, VideoAdmin)
