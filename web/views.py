from django.shortcuts import render
from rest_framework import viewsets
from serializers import *
from web.models import *
from django.shortcuts import render, render_to_response, redirect
from django.template import RequestContext
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required
from django.views.decorators.cache import never_cache
import json
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseBadRequest, HttpResponseForbidden


# Create your views here.

def parse_deudor(raw):
    from bs4 import BeautifulSoup as bs

    for tr in bs(raw).find_all('tr', class_='info'):
        return [td.get_text() for td in tr.find_all('td')]
    else:
        return None

    return None

def consult(request):
    import urllib, urllib2, cookielib

    cookie_jar = cookielib.CookieJar()
    opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cookie_jar))
    urllib2.install_opener(opener)

    # acquire cookie
    url_1 = 'http://www.machala.gob.ec/ConsultaDeuda/'
    req = urllib2.Request(url_1)
    rsp = urllib2.urlopen(req)

    # do POST
    url_2 = 'http://www.machala.gob.ec/ConsultaDeuda/Clases/consulta.php'
    values = dict(txtcadena='0702373119', tipo='1')
    data = urllib.urlencode(values)
    req = urllib2.Request(url_2, data)
    rsp = urllib2.urlopen(req)
    content = rsp.read()
    print parse_deudor(content)
    print content

def get_user(email, username):
    mail = User.objects.filter(email=email.lower())
    nick = User.objects.filter(username = username.lower())
    return not(len(mail)>0 or len(nick)>0)


@csrf_exempt
def signup(request):
    if request.method == "POST":
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        exist = get_user(email, username)
        if exist:
            user = User.objects.create_user(username, email, password)
            user.first_name = first_name
            user.last_name = last_name
            user.save()
            #user = authenticate(username=user, password=password)
            #login
            response = { 'id' : user.id }
            response['status'] = 'ok'
            return HttpResponse(json.dumps(response))
        else:
            #messages
            response = {'error':'ya existe el nombre de usuario o esta registrado'}

        return HttpResponseBadRequest(json.dumps(response))
    elif request.method == "GET":
        return HttpResponse(json.dumps({}))


@never_cache
@csrf_exempt
def login(request):
    #if not request.is_ajax() or request.method != 'GET':
    #    return
    try:
        username = request.POST['username']
        password = request.POST['password']
    except:
        return HttpResponseBadRequest('Bad parameters')

    from django.contrib.auth import authenticate, login

    user = authenticate(username=username, password=password)
    if user is not None:
        if user.is_active:
            login(request, user)
            response_content = {
                'username': user.username,
                'email': user.mail,
                'firstname': user.first_name,
                'lastname': user.lastname,
            }
            response =  HttpResponse(json.dumps(response_content))
            response['Content-Type'] = 'application/json; charset=utf-8'
            response['Cache-Control'] = 'no-cache'
            return response
        else:
            # Return a 'disabled account' error message
            return HttpResponseBadRequest('Usuario ha sido supendido')
    else:
        # Return an 'invalid login' error message.
        return HttpResponseBadRequest('Usuario o clave incorrecto')



