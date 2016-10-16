from django.db import models

class Usuario(models.Model):
	nome      = models.CharField(max_length = 30)
	pontuacao = models.IntegerField(default = 0)

	def __str__(self):
		pontos = "pontos"

		if (self.pontuacao <= 1):
			pontos = "ponto"


		return "{0} ({1} {2})".format(self.nome, self.pontuacao, pontos)

class Prova(models.Model):
	DIFICULDADE_ESCOLHAS = (
		(1, 'Muito fácil'),
		(2, 'Fácil'),
		(3, 'Normal'),
		(4, 'Difícil'),
		(5, 'Muito difícil'),
	)

	titulo      = models.CharField(max_length = 40)
	autor       = models.ForeignKey(Usuario, on_delete = models.CASCADE)
	dificuldade = models.IntegerField(default = 3, choices = DIFICULDADE_ESCOLHAS)

	def __str__(self):
		return "{0} ~ {1}".format(self.titulo, self.autor.nome)

class Questao(models.Model):
	prova      = models.ForeignKey(Prova, on_delete = models.CASCADE)
	enunciado  = models.CharField(max_length = 100)

	opcao1     = models.CharField(max_length = 60)
	opcao2     = models.CharField(max_length = 60)
	opcao3     = models.CharField(max_length = 60)
	opcao4     = models.CharField(max_length = 60)

	def __str__(self):
		return "{0}".format(self.enunciado)

class Realizado(models.Model):
	usuario = models.ForeignKey(Usuario, on_delete = models.CASCADE)
	prova   = models.ForeignKey(Prova, on_delete = models.CASCADE)

	def __str__(self):
		return "{0} ~ {1}".format(self.usuario.nome, self.prova.titulo)