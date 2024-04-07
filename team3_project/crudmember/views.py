from django.shortcuts import render, get_object_or_404
import json
from django.http import JsonResponse
from .models import *

'''
crudmember/urls.py 
    path('addUser/', views.addUser), #1. 회원 생성
    path('<int:pk>/', views.userInfo), #2. 회원 정보 조회
    path('changepwd/', views.changePwd), #회원 정보 수정
    path('delUser/<int:pk>/', views.delUser), #4. 회원 삭제
    path('userHeart/<int:pk>/', views.userHeart), #5. 하트 누르기
    path('rpsnt/', views.represent), #6. 대표로 임명하기, 대표 자격 박탈시키기
    path('allUser/', views.allUser),#7. 모든 회원들의 정보 조회 
'''
def addUser(request):
    if request.method == 'POST':
        data = json.loads(request.body)

        personal_key = data.get('personal_key')
        email = data.get('email')
        is_leader = data.get('is_leader')
        hearts = data.get('hearts')
        password = data.get('password')

        post = Post(
            personal_key = personal_key,
            email = email,
            is_leader = is_leader,
            hearts = hearts,
            password = password
        )
        post.save()
        return JsonResponse({'message':'success'})
    return JsonResponse({'message':'POST 요청만 허용됩니다.'})
	    

def userInfo(request, personal_key):
    if request.method == 'GET':
        post = get_object_or_404(Post, personal_key = personal_key)
        data = {
            'id' : post.personal_key,
            'email' : post.email,
            'is_leader' : post.is_leader,
            'hearts' : post.hearts
        }
    
        

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
