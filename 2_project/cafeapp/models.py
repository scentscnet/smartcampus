from django.db import models

from django.utils.translation import gettext as _
from taggit.managers import TaggableManager
from taggit.models import Tag, TaggedItemBase

class Blog(models.Model):
    title = models.CharField(max_length=200)


    def __str__(self):
        return self.title

class Comment(models.Model):
    comment = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    post = models.ForeignKey(Blog, on_delete=models.CASCADE)

    def __str__(self):
        return self.comment

class City(models.Model):
    name = models.CharField(max_length=255)
    state = models.CharField(max_length=255)

    class Meta:
      verbose_name_plural = "cities"

    def __str__(self):
        return self.name

# Create your models here.


    
class Subject(models.Model):

    subid = models.IntegerField(primary_key=True,unique=True, blank=False)
    semester=models.CharField(_("semester"), blank=False,max_length=255)
    series_num=models.CharField(_("series_num"), blank=False,max_length=255)
    num=models.CharField(_("num"), blank=True,max_length=255) 
    category=models.CharField(_("category"),  blank=True, max_length=255) 
    department= models.CharField(_("department"),  blank=False, max_length=255) 
    name=models.CharField(_("name"), blank=False, max_length=255) 
    professor=models.CharField(_("professor"), blank=True, max_length=255) 
    credit=models.CharField(_("credit"), blank=True, max_length=255) 
    namecomma=models.CharField(_("namecomma"), blank=False, max_length=255) 
    namespaced=models.CharField(_("namespaced"), blank=False, max_length=255) 
    words= models.TextField(_("words"), blank=True)
    keywords_3=models.TextField(_("keywords_3"), blank=True)
    keywords_5=models.TextField(_("keywords_5"), blank=True)
    keywords_20=models.TextField(_("keywords_20"), blank=True)
    # semester=models.DateField(_("semester"), blank=False) 
    # tags=TaggableManager(_("tags"), blank=True)
    
    class Meta:
        # 모델 객체 리스트 출력할 때 어떻게 할 것인가 
        ordering=('subid',)

    def __str__(self):
        return self.series_num


class Kmooc(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(_("name"),  blank=False, max_length=255)
    midclassify=models.CharField(_("midclassify"), max_length=255)
    level= models.CharField(_("level"), max_length=255)
    image= models.URLField(_("image"))
    link= models.URLField(_("link")) 
    subject = models.ForeignKey(Subject, blank=True, related_name="sub_mooc", null=True, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

#class Sort(keyword):
#    a=len(keyword)
#    def __init__(self) -> None:
#        super().__init__()
#    def __str__(self):
#        return self.a
