from django.shortcuts import render, redirect
import requests
from django.views.decorators.csrf import csrf_exempt
# Create your views here.
from django.urls import reverse
from django.http import JsonResponse
import json
from .models import PresentKey


def index(request):
    return render(request, 'index.html', {})


@csrf_exempt
def callback_control(request):

    if request.method == "GET":
        callback_CHAT_TYPE = request.GET.get('CHAT_TYPE', None)
        callback_myKey = request.GET.get('myKey', None)
        print("callback_data: ", callback_CHAT_TYPE, callback_myKey)
        context = {'callback_CHAT_TYPE': callback_CHAT_TYPE, 'callback_myKey': callback_myKey}

        return JsonResponse({})

    if request.method == 'POST':
        context = json.loads(request.body)
        print('Context: ', context)
        key_val = PresentKey(key="key_idx", value=context['myKey'])
        key_val.save()

        return JsonResponse({})




# REST API 사용 로그인

# def oauth(request):
#     code = request.GET['code']
#     print('code = ' + str(code))
#
#     client_id = 'df3693a9b8c6a6e814e43d2fe3acc8b6'
#     # redirect_uri = 'http://127.0.0.1:8000/oauth'
#     redirect_uri = 'http://91db44ee63d5.ngrok.io/oauth'
#
#     access_token_request_uri = 'https://kauth.kakao.com/oauth/token?grant_type=authorization_code&'
#     access_token_request_uri += 'client_id=' + client_id
#     access_token_request_uri += '&redirect_uri=' + redirect_uri
#     access_token_request_uri += '&code=' + code
#     print('access_token_request_uri: ', access_token_request_uri)
#
#     access_token_request_uri_data = requests.get(access_token_request_uri)
#     json_data = access_token_request_uri_data.json()
#     access_token = json_data['access_token']
#     print('access_token: ', access_token)
#
#     user_profile_info_uri = 'https://kapi.kakao.com/v2/user/me?access_token='
#     user_profile_info_uri += str(access_token)
#     print('user_profile_info_uri: ',user_profile_info_uri)
#
#     user_profile_info_uri_data = requests.get(user_profile_info_uri)
#     user_json_data = user_profile_info_uri_data.json()
#     print("JSON: ", user_json_data)
#     user_nickname = user_json_data['properties']['nickname']
#     print('user_nickname: ', user_nickname)
#
#     return redirect('index')
#
# def kakaologin(request):
#
#     login_request_uri = 'https://kauth.kakao.com/oauth/authorize?'
#     client_id = 'df3693a9b8c6a6e814e43d2fe3acc8b6'
#     # redirect_uri = 'http://127.0.0.1:8000/oauth'
#     redirect_uri = 'http://91db44ee63d5.ngrok.io/oauth'
#
#     login_request_uri += 'client_id=' + client_id
#     login_request_uri += '&redirect_uri=' + redirect_uri
#     login_request_uri += '&response_type=code'
#
#     return redirect(login_request_uri)
#
