from django.db import models
from ckeditor.fields import RichTextField
from django.conf import settings


class Video(models.Model):
    title = models.CharField(max_length=200)
    url_path = models.TextField()
    scripts = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    recently_searched_date = models.DateTimeField(auto_now=True)
    # hits = models.PositiveIntergerField(default=0, verbose_name='검색횟수')


class Essay(models.Model):
    content = RichTextField(blank=True, null=True)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    video = models.ForeignKey(Video, on_delete=models.PROTECT)


class Studylog(models.Model):
    STUDY_PROGRESS = [
        ('RD', '공부 준비 중'),
        ('SC', '대본 공부 중'),
        ('WR', '에세이 쓰는 중'),
        ('SP', '말하기 연습 중'),
        ('DN', '공부 완료'),
        ('RV', '복습 중')
    ]
    # user 필드 필요함...
    video = models.ForeignKey(Video, on_delete=models.PROTECT)
    progress = models.CharField(max_length=2, choices=STUDY_PROGRESS)
    essay = models.ForeignKey(Essay, on_delete=models.PROTECT)
    # voca_list = ???
    started_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)