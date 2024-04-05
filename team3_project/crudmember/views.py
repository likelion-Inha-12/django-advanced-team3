from django.shortcuts import render
import json
from django.http import JsonResponse
from django.shortcuts import get_object_or_404
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
    return 0

def userInfo(request):
    return 0

def changePwd(request, pk):

    if request.method == 'POST':
        data = json.loads(request.body)
        new_pwd = data.get('new_password', None)
    
    if new_pwd:
        post = get_object_or_404(Post, personal_key=pk)
        post.password = new_pwd
        post.save()

        return JsonResponse({'message' : f'비밀번호가 변경되었습니다. 새로운 비밀번호는 {new_pwd}입니다.'})
    else:
        return JsonResponse({'message':'비밀번호 변경이 실패하였습니다.'})
        

def delUser(request):
    return 0

def userHeart(request, pk):
    
    if request.method == 'POST':

        post = get_object_or_404(Post, personal_key=pk)
        post.hearts += post.hearts
        post.save()

        return JsonResponse({'message' : f'회원 {post.user_name}의 하트 수가 1개 증가하였습니다. \n 회원 {post.user_name}의 하트는 총 {post.hearts}개 입니다.'})
    else:
        return JsonResponse({'message':'동작 실패하였습니다.'})

def represent(request):
    return 0

def allUser(request):
    return 0

