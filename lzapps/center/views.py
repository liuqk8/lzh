from django.shortcuts import render

# Create your views here.
from django.views.generic.base import View
from django.db.models import Q

from adv.models import Advment
from center.models import CenterArticle,CenterHeadLine


class IndexView(View):
    def get(self,request):
        lasts=CenterArticle.objects.all().order_by("-date_issued")[:9]
        adv1=Advment.objects.filter(Q(ad_category='402881b74428f729014429241fc30000')&Q(sign=True)).order_by('local_on_page')
        headLines=CenterHeadLine.objects.filter(sign=True).order_by('-operate_time')[:5]

        return render(request, 'lzh/index.html',{"lasts":lasts,'adv1':adv1,'headLines':headLines})

class DetailView(View):
    def get(self, request, article_id):
        article = CenterArticle.objects.get(id=int(article_id))
        article.clicknum += 1
        article.save()
        return render(request,'lzh/detail.html',{'article':article})

