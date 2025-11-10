from django.shortcuts import render
from contact.forms import RegisterForm
form= RegisterForm()
context={
    'form':form
}
def register(request):
    form= RegisterForm()
    context={
        'form':form
    }
    if request.method=='POST':
        form=RegisterForm(request.POST)

        if form.is_valid():
            form.save()

    return render(
        request,
        'contact/register.html',
        context 
    )