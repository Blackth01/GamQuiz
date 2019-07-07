# coding: utf-8
from kivy.app import App
from kivy.uix.textinput import TextInput


class NormalOnly(TextInput):

	def insert_text(self, substring, from_undo=False):

		s = ''
		if (len(self.text) < 15):
			try:
				if (ord(substring) > 47 and ord(substring) < 58):
					s = substring
			except:
				pass
			try:
				if (ord(substring) > 64 and ord(substring) < 91):
					s = substring
			except:
				pass
			try:
				if (ord(substring) > 96 and ord(substring) < 123):
					s = substring
			except:
				pass
		return super(NormalOnly, self).insert_text(s, from_undo=from_undo)
