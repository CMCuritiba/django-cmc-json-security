# coding=utf-8

from django.conf import settings
from django.http import HttpResponse

import jwt
import json

from rest_framework import views
from rest_framework.response import Response

#---------------------------------------------------------------------------------------------
# Classe responsável por codificar o JSON
#---------------------------------------------------------------------------------------------
class CMCDecoder():

	def __init__(self):
		self.key = settings.CMC_ENCDEC_KEY

	def decode(self, encoded_data):
		try:
			result_json = json.loads(encoded_data.content.decode('utf-8'))
			token = result_json['token']
			return jwt.decode(token, self.key, algorithms=['HS256'])
		except:
			return {'erro': 'Não foi possível decodificar o token.'}

	def decode_response(self, encoded_data):
		retorno = self.decode(encoded_data)
		return HttpResponse(
			json.dumps(retorno),
			status=200
		)