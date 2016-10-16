from django.http              import HttpResponse
from django.template          import loader
from .models                  import Usuario, Prova, Questao
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

			Questao.objects.create(prova     = test,
				                   enunciado = form.cleaned_data['enunciado_1'],
				                   opcao1    = form.cleaned_data['questao_1_1'],
				                   opcao2    = form.cleaned_data['questao_1_2'],
				                   opcao3    = form.cleaned_data['questao_1_3'],
				                   opcao4    = form.cleaned_data['questao_1_4']).save()

			Questao.objects.create(prova     = test,
				                   enunciado = form.cleaned_data['enunciado_2'],
				                   opcao1    = form.cleaned_data['questao_2_1'],
				                   opcao2    = form.cleaned_data['questao_2_2'],
				                   opcao3    = form.cleaned_data['questao_2_3'],
				                   opcao4    = form.cleaned_data['questao_2_4']).save()

			Questao.objects.create(prova     = test,
				                   enunciado = form.cleaned_data['enunciado_3'],
				                   opcao1    = form.cleaned_data['questao_3_1'],
				                   opcao2    = form.cleaned_data['questao_3_2'],
				                   opcao3    = form.cleaned_data['questao_3_3'],
				                   opcao4    = form.cleaned_data['questao_3_4']).save()

			Questao.objects.create(prova     = test,
				                   enunciado = form.cleaned_data['enunciado_4'],
				                   opcao1    = form.cleaned_data['questao_4_1'],
				                   opcao2    = form.cleaned_data['questao_4_2'],
				                   opcao3    = form.cleaned_data['questao_4_3'],
				                   opcao4    = form.cleaned_data['questao_4_4']).save()

			Questao.objects.create(prova     = test,
				                   enunciado = form.cleaned_data['enunciado_5'],
				                   opcao1    = form.cleaned_data['questao_5_1'],
				                   opcao2    = form.cleaned_data['questao_5_2'],
				                   opcao3    = form.cleaned_data['questao_5_3'],
				                   opcao4    = form.cleaned_data['questao_5_4']).save()

		context = {
			'title': 'Crystal - Prova submetida!',
			'test_id': test.id
		}

		return HttpResponse(template.render(context, request))

def shuffle_question(question):
	options = [question.opcao1, question.opcao2, question.opcao3, question.opcao4]
	shuffle(options)
	question.opcao1 = options[0]
	question.opcao2 = options[1]
	question.opcao3 = options[2]
	question.opcao4 = options[3]

	return question

def check_question(question, answer):
	question = Questao.objects.get(id = question.id)
	return answer == question.opcao1
		
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
		questions = Questao.objects.filter(prova = test)
		answers = []
		answers.append([questions[0].enunciado, questions[0].opcao1, request.POST['question1'], check_question(questions[0], request.POST['question1'])])
		answers.append([questions[1].enunciado, questions[1].opcao1, request.POST['question2'], check_question(questions[1], request.POST['question2'])])
		answers.append([questions[2].enunciado, questions[2].opcao1, request.POST['question3'], check_question(questions[2], request.POST['question3'])])
		answers.append([questions[3].enunciado, questions[3].opcao1, request.POST['question4'], check_question(questions[3], request.POST['question4'])])
		answers.append([questions[4].enunciado, questions[4].opcao1, request.POST['question5'], check_question(questions[4], request.POST['question5'])])
		
		return HttpResponse("Respostas: {0}".format(answers))

def ranking(request):
	template = loader.get_template('crystal/ranking.html')
	
	users = Usuario.objects.all() \
						   .filter(pontuacao__gt = 0) \
						   .order_by('-pontuacao')

	context = {'title': 'Crystal - Ranking', 'users': users}

	return HttpResponse(template.render(context, request))