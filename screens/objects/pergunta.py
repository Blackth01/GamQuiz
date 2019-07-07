# coding: utf-8

#Model for each question
class Pergunta(object):
	def __init__(self):
		self.texto = None
		self.resposta = None
		self.alt_A = None
		self.alt_B = None
		self.alt_C = None
		self.alt_D = None
		self.tipo = None
