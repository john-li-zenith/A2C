from django.views.generic.list import ListView
from django.utils import timezone
from django.contrib.auth.models import User
from apps.models import App, AppForm 
from django.contrib.auth.decorators import login_required
from django.shortcuts import render

from apps.models import App

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
        context['now'] = timezone.now()
        return context
        

@login_required
def app_upload(request):
    if request.method =='GET':
        form=AppForm(instance=get_or_return_none(App,user=request.user))
    else:
        form=AppForm(request.POST,instance=get_or_return_none(App,user=request.user))
        if form.is_valid():
            form.save(commit=False)
            form.user=request.user
            form.save()
            form.save_m2m()
        return render(request, 'apps/app_update.html', {'form': form})
    return render(request, 'apps/app_update.html', {'form': form})