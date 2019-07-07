# coding: utf-8
from kivy.app import App
from kivy.uix.screenmanager import Screen
from kivy.uix.popup import Popup
from kivy.uix.image import Image
from kivy.clock import Clock

class Perguntas(Screen):
	def __init__(self, **kwargs):
		super(Perguntas, self).__init__(**kwargs)
		#variable to iterate questions list
		self.indice = -1
		#creates the loading popup
		self.pop = Popup(title=' ', content=Image(source='Images/carregando.gif'), size_hint=(0.3, 0.3))

	#Method to get the database instance
	def getBanco(self):
		self.banco = App.get_running_app().root.ids.login.banco
		#Gets the question list
		self.perguntas = self.banco.getRandom(self.choice)
		#Initializes the score variable
		self.pontos = 0

	#Goes to the next question
	def nextpergunta(self):
		#Increments the variable responsible for iterate the questions list
		self.indice += 1
		#If the last question was the fifth
		if (self.indice == 5):
			'''Schedules the method to register the score
			and set the current screen to "terminou"'''
			Clock.schedule_once(self.registraPontos)
			'''Dismiss the popup that was open on the errou_acertou method
			after registering the score'''
			self.pop.dismiss()
		else:
			#Prepares the question elements to be shown on screen
			self.ids.texto.text = self.perguntas[self.indice].texto
			self.ids.b1.text = self.perguntas[self.indice].alt_A
			self.ids.b2.text = self.perguntas[self.indice].alt_B
			self.ids.b3.text = self.perguntas[self.indice].alt_C
			self.ids.b4.text = self.perguntas[self.indice].alt_D
			self.ids.imagem.source = ('Images/%s.png' % self.perguntas[self.indice].tipo)

	def registraPontos(self, dt):
			#Gets the screen manager root
			maintela = App.get_running_app().root
			#If the score wasn't "hacked"
			if (self.pontos < 6):
				'''Registers the score using a method in the login screen class.
				It's a bit ugly, but at least it worked lol'''
				try:
					maintela.ids.login.scorepontos(self.pontos, self.choice)
				except:
					App.get_running_app().root.current = 'bugou'
			#Generates a new list of questions
			try:
				self.perguntas = self.banco.getRandom(self.choice)
				self.indice = -1
				#Next 2 lines gets the user position from the login screen class
				todos = maintela.ids.login.getcolocacao(1, self.choice)
				hoje = maintela.ids.login.getcolocacao(0, self.choice)
				#Gets user score from the login screen class
				pontuacao = maintela.ids.login.getpontos(self.choice)
				#Prepares the elements to be shown on "terminou" screen
				maintela.ids.terminou.ids.rankjogador.jogador = maintela.ids.login.username
				maintela.ids.terminou.ids.rankjogador2.jogador = maintela.ids.login.username
				maintela.ids.terminou.ids.rankjogador.posicao = ("%dº" % todos)
				maintela.ids.terminou.ids.rankjogador2.posicao = ("%dº" % hoje)
				maintela.ids.terminou.ids.rankjogador.pontuacao = str(pontuacao[0])
				maintela.ids.terminou.ids.rankjogador2.pontuacao = str(pontuacao[1])
				maintela.ids.terminou.ids.resultado.text = ('SEU SALDO FOI DE %d PONTOS' % self.pontos)
				#Sets the current screen to "terminou"
				maintela.current = 'terminou'
				self.pontos = 0
				self.pop.dismiss()
			except:
				App.get_running_app().root.current = 'bugou'

	#Method that verifies if the answer was right or wrong
	def errou_acertou(self, alt):
		#Gets the screen manager root
		maintela = App.get_running_app().root
		if (self.indice != -1):
			#If the answer was right
			if (self.perguntas[self.indice].resposta == alt):
				self.pontos += 1
				#Verifies if it was the last question
				if (self.indice == 4):
						self.pop.open()
				else:
					#Shows up "acertou" screen
					maintela.current = 'acertou'
			else:
				self.pontos -= 1
				if (self.indice == 4):
						self.pop.open()
				else:
					#Shows up "errou" screen
					maintela.current = 'errou'
		#Runs the method responsible for preparing next question
		self.nextpergunta()

