# coding: utf-8
from kivy.app import App
from kivy.uix.screenmanager import Screen
from kivy.uix.popup import Popup
from kivy.uix.image import Image
from kivy.clock import Clock

class Terminou(Screen):
	def __init__(self, **kwargs):
		super(Terminou, self).__init__(**kwargs)
		self.parou = False
		self.pop = Popup(title=' ', content=Image(source='Images/carregando.gif'), size_hint=(0.3, 0.3))
	def on_pre_leave(self):
		''' On the "creditos" screen, there is a variable
		that stores the name of the last screen, then it uses
		this variable to go back to the last screen when the
		return button is pressed. This command sets the last
		screen to "terminou" '''
		App.get_running_app().root.ids.creditos.atual = 'terminou'

	#Method responsible for running one of the top10 methods
	def gerarTop10(self, opcao):
		self.pop.open()
		if  (opcao == 1):
			Clock.schedule_once(self.gerandoTop10)
		else:
			Clock.schedule_once(self.gerandoTopHoje)
		self.pop.dismiss()

	#Method responsible for setting the "Today Top10" on the "top10" screen class
	def gerandoTopHoje(self, dt):
		App.get_running_app().root.ids.top10.setTop10(2)
		App.get_running_app().root.current = 'top10'

	#Method responsible for setting the "All time Top10" on the "top10" screen class
	def gerandoTop10(self, dt):
		App.get_running_app().root.ids.top10.setTop10(1)
		App.get_running_app().root.current = 'top10'

	#Method responsible for playing or stoping the song
	def desligaMusica(self):
		#If song is playing
		if (self.parou == False):
			App.get_running_app().root.ids.login.musica.stop()
			self.parou = True
		else:
			App.get_running_app().root.ids.login.musica.play()
			self.parou = False

	def restart(self):
		App.get_running_app().root.ids.perguntas.nextpergunta()
		App.get_running_app().root.current = 'perguntas'
