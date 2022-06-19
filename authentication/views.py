from django.shortcuts import render, redirect
from .forms import UserRegistrationForm
from django.contrib.auth.models import User


def userReg(request):
    regForm = UserRegistrationForm()

    # userModelField = User._meta.get_fields()
    # for um in userModelField:
    #     print(um)

    if request.method == 'POST':
        #form = UserRegistrationForm(request.POST)
        #if form.is_valid():
          #  form.save()

        print('Username:', request.POST['user_name'])
        print('Email:', request.POST['email'])
        print('Gender:', request.POST['gender'])
        print('Password1:', request.POST['pass1'])
        print('Password2:', request.POST['pass2'])

        User.objects.create(
            username=request.POST['user_name'],
            email=request.POST['email'],
            password=request.POST['pass1'],
        )
        return redirect('authApplication:userReg')


    context = {
        'regForm': regForm,
    }
    return render(request, 'authentication/reg_form/regForm.html', context)
