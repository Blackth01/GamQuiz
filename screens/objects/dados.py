
# coding: utf-8
import requests
from pergunta import *

class Dados(object):
	def __init__(self):
		self.url = 'https://localhost/api.php'

	#Method responsible for getting random questions from the database
	def getRandom(self, choice):
		r = requests.post(url=self.url, data={'opcao': 6, 'escolha1': choice})
		lista = r.json()
		#List of questions
		questions = []

		for pergunta in lista:
			#Creates a new "Pergunta" instance
			perg = Pergunta()
			perg.texto = pergunta['texto']
			perg.resposta = pergunta['resposta']
			perg.alt_A = pergunta['alt_A']
			perg.alt_B = pergunta['alt_B']
			perg.alt_C = pergunta['alt_C']
			perg.alt_D = pergunta['alt_D']
			perg.tipo = pergunta['tipo']
			print("Tipo: %s" % pergunta['tipo'])
			#Adds the question to the list
			questions.append(perg)

		return questions

	#Registers the new player
	def registraJogador(self, username, senha):
		r = requests.post(url=self.url, data={'opcao': 1, 'username': username, 'senha': senha})

		return r.json()['resposta']

	def login(self, username, senha):
		r = requests.post(url=self.url, data={'opcao': 2, 'username': username, 'senha': senha})
		token = r.json()['token']
		return token

	#Method responsible for setting user score
	def setPontos(self, username, token, score, choice):
		r = requests.post(url=self.url, data={'opcao': 5, 'username': username, 'token': token, 'score': score, 'escolha1': choice})

		return r.json()['resposta']

	def getPontos(self, username, escolha1):
		r = requests.post(url=self.url, data={'opcao': 8, 'username': username, 'escolha1': escolha1})
		pontuacao = [r.json()['todos'], r.json()['hoje']]
		return pontuacao
	#Method responsible for getting top10
	def getTop10(self, opcao, choice):
		r = requests.post(url=self.url, data={'opcao': 3, 'escolha1': choice, 'escolha2': opcao})
		jogadores = r.json()

		if (choice == 1):
			if (opcao == 1):
				param = 'pontos'
			else:
				param = 'pontos_hoje'
		else:
			if (opcao == 1):
				param = 'pontos_matematica'
			else:
				param = 'p_hoje_matematica'
		#Creates the list of players
		players = []
		for jogador in jogadores:
			#Creates a dictionary to store player information
			player = {'username':'null', 'score':0}
			player['username'] = jogador['username']
			player['score'] = jogador[param]
			players.append(player)

		return players

	#Method responsible for getting player position
	def getColocacao(self, username, opcao, choice):
		r = requests.post(url=self.url, data={'opcao': 4, 'username': username, 'escolha1': choice, 'escolha2': opcao})
		colocacao = int(r.json()['colocacao'])
		return colocacao+1

	#Method responsible for checking if there is an update
	def getUpdate(self):
		r = requests.post(url=self.url, data={'opcao': 7})
		versao = r.json()['versao']

		versao = float(versao)
		if (versao > 1.2):
			update = 1
		else:
			update = 0

		return update

