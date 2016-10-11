from django.db import models

class Usuario(models.Model):
	nome      = models.CharField(max_length = 30)
	pontuacao = models.IntegerField(default = 0)

	def __str__(self):
		pontos = "pontos"

		if (pontuacao <= 1):
			pontos = "ponto"


		return "{0} ({1} {2})".format(nome, pontuacao, pontos)

class Prova(models.Model):
	titulo = models.CharField(max_length = 30)
	autor  = models.ForeignKey(Usuario, on_delete = models.CASCADE)

	def __str__(self):
		return "{0} ~ {1}".format(titulo, autor)

class Questao(models.Model):
	prova      = models.ForeignKey(Prova, on_delete = models.CASCADE)
	enunciado  = models.CharField(max_length = 100)

	resposta   = models.IntegerField()
	opcao1     = models.CharField(max_length = 60)
	opcao2     = models.CharField(max_length = 60)
	opcao3     = models.CharField(max_length = 60)
	opcao4     = models.CharField(max_length = 60)

	def __str__(self):
		return "{0} ~ {1}".format(disciplina, enunciado)

class Realizado(models.Model):
	usuario = models.ForeignKey(Usuario, on_delete = models.CASCADE)
	prova   = models.ForeignKey(Prova, on_delete = models.CASCADE)

	def __str__(self):
		return "{0} ~ {1}".format(usuario.nome, prova.titulo)