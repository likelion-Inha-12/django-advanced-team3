from django.db import models

class Post(models.Model):
    personal_key = models.IntegerField() # id(pk)
    name = models.CharField(max_length=10) # 사람 이름, 최대 길이 10글자
    email = models.CharField(max_length=100) # 100글자가 최대인 문자열
    is_leader = models.BooleanField() # 대표 여부
    hearts = models.IntegerField() # 하트 수
    password = models.CharField(max_length=100) # 비밀번호