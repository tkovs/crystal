from django.http     import HttpResponse
from django.template import loader
from .models         import Usuario, Prova

def index(request):
	template = loader.get_template('crystal/index.html')
	context = {'title': 'Crystal'}

	return HttpResponse(template.render(context, request))

def test_list(request):
	template = loader.get_template('crystal/provas.html')
	tests = Prova.objects.all().order_by('titulo')
	context = {'title': 'Crystal - Provas', 'tests': tests}

	return HttpResponse(template.render(context, request))

def test_details(request, id):
	pass

def ranking(request):
	template = loader.get_template('crystal/ranking.html')
	users = Usuario.objects.all().order_by('-pontuacao')
	context = {'title': 'Crystal - Ranking', 'users': users}

	return HttpResponse(template.render(context, request))