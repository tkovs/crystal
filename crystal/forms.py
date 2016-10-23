from django import forms

class SubmissaoForm(forms.Form):
	autor       = forms.CharField(max_length=30)
	titulo      = forms.CharField(max_length=40)
	dificuldade = forms.ChoiceField(choices = ((1, 'Muito fácil'), (2, 'Fácil'), (3, 'Médio'), (4, 'Difícil'), (5, 'Muito difícil')))

	enunciado_1 = forms.CharField(max_length=300)
	questao_1_1 = forms.CharField(max_length=150)
	questao_1_2 = forms.CharField(max_length=150)
	questao_1_3 = forms.CharField(max_length=150)
	questao_1_4 = forms.CharField(max_length=150)

	enunciado_2 = forms.CharField(max_length=300)
	questao_2_1 = forms.CharField(max_length=150)
	questao_2_2 = forms.CharField(max_length=150)
	questao_2_3 = forms.CharField(max_length=150)
	questao_2_4 = forms.CharField(max_length=150)

	enunciado_3 = forms.CharField(max_length=300)
	questao_3_1 = forms.CharField(max_length=150)
	questao_3_2 = forms.CharField(max_length=150)
	questao_3_3 = forms.CharField(max_length=150)
	questao_3_4 = forms.CharField(max_length=150)

	enunciado_4 = forms.CharField(max_length=300)
	questao_4_1 = forms.CharField(max_length=150)
	questao_4_2 = forms.CharField(max_length=150)
	questao_4_3 = forms.CharField(max_length=150)
	questao_4_4 = forms.CharField(max_length=150)

	enunciado_5 = forms.CharField(max_length=300)
	questao_5_1 = forms.CharField(max_length=150)
	questao_5_2 = forms.CharField(max_length=150)
	questao_5_3 = forms.CharField(max_length=150)
	questao_5_4 = forms.CharField(max_length=150)

	