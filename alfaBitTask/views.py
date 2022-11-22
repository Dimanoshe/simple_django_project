from django.shortcuts import render
from django.http import HttpResponse
from .models import LeadState, Lead

def index(request):

    new = LeadState.objects.get(name='STATE_NEW')
    in_progress = LeadState.objects.get(name='STATE_IN_PROGRESS')
    postponed = LeadState.objects.get(name='STATE_POSTPONED')
    done = LeadState.objects.get(name='STATE_DONE')


    ld = Lead.objects.get(name='test')

    '''
    Метод обновления статуса:
    status_update(объект, новый статус)
    '''
    Lead.status_update(ld, done)

    return HttpResponse(ld.state.name)