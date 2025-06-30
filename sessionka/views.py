from django.shortcuts import render, HttpResponse

# Create your views here.
def home(request):
    return HttpResponse('Hello World!')


def set_session_view(request):
    request.session['username'] = 'NIGGA'
    request.session['is_authenticated'] = True
    return HttpResponse('Sessions SET!')


def get_session_view(request):
    is_authenticated = request.session.get('is_authenticated')
    username = request.session['username']
    return HttpResponse(f'Username: {username}, Is authenticated: {is_authenticated}')


def delete_session_view(request):
    request.session.set_expiry(0)
    return HttpResponse('Session will be deleted with the browser closed')