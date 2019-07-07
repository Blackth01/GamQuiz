# coding: utf-8
from kivy.app import App
from kivy.uix.screenmanager import Screen
from kivy.clock import Clock
from kivy.core.audio import SoundLoader
from kivy.uix.popup import Popup
from kivy.uix.image import Image
from objects import Dados

class Login(Screen):
	def __init__(self, **kwargs):
		super(Login, self).__init__(**kwargs)
		try:
			#Creates the database instance
			self.banco = Dados()
			self.username = None
			self.registrou = False
			#Loads the song
			self.musica = SoundLoader.load('Songs/rc.ogg')
			#Creates the loading popup
			self.pop = Popup(title=' ', content=Image(source='Images/carregando.gif'), size_hint=(0.3, 0.3))

		except:
			Clock.schedule_once(self.erro)

	def erro(self, dt):
		#Runs the error screen
		App.get_running_app().root.current = 'bugou'
	def on_pre_leave(self):
		''' On the "creditos" screen, there is a variable
		that stores the name of the last screen, then it uses
		this variable to go back to the last screen when the
		return button is pressed. This command sets the last
		screen to "login" '''
		App.get_running_app().root.ids.creditos.atual = 'login'
	#Method to register new players
	def registra(self, dt):
		#Check if exists and registers the new user
		try:
			self.registrado = self.banco.registraJogador(self.ids.username.text, self.ids.senha.text)
		except:
			self.registrado = 0
			App.get_running_app().root.current = 'bugou'
		if (not self.registrado):
			self.ids.aviso.text = "ESTE USERNAME JÁ EXISTE!"
		else:
			#Check if user already registered a user in the current session
			if (self.registrou == True):
				self.ids.aviso.text = ("VOCÊ JÁ REGISTROU UM USUÁRIO")
			else:
				self.ids.aviso.text = "USUÁRIO REGISTRADO COM SUCESSO!"
				self.registrou = True

	#Method responsible for the login
	def loga(self, dt):
		#Check if username coincides with the password given
		try:
			self.token = self.banco.login(self.ids.username.text, self.ids.senha.text)
		except:
			self.token = 0
			App.get_running_app().root.current = 'bugou'
		if (self.token):
			'''The next lines set the username, passes the database instance to the
			"perguntas" screen class, play the song and set current screen to "perguntas" '''
			self.username = self.ids.username.text
			self.musica.play()
			App.get_running_app().root.current = 'menu'
		else:
			self.ids.aviso.text = "O USERNAME E A SENHA NÃO COINCIDEM!"


	#Method to show the loading popup and run the login method
	def proximo(self):
		self.pop.open()
		Clock.schedule_once(self.loga)
		self.pop.dismiss()

	#Method to show the loading popup and run the sign up method
	def registrando(self):
		self.pop.open()
		Clock.schedule_once(self.registra)
		self.pop.dismiss()

	#Method to update user score
	def scorepontos(self, pontos, choice):
		self.banco.setPontos(self.username, self.token, pontos, choice)

	#Method to return user score
	def getpontos(self, choice):
		pontos = self.banco.getPontos(self.username, choice)

		return pontos

	#Method to return user position
	def getcolocacao(self, opcao, choice):
		colocacao = self.banco.getColocacao(self.username, opcao, choice)

		return colocacao

	#Method responsible for opening the user browser on the gamquiz site
	def gotosite(self, *args):
		import webbrowser
		webbrowser.open('http://desenvolvedor.tech/gamquiz')
