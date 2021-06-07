from django.shortcuts import render
from django.contrib import messages
from django.http import HttpResponseRedirect
from .forms import AppUserForm

def register(request):
    if request.method == 'POST':
        form = AppUserForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Account Created Successfully.')
            return HttpResponseRedirect('register')
        else:
            er = form.errors
            print(form.error_messages)
            er = '<b>fuck you</b>'
            render(request, 'user_auth/register.html', {'form': form, 'err': str(er)})
    form = AppUserForm
    return render(request, 'user_auth/register.html', {'form':form})
