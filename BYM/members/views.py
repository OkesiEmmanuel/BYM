from django.shortcuts import render, redirect
from .forms import MemberForm

def member_form(request):
    if request.method == 'POST':
        form = MemberForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('success')
    else:
        form = MemberForm()
    return render(request, 'members/form.html', {'form': form})

def success(request):
    return render(request, 'members/success.html')
