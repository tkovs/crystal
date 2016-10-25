from django.http              import HttpResponse, HttpResponseRedirect
from django.template          import loader
from .models                  import Usuario, Prova, Questao, Realizado
from .forms                   import SubmissaoForm
from django.core.urlresolvers import reverse
from random                   import shuffle

def index(request):
	template = loader.get_template('crystal/index.html')
	context = {'title': 'Crystal'}

	return HttpResponse(template.render(context, request))

def test_list(request):
	template = loader.get_template('crystal/provas.html')
	tests = Prova.objects.all().order_by('titulo')
	context = {'title': 'Crystal - Provas', 'tests': tests}

	return HttpResponse(template.render(context, request))

def submit_test(request):
	template = loader.get_template('crystal/submissao.html')

	if request.method == 'GET':
		test_length = 5 # tamanho da prova
		form = SubmissaoForm()
		context = {
			'form': form,
			'title': 'Crystal - Nova prova',
			'test_length': range(1, test_length + 1), 
			'options_length': range(1, test_length)
		}

		return HttpResponse(template.render(context, request))
	elif request.method == 'POST':
		form = SubmissaoForm(request.POST)

		if form.is_valid():
			if (Usuario.objects.filter(nome = form.cleaned_data['autor']).exists()):
				author = Usuario.objects.get(nome = form.cleaned_data['autor'])
			else:
				author = Usuario.objects.create(nome = form.cleaned_data['autor'])
				author.save()

			if (Prova.objects.filter(titulo = form.cleaned_data['titulo']).exists()):
				return HttpResponse('Prova já existente')

			test = Prova.objects.create(titulo = form.cleaned_data['titulo'],
										autor  = author,
									    dificuldade = form.cleaned_data['dificuldade'])

			for q in range(1, 6):
				Questao.objects.create(prova     = test,
			                   		   enunciado = form.cleaned_data["enunciado_{0}".format(q)],
			                   		   opcao1    = form.cleaned_data["questao_{0}_1".format(q)],
			                   		   opcao2    = form.cleaned_data["questao_{0}_2".format(q)],
									   opcao3    = form.cleaned_data["questao_{0}_3".format(q)],
			            	       	   opcao4    = form.cleaned_data["questao_{0}_4".format(q)],
			         	          	   opcao5    = form.cleaned_data["questao_{0}_5".format(q)]).save()

		context = {
			'title': 'Crystal - Prova submetida!',
			'test_id': test.id
		}

		return HttpResponse(template.render(context, request))

def shuffle_question(question):
	options = [question.opcao1, question.opcao2, question.opcao3, question.opcao4, question.opcao5]
	shuffle(options)
	question.opcao1 = options[0]
	question.opcao2 = options[1]
	question.opcao3 = options[2]
	question.opcao4 = options[3]
	question.opcao5 = options[4]

	return question

def check_question(question, answer):
	question = Questao.objects.get(id = question.id)
	if answer == question.opcao1:
		return 1

	return 0
		
def test_details(request, id):
	template = loader.get_template('crystal/prova.html')
	test = Prova.objects.get(id = id)
	
	if request.method == 'GET':
		questions = Questao.objects.filter(prova = test)
		questions = [shuffle_question(question) for question in questions]

		context = {
			'title': "Crystal - {0}".format(test.titulo),
			'test': test,
			'questions': questions
		}

		return HttpResponse(template.render(context, request))
	elif request.method == 'POST':
		if (Usuario.objects.filter(nome = request.POST['user']).exists()):
			user = Usuario.objects.get(nome = request.POST['user'])
			if (Realizado.objects.filter(usuario = user, prova = test).exists()):
				return HttpResponseRedirect('/crystal/')

		qs = Questao.objects.filter(prova = test) # qs = questions
		answers = []

		for q in range(len(qs)):
			answers.append([qs[q], request.POST["question{0}".format(q + 1)]])

		result = sum([check_question(answer[0], answer[1]) for answer in answers])

		if (not Usuario.objects.filter(nome = request.POST['user']).exists()):
			new_user = Usuario.objects.create(nome = request.POST['user'], pontuacao = result)
			new_user.save()
			Realizado.objects.create(usuario = new_user, prova = test).save()
		else:
			user = Usuario.objects.get(nome = request.POST['user'])
			user.pontuacao += result
			user.save()
			Realizado.objects.create(usuario = user, prova = test).save()

		context = {
			'title': "Crystal - {0}".format(test.titulo),
			'answers': answers,
			'result': result
		}

		return HttpResponse(template.render(context, request))

def ranking(request):
	template = loader.get_template('crystal/ranking.html')
	
	users = Usuario.objects.all() \
						   .filter(pontuacao__gt = 0) \
						   .order_by('-pontuacao')

	context = {'title': 'Crystal - Ranking', 'users': users}

	return HttpResponse(template.render(context, request))