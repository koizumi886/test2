from django.shortcuts import render
from django.http.response import HttpResponse
# Create your views here.
def hello (request):
    return HttpResponse('<h1>こんにちは！</h1>')

import random
運勢 = ['大吉', '中吉', '小吉']

def omikuji (request):
    n = random.randint(0,2) #乱数で0,1,2のいずれかを生成
    return HttpResponse('<h1>今日の運勢は、' + 運勢[n] + '</h1>')

def t_omikuji (request):
    n = random.randint(0,2) #乱数で0,1,2のいずれかを生成
    # return HttpResponse('<h1>今日の運勢は、' + 運勢[n] + '</h1>')
    params = {'text':'本日の運勢', 'result':運勢[n]}
    return render(request, 'omikuji.html', params)

import requests as rq # サーバにURLを送るためのライブラリ
def weather(request):
    url = 'https://weather.tsukumijima.net/api/forecast/city/'
    r = rq.get(url + '020030') # 八戸の天気を調べる（ブラウザのアドレスバーに入力するのと同じ）
    天気 = r.json() # 辞書形式に変換
    telop = 天気['forecasts'][1]['telop'] # 真ん中の数字は、0:今日 1:明日 2:明後日を表す
    return HttpResponse('<h1>あすの天気は、' + telop + '</h1>')

