from django import forms

class SubmissaoForm(forms.Form):
	autor       = forms.CharField(max_length=30)
	titulo      = forms.CharField(max_length=40)
	dificuldade = forms.ChoiceField(choices = ((1, 'FÁCIL'), (2, 'INICIANTE'), (3, 'COMUM'), (4, 'DIFÍCIL'), (5, 'MESTRE')))

	enunciado_1 = forms.CharField(max_length=100)
	questao_1_1 = forms.CharField(max_length=60)
	questao_1_2 = forms.CharField(max_length=60)
	questao_1_3 = forms.CharField(max_length=60)
	questao_1_4 = forms.CharField(max_length=60)

	enunciado_2 = forms.CharField(max_length=100)
	questao_2_1 = forms.CharField(max_length=60)
	questao_2_2 = forms.CharField(max_length=60)
	questao_2_3 = forms.CharField(max_length=60)
	questao_2_4 = forms.CharField(max_length=60)

	enunciado_3 = forms.CharField(max_length=100)
	questao_3_1 = forms.CharField(max_length=60)
	questao_3_2 = forms.CharField(max_length=60)
	questao_3_3 = forms.CharField(max_length=60)
	questao_3_4 = forms.CharField(max_length=60)

	enunciado_4 = forms.CharField(max_length=100)
	questao_4_1 = forms.CharField(max_length=60)
	questao_4_2 = forms.CharField(max_length=60)
	questao_4_3 = forms.CharField(max_length=60)
	questao_4_4 = forms.CharField(max_length=60)

	enunciado_5 = forms.CharField(max_length=100)
	questao_5_1 = forms.CharField(max_length=60)
	questao_5_2 = forms.CharField(max_length=60)
	questao_5_3 = forms.CharField(max_length=60)
	questao_5_4 = forms.CharField(max_length=60)

	