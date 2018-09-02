from .forms import CarroForm
from usuario_tipo.models import Motorista
from usuario_tipo.forms import MotoristaForm


def CarroFormMotoristaAdd(request):
    form = CarroForm(request.POST or None)
    if form.is_valid():
        if request.user.is_authenticated:
            current_user = request.user
            motorista = Motorista.objects.get(usuario_idusuario=current_user.id)
            form = CarroForm(form.setMotorista(motorista.idmotorista) or None)
            form.save()
            form = CarroForm()
    return form

def MotoristaFormAddCNH(request):
    form = MotoristaForm(request.POST or None)
    if form.is_valid():
        if request.user.is_authenticated:
            current_user = request.user
            form = MotoristaForm(form.setUsuario(current_user.id) or None)
            form.save()
            form = CarroForm()
    return form