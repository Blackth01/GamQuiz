# coding: utf-8
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.screenmanager import Screen
from kivy.properties import StringProperty
from kivy.core.window import Window

class Top10(Screen):
	def setTop10(self, opcao):
		#Gets the database instance from login screen class
		banco = App.get_running_app().root.ids.login.banco
		#If option == 1, it gets "All Time Top10" list, else, "Today Top10" list
		try:
			if (opcao == 1):
				jogador = banco.getTop10(1, App.get_running_app().root.ids.perguntas.choice)
			else:
				jogador = banco.getTop10(0, App.get_running_app().root.ids.perguntas.choice)

			#Next lines prepares the elements to be shown on screen
			self.ids.top1.jogador = jogador[0]["username"]
			self.ids.top2.jogador = jogador[1]["username"]
			self.ids.top3.jogador = jogador[2]["username"]
			self.ids.top4.jogador = jogador[3]["username"]
			self.ids.top5.jogador = jogador[4]["username"]
			self.ids.top6.jogador = jogador[5]["username"]
			self.ids.top7.jogador = jogador[6]["username"]
			self.ids.top8.jogador = jogador[7]["username"]
			self.ids.top9.jogador = jogador[8]["username"]
			self.ids.top10.jogador = jogador[9]["username"]

			self.ids.top1.pontuacao = str(jogador[0]["score"])
			self.ids.top2.pontuacao = str(jogador[1]["score"])
			self.ids.top3.pontuacao = str(jogador[2]["score"])
			self.ids.top4.pontuacao = str(jogador[3]["score"])
			self.ids.top5.pontuacao = str(jogador[4]["score"])
			self.ids.top6.pontuacao = str(jogador[5]["score"])
			self.ids.top7.pontuacao = str(jogador[6]["score"])
			self.ids.top8.pontuacao = str(jogador[7]["score"])
			self.ids.top9.pontuacao = str(jogador[8]["score"])
			self.ids.top10.pontuacao = str(jogador[9]["score"])
		except:
			App.get_running_app().root.current = 'bugou'

	def back(self, window, key, *args):
		if (key == 27):
			App.get_running_app().root.current = 'terminou'
			return True
	def on_pre_enter(self):
		Window.bind(on_keyboard=self.back)
	def on_pre_leave(self):
		Window.unbind(on_keyboard=self.back)


#Layout for each position, it is used in the main.kv file
class Colocacao(BoxLayout):
	tipo = StringProperty('x')
	posicao = StringProperty('x')
	jogador = StringProperty('x')
	pontuacao = StringProperty('x')
