# coding: utf-8
from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from screens import Login, Menu, Top10, Terminou, Perguntas, Creditos
from screens.inputs import NormalOnly


class Gerenciador(ScreenManager):
	pass

class Errou(Screen):
	pass

class Acertou(Screen):
	pass

class Bugou(Screen):
	pass


class Main(App):
	def build(self):
		return Gerenciador()

Main().run()
