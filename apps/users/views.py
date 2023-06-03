from django.utils import timezone
from django.contrib import messages
from django.shortcuts import redirect, render
from django.contrib.auth import get_user_model, authenticate, login, logout
from django.urls import reverse
from django.utils.http import urlsafe_base64_decode
from django.utils.encoding import force_str
from django.contrib.sites.shortcuts import get_current_site
from django.utils.translation import gettext_lazy as _

from apps.users.forms import Sign_UpForm
from apps.users.token import generate_token
from apps.users.email import send_email_activation_account, send_email_activation_account_success

User = get_user_model()


def sign_up(request):
    if request.method == 'POST':
        user_form = Sign_UpForm(data=request.POST)
        if user_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            # user.is_email_verified = True
            user.save()
            
            msg = f"""{_('Merci de votre incription. Veuillez activer votre adresse e-mail pour accéder à votre compte Mackdin')}. \n {_('Nous avons envoyé un email à %(email)s')} % {user.email} \n {_('pour activer votre compte Mackdin')}. \n {("Si vous n'avez pas reçu l'email, veuillez vérifier votre dossier spam.")}"""
            # msg: str = f"Votre compte a été créé et est prêt à être utilisé !"
            
            messages.success(request, msg)
            
            # mail d'activation du compte
            send_email_activation_account(user, request)
            return redirect('sign_in')
        else:
            messages.error(request, _("Merci de bien remplir les informations correctement."))
    else:
        user_form = Sign_UpForm()
    template = 'users/sign_up.html'
    context = {
        'user_form': user_form,
    }
    return render(request, template, context=context)
    

def sign_in(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        user = authenticate(email=email, password=password)
        if user:
            if not user.is_email_verified:
                messages.warning(request, _("Merci de confirmer d'abord votre adresse email."))
                return redirect('sign_in')
            else:
                login(request, user)
                return redirect('post:post_list')
        # elif User.objects.filter(email=email).exists():
        #     messages.error(request, "ERREUR : mot de passe ou adresse email est incorrect.")
        else:
            messages.error(request, _("ERREUR : adresse email ou mot de passe incorrect."))
            # messages.error(request, "ERREUR : Il semble que vous n'avez pas compte avec cette adresse email")
    template = 'users/sign_in.html'
    return render(request, template)


def user_logout(request):
    user = request.user
    user.last_logout = timezone.now()
    user.save()
    logout(request)
    return redirect('home:home')


def activate_user(request, uidb64, token):
    try:
        uid = force_str(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
    except Exception as e:
        user = None
    if user and generate_token.check_token(user, token):
        user.is_email_verified = True
        user.save()
        send_email_activation_account_success(user, request)
        messages.success(request, _("Votre email est vérifié avec succès. Vous pouvez vous connecter."))
        return redirect(reverse('sign_in'))
    template = 'users/activate_failed.html'
    context = {'user': user}
    return render(request, template, context=context)