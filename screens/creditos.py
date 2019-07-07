# coding: utf-8
from kivy.app import App
from kivy.uix.screenmanager import Screen
from kivy.core.window import Window

class Creditos(Screen):
	def voltar(self):
		#Sets current screen to the last screen user has seen
		App.get_running_app().root.current = self.atual

	#Method to bind the "return" button
	def back(self, window, key, *args):
		if (key == 27):
			App.get_running_app().root.current = self.atual
			return True

	#Next methods are responsible for bind and unbind the "return" button
	def on_pre_enter(self):
		Window.bind(on_keyboard=self.back)
	def on_pre_leave(self):
		Window.unbind(on_keyboard=self.back)
