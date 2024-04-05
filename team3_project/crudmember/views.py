from django.shortcuts import render
import json
from django.http import JsonResponse
from .models import *

'''
curdmember/urls.py 

    path('addUser/', views.addUser), #1. 회원 생성
    path('<int:pk>/', views.userInfo), #2. 회원 정보 조회
    path('changepwd/', views.changePwd), #회원 정보 수정
    path('delUser/<int:pk>/', views.delUser), #4. 회원 삭제
    path('userHeart/<int:pk>/', views.userHeart), #5. 하트 누르기
    path('rpsnt/', views.represent), #6. 대표로 임명하기, 대표 자격 박탈시키기
    path('allUser/', views.allUser),#7. 모든 회원들의 정보 조회 
'''
def addUser(request):
    return 0

def userInfo(request):
    return 0

def changePwd(request):
    return 0

def delUser(request):
    return 0

def userHeart(request):
    return 0

def represent(request):
    return 0

def allUser(request):
    return 0

# Create your views here.
