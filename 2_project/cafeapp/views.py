from django.shortcuts import get_object_or_404, render, redirect
from .models import Blog, Subject
from django.utils import timezone
from .forms import BlogForm, BlogModelForm, CommentForm
from .tfidf_keyword import sortingimportance

def home(request):
    # 블로그 글들을 모조리 띄우는 코드
    # posts = Blog.objects.all()
    #posts = Subject.objects.filter().order_by('-subid')
    return render(request, 'index.html')#, {'posts':posts})
    #dict형태로 index.html에 post를 보내주는거

def detail(request):
    return render(request, 'portfolio-details.html')

def detail1(request):
    return render(request, 'portfolio-details1.html')

def detail2(request):
    return render(request, 'portfolio-details2.html')

def detail3(request):
    return render(request, 'portfolio-details3.html')

def detail4(request):
    return render(request, 'portfolio-details4.html')

def detail5(request):
    return render(request, 'portfolio-details5.html')

def detail6(request):
    return render(request, 'portfolio-details6.html')

def detail7(request):
    return render(request, 'portfolio-details7.html')

def detail8(request):
    return render(request, 'portfolio-details8.html')

def detail9(request):
    return render(request, 'portfolio-details9.html')

def subdetail(request):
    return render(request, 'subdetail.html')

# 블로그 글을 저장해주는 함수
def create(request):
    if(request.method == 'POST'):
        post = Blog()
        post.title = request.POST['title']
        post.save()
    return redirect('subdetail') #어떤 경로로 이동하게

#cities.views
from django.shortcuts import render
from django.views.generic import TemplateView, ListView
from django.db.models import Q
from .models import City
import pandas as pd
from django_pandas.io import read_frame
#from myapp.models import BlogPost
from django.shortcuts import HttpResponse


class HomePageView(TemplateView):
    template_name = 'home.html'

class SearchResultsView(ListView):
    model = Subject
    template_name = 'search_results.html'
    def get_queryset(self): # new
        query = self.request.GET.get('q')
        object_list = pd.DataFrame.from_records(Subject.objects.all().values_list('subid','semester', 'series_num', 'num','category','department',  'name', 'professor','credit','namecomma','namespaced','words','keywords_3','keywords_5','keywords_20'))
        #object_list=pd.DataFrame(list(Subject.objects.all().values('words')))
        #object_list=Subject.objects.all().values('words')
        ##object_list = pd.DataFrame(Subject.objects.filter(Q(words__icontains=query)))
        #object_list=Subject.objects.filter(Q(words__icontains=query)).values('words')
        #pdobject_list=pd.DataFrame(object_list)
        #pdlist_object_list=pd.DataFrame(list(object_list))
        #qs=Subject.objects.filter(Q(words__icontains=query))
        #object_list=read_frame(qs,fieldnames=['id','semester', 'series_num', 'num','category','department',  'name', 'professor','credit','words'])

        
        #object_list=sortingimportance(qs,query)
        #geeks_object = object_list.to_html()
        
        #numbers=object_list['series_num'][4:]
        #object_list=object_list.order_by(-numbers)
        return render(ListView, 'search_results.html', {'object_list':object_list})
        #return object_list #geeks_object#HttpResponse(geeks_object) #object_list #,df #,pdobject_list,pdlist_object_list

from django.shortcuts import HttpResponse



#상세페이지
def detail(request, subject_id):
    # blog_id 번째 블로그 글을 데이터베이스로부터 갖고와서
    blog_detail = get_object_or_404(Subject, pk=subject_id)
    # blog_id 번째 블로그 글을 detail.html로 띄워주는 코드 pk값을 이용해 특정모델 객체 하나만 갖고오기

    comment_form = CommentForm()

    return render(request, 'detail.html', {'blog_detail':blog_detail, 'comment_form':comment_form})
    #dict형태로 파일 보내주기

