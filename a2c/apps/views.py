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
        return reverse('thankyou')

    def get_queryset(self):
        return super(AppUpdateCreateView, self).get_queryset().filter(user=self.request.user) 
        
       
        
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