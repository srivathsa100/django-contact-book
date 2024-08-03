from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from .models import Contact
from .forms import ContactForm, LoginForm
from django.contrib.auth import authenticate, login

@login_required
def saveinfo(request):
    if request.method == "POST":
        form = ContactForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = ContactForm()
    Data = Contact.objects.all()
    return render(request, "index.html", {'Data': Data, 'form': form})

@login_required
def index(request):
    Data = Contact.objects.all()
    form = ContactForm()
    return render(request, "index.html", {'Data': Data, 'form': form})

@login_required
def formupdate(request, id):
    contact = get_object_or_404(Contact, id=id)
    if request.method == "POST":
        form = ContactForm(request.POST, request.FILES, instance=contact)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = ContactForm(instance=contact)
    return render(request, 'edit.html', {'Data': contact , 'form': form})

@login_required
def edit(request, id):
    contact = get_object_or_404(Contact, id=id)
    form = ContactForm(instance=contact)
    return render(request, 'edit.html', {'form': form, 'Data': contact})

@login_required
def delete(request, id):
    contact = get_object_or_404(Contact, id=id)
    contact.delete()
    return redirect('index')

@login_required
def search(request):
    query = request.GET.get('query1')
    if query:
        results = Contact.objects.filter(
            Q(FirstName__icontains=query) | 
            Q(LastName__icontains=query) | 
            Q(ContactNumber__icontains=query) | 
            Q(Email__icontains=query)
        ).distinct()
    else:
        results = Contact.objects.all()
    
    context = {
        'Data': results
    }
    return render(request, 'index.html', context)

def custom_login(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('index')
            else:
                form.add_error(None, "Invalid username or password")
    else:
        form = LoginForm()
    return render(request, 'login.html', {'form': form})