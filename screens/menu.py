# coding: utf-8
from kivy.app import App
from kivy.uix.screenmanager import Screen
from kivy.clock import Clock
from kivy.uix.image import Image
from kivy.uix.popup import Popup

class Menu(Screen):
	def __init__(self, **kwargs):
		super(Menu, self).__init__(**kwargs)
		self.pop = Popup(title=' ', content=Image(source='Images/carregando.gif'), size_hint=(0.3, 0.3))

	def select_choice(self, dt):
		try:
			App.get_running_app().root.ids.perguntas.choice = self.choice
			App.get_running_app().root.ids.perguntas.getBanco()
			App.get_running_app().root.ids.perguntas.nextpergunta()
			App.get_running_app().root.current = 'perguntas'
		except:
			App.get_running_app().root.current = 'bugou'

	def proximo(self, choice):
		self.choice = choice
		self.pop.open()
		Clock.schedule_once(self.select_choice)
		self.pop.dismiss()
