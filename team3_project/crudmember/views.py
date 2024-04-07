from django.shortcuts import render, get_object_or_404
import json
from django.http import JsonResponse
from django.shortcuts import get_list_or_404
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

crudmember/models.py

    class Post(models.Model):
    personal_key = models.IntegerField() # id(pk)
    email = models.CharField(max_length=100) # 100글자가 최대인 문자열
    is_leader = models.BooleanField() # 대표 여부
    hearts = models.IntegerField() # 하트 수
    password = models.CharField(max_length=100) # 비밀번호
    user_name = models.CharField(max_length=100) #회원 이름

'''
def addUser(request):
    if request.method == 'POST':
        data = json.loads(request.body)

        email = data.get('email')
        is_leader = data.get('is_leader')
        hearts = data.get('hearts')
        password = data.get('password')
        user_name = data.get('user_name')

        post = Post(
            email = email,
            is_leader = is_leader,
            hearts = hearts,
            password = password,
            user_name = user_name
        )
        post.save()

        return JsonResponse({'message':'success'})
    return JsonResponse({'message' : 'POST 요청만 허용됩니다.'})


def userInfo(request, pk): # 입력값: id (personal_key) -> 출력값: id, email, 대표 여부, 하트 수
    if request.method == 'GET':
        post = get_object_or_404(Post, pk = pk)
        data = {
            'id' : post.pk,
            'email' : post.email,
            'is_leader' : post.is_leader,
            'hearts' : post.hearts
        }
        return JsonResponse(data, status = 200)
    else:
        return JsonResponse({'message':'GET 요청만 허용됩니다.'})

def changePwd(request, pk):
    if request.method == 'PUT':
        data = json.loads(request.body)
        new_pwd = data.get('new_password')
    
        if new_pwd:
            post = get_object_or_404(Post, pk=pk)
            post.password = new_pwd
            post.save()

            return JsonResponse({'message' : f'비밀번호가 변경되었습니다. 새로운 비밀번호는 {new_pwd}입니다.'})
        else:
            return JsonResponse({'message':'비밀번호 변경에 실패하였습니다.'})
    else:
        return JsonResponse({'message':'PUT 요청만 허용됩니다.'})
        

def delUser(request, pk):
    if request.method == 'DELETE':
        post = get_object_or_404(Post, pk=pk)
        post.delete()
        data = {
            "message" : f"id: {pk} 포스트 삭제 완료"
        }
        return JsonResponse(data, status=200)
    return JsonResponse({'message':'DELETE 요청만 허용됩니다.'})

def userHeart(request, pk):
    if request.method == 'PUT':
        post = get_object_or_404(Post, pk=pk)
        post.hearts = post.hearts+1
        post.save()

        return JsonResponse({'message' : f'회원 {post.user_name}의 하트 수가 1개 증가하였습니다. \n 회원 {post.user_name}의 하트는 총 {post.hearts}개 입니다.'})
    else:
        return JsonResponse({'message':'동작 실패하였습니다.'})

def represent(request,pk):
    if request.method ==" POST":       
        post = get_object_or_404(Post, pk=pk)
        if post.is_leader == True:
            post.is_leader = False
            post.save()
            data = { 
                "message" : f"{post.user_name}의 대표자격을 박탈하였습니다."
            }
            return JsonResponse(data, status=200)
        else:
            leaderlist=get_list_or_404(Post, is_leader=True)
            if len(leaderlist) >=2:
                data = {"message" : "대표는 2명이상일 수 없습니다."}
                return JsonResponse(data, status=400)
               
            else:
                post.is_Leader = True
                post.save()
                data = {"message" : f"{post.user_name}을 대표로 임명하였습니다."
                        }
                
                return JsonResponse(data, status=200)
    else:
        return JsonResponse({'message':'PUT 요청만 허용됩니다.'})
    
def allUser(request):
    if request.method == 'GET':
        post = Post.objects.all()

        member_count = 0
        total_hearts = 0

        for i in range(0, len(post)):
            member_count += 1
            total_hearts += post[i].hearts
        
        data = {
            'message' : '전체 회원 정보입니다.',
            'member_count' : member_count,
            'total_hearts' : total_hearts
        }

        return JsonResponse(data, status = 200)
    else:
        return JsonResponse({'message':'GET 요청만 허용됩니다.'})