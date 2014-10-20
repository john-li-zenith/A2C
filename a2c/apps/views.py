from django.views.generic.list import ListView
from django.utils import timezone
from django.contrib.auth.models import User
from apps.models import App, AppUpdate
from apps.forms import AppForm, AppUpdateForm
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.shortcuts import get_object_or_404
from apps.models import App, AppLog,AppUpdate
from django.http import HttpResponseRedirect
from django.http import Http404
from django.views.generic.edit import CreateView
from django.db.models import Count
from django.core.urlresolvers import reverse
import requests
import datetime
from django.shortcuts import render
import json
from django.core.mail import send_mail


def get_or_return_none(classobject,**kwags):
    try:
        return classobject.objects.get(**kwags)
    except classobject.DoesNotExist:
        return None
        

class AppListView(ListView):

    model = App
    
    def get_queryset(self):
        return App.objects.filter(user=self.request.user)
    
    def get_context_data(self, **kwargs):
        context = super(AppListView, self).get_context_data(**kwargs)
        #context['now'] = timezone.now()
        return context
        
class AppLogListView(ListView):
    
    model=AppLog
    template_name = 'apps/applog_list.html'
    
    def get_queryset(self):
        self.app = get_object_or_404(App, id=self.args[0])
        return AppLog.objects.filter(app=self.app)
        
    def get_context_data(self, **kwargs):
        context = super(AppLogListView, self).get_context_data(**kwargs)
        context['types']=AppLog.objects.values('type__name').annotate().order_by()
        context['app'] = self.app.name
        return context
    
    
# @login_required
# def app_upload(request):
#     if request.method =='GET':
#         form=AppForm(instance=get_or_return_none(App,user=request.user))
#     else:
#         form=AppForm(request.POST,instance=get_or_return_none(App,user=request.user))
#         if form.is_valid():
#             form.save(commit=False)
#             form.user=request.user
#             form.save()
#             form.save_m2m()
#         return render(request, 'apps/app_upload.html', {'form': form})
#     return render(request, 'apps/app_upload.html', {'form': form})

class AppUploadCreateView(CreateView):
    model = App
    form_class = AppForm
    template_name = 'apps/app_upload.html'

    def get_initial(self):
        initial = super(AppUploadCreateView,self).get_initial()
        initial['user'] = self.request.user
        return initial

    def get_success_url(self):
        send_mail(self.request.user.username+' uploaded an app', 'Please go to Admin site to check out.', 'app2china.com',
    ['app2china@gmail.com'], fail_silently=False)
        return HttpResponseRedirect(reverse('thankyou'))

    def get_queryset(self):
        return super(AppUploadCreateView,self).get_queryset().filter(user=self.request.user) 
        
        
class AppUpdateCreateView(CreateView):
    model = AppUpdate
    form_class = AppUpdateForm
    template_name = 'apps/app_update.html'

    def get_initial(self):
        initial = super(AppUpdateCreateView,self).get_initial()
        initial['user'] = self.request.user
        return initial

    def get_success_url(self):
        send_mail(self.request.user.username+' updated an app', 'Please go to Admin site to check out.', 'app2china.com',
    ['app2china@gmail.com'], fail_silently=False)
        return reverse('thankyou')

    def get_queryset(self):
        return super(AppUpdateCreateView, self).get_queryset().filter(user=self.request.user) 
        
    def get_form_kwargs(self):
        kwargs = super(AppUpdateCreateView, self ).get_form_kwargs()
        kwargs['user'] = self.request.user
        return kwargs

       
        
# @login_required
# def app_update(request):
#     if request.method =='GET':
#         form=AppUpdateForm()
#     else:
#         form=AppUpdateForm(request.POST)
#         if form.is_valid():
#             form.save(commit=False)
#             form.user=request.user
#             form.save()
#             form.save_m2m()
#             return HttpResponseRedirect('/accounts/thankyou/')
#     #app_update=AppUpdate.objects.filter(app=form.app)
#     return render(request, 'apps/app_update.html', {'form': form,})

def return_zero_if_empty(li):
    if not li:
        return '0'
    else:
        return li

@login_required
def umeng(request,appid):
    auth=("app2china@126.com:app2china126").encode('base64')
    end_date=datetime.date.today()
    start_date=end_date+datetime.timedelta(weeks=-1)
    app=App.objects.get(id=appid)
    appkey=app.appkey
    if not appkey:
        return render(request, 'apps/app_track.html', {"result": "You app doesnt have an appkey!"})
    newuser_url = "http://api.umeng.com/new_users?appkey="+appkey+"&start_date="+str(start_date)+"&end_date="+str(end_date)+"&period_type=weekly"
    activeuser_url= "http://api.umeng.com/active_users?appkey="+appkey+"&start_date="+str(start_date)+"&end_date="+str(end_date)+"&period_type=weekly"
    launches_url="http://api.umeng.com/launches?appkey="+appkey+"&start_date="+str(start_date)+"&end_date="+str(end_date)+"&period_type=weekly"
    r_newuser=requests.get(newuser_url,headers={'Authorization':'Basic '+str(auth)})
    r_activeuser=requests.get(activeuser_url,headers={'Authorization':'Basic '+str(auth)})
    r_launches=requests.get(launches_url,headers={'Authorization':'Basic '+str(auth)})
    r_newuser_data=json.loads(r_newuser.text)
    r_activeuser_data=json.loads(r_activeuser.text)
    r_launches_data=json.loads(r_launches.text)
    newuser_number=return_zero_if_empty(r_newuser_data['data']['all'])
    activeuser_number=return_zero_if_empty(r_activeuser_data['data']['all'])
    lauches_number=return_zero_if_empty(r_launches_data['data']['all'])
    result="<div id='plan'><table border='2' padding='2' class='table'><thead><tr><td>No. of New Users</td><td>No. of Active Users</td><td>No. of Launches</td></tr></thead><tbody><tr><td>"+str(newuser_number[0])+"</td><td>"+str(activeuser_number[0])+"</td><td>"+str(lauches_number[0])+"</td></tr></tbody></table></div>"
    return render(request, 'apps/app_track.html', {"result": result})