from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.contrib.auth.forms import PasswordResetForm
from django.contrib.auth.models import User
from django.template.loader import render_to_string
from django.db.models.query_utils import Q
from django.utils.http import urlsafe_base64_encode
from django.contrib.auth.tokens import default_token_generator
from django.utils.encoding import force_bytes
from django.core.mail import send_mail, BadHeaderError
from django.contrib.auth import authenticate, login, logout
from planning.models import *
from . import forms

# Create your views here.

def password_reset_request(request):
	if request.method == "POST":
		password_reset_form = PasswordResetForm(request.POST)
		if password_reset_form.is_valid():
			data = password_reset_form.cleaned_data['email']
			associated_users = User.objects.filter(Q(email=data))
			if associated_users.exists():
				for user in associated_users:
					subject = "Password Reset Requested"
					email_template_name = "main/password/password_reset_email.txt"
					c = {
					"email":user.email,
					'domain':'127.0.0.1:8000',
					'site_name': 'Website',
					"uid": urlsafe_base64_encode(force_bytes(user.pk)),
					"user": user,
					'token': default_token_generator.make_token(user),
					'protocol': 'http',
					}
					email = render_to_string(email_template_name, c)
					try:
						send_mail(subject, email, 'admin@example.com' , [user.email], fail_silently=False)
					except BadHeaderError:
						return HttpResponse('Invalid header found.')
					return redirect ("/password_reset/done/")
	password_reset_form = PasswordResetForm()
	return render(request=request, template_name="main/password/password_reset.html", context={"password_reset_form":password_reset_form})

def indexMain(request):
    """
    Affiche la page d'accueil du site web pour l'application PalmPlanning

    **Template:**

    :template:`main/index.html`
    """
    return render(request, "main/index.html")

@login_required(login_url='login_user')
def indexApp(request):
    """
    Affiche la page d'accueil de l'application planning

    **Context:**

    `usr`
        Une instance du modèle :model:`planning.ENTRAINEUR`

    **Template:**

    :template:`planning/index.html`
    """
    usr = ENTRAINEUR.objects.get(UserId=request.user)
    return render(request, "planning/index.html", {'usr': usr})

def login_user(request):
    """
    Affiche la page de connexion de l'application planning

    **Template:**

    :template:`planning/login.html`
    """
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(username=username, password=password)
        if user:
            login(request, user)
            return redirect('indexApp')
        else:
            error = "Mauvais identifiants de connexion"
            return render(request, 'planning/login.html', {'error': error})
    return render(request, 'planning/login.html')

@login_required(login_url='login_user')
def logout_user(request):
    """
    Vue de déconnexion de l'application planning
    """
    logout(request)
    return redirect('indexMain')

def create_entrainement(request):
    """
    Affiche la page de création d'un entrainement

    **Template:**

    :template:`planning/create_entrainement.html`
    """
    submitted = False
    if request.method == "POST":
        form = forms.ENTRAINEMENTForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('dashboard')
    else:
        form = forms.ENTRAINEMENTForm()
        if 'submitted' in request.GET:
            submitted = True
    return render(request, 'planning/create_entrainement.html', {'form': form})

def dashboard(request):
    """
    Affiche la page de dashboard de l'application planning

    **Template:**

    :template:`planning/dashboard.html`
    """
    entrainements = ENTRAINEMENT.objects.all()
    return render(request, 'planning/dashboard.html', {'entrainements': entrainements})

def modifEntrainement(request, titre):
    """
    Affiche la page d'un entrainement

    **Template:**

    :template:`planning/entrainement.html`
    """
    submitted = False
    entrainement = ENTRAINEMENT.objects.get(Titre=titre)
    if request.method == "POST":
        form = forms.ENTRAINEMENTForm(request.POST, instance=entrainement)
        if form.is_valid():
            form.save()
            return redirect('dashboard')
    else:
        form = forms.ENTRAINEMENTForm(instance=entrainement)
        if 'submitted' in request.GET:
            submitted = True
    return render(request, 'planning/entrainement.html', {'entrainement': entrainement, 'form': form})

def deleteEntrainement(request, titre):
    """
    Supprime un entrainement

    **Template:**

    :template:`planning/dashboard.html`
    """
    entrainement = ENTRAINEMENT.objects.get(Titre=titre)
    entrainement.delete()
    return redirect('dashboard')