from django.contrib import admin
from django.urls import path,include
from cafeapp import views
from cafeapp.views import HomePageView, SearchResultsView
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('detail/', views.detail, name='detail'),
    path('detail1/', views.detail1, name='detail1'),
    path('detail2/', views.detail2, name='detail2'),
    path('detail3/', views.detail3, name='detail3'),
    path('detail4/', views.detail4, name='detail4'),
    path('detail5/', views.detail5, name='detail5'),
    path('detail6/', views.detail6, name='detail6'),
    path('detail7/', views.detail7, name='detail7'),
    path('detail8/', views.detail8, name='detail8'),
    path('detail9/', views.detail9, name='detail9'),
    #path('/?', views.subdetail, name='subdetail'),
    path('create/', views.create, name='create'),
    #path('city/', include('cities.urls')),
    path('search/', SearchResultsView.as_view(), name='search_results'),
    #path('', HomePageView.as_view(), name='home'),
    path('detail/<int:subject_id>', views.detail, name='detail'), #id값도 같이 넘어가게 된다
    #path('1/',views.Table,name='table')
]

# media 파일에 접근할 수 있는 url도 추가해주어야 함    
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

