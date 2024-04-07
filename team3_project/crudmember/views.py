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

def changePwd(request):
    return 0

def delUser(request, pk):
    if request.method == 'DELETE':
        post = get_object_or_404(Post, pk=pk)
        post.delete()
        data = {
            "message" : f"id: {pk} 포스트 삭제 완료"
        }
        return JsonResponse(data, status=200)
    return JsonResponse({'message':'DELETE 요청만 허용됩니다.'})

def userHeart(request):
    return 0

def represent(request,pk):
    if request.method ==" POST":       
        post = get_object_or_404(Post, pk=pk)
        if post.is_leader == True:
            post.is_leader = False
            post.save()
            data = { 
                "message" : f"{post.name}의 대표자격을 박탈하였습니다."
            }
            return JsonResponse(data, status=200)
        else:
            if True in Post.objects.values_list('is_leader',flat=True):
                data = {"message" : "대표는 2명이상일 수 없습니다."}
                return JsonResponse(data, status=400)

               
            else:
                post.is_Leader = True
                post.save()
                data = {"message" : f"{post.name}을 대표로 임명하였습니다."
                        }
                return JsonResponse(data, status=200)

def allUser(request):
    return 0

