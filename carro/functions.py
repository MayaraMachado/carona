from .forms import CarroForm


def CarroFormMotoristaAdd(request):
    form = CarroForm(request.POST or None)
    if form.is_valid():
        if request.user.is_authenticated:
            current_user = request.user
            form = CarroForm(form.setMotorista(current_user.id) or None)
            form.save()
            form = CarroForm()
    return form