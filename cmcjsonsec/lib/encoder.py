# coding=utf-8

from django.conf import settings
from django.http import HttpResponse
from django.http import JsonResponse

import jwt
import json

from rest_framework import views
from rest_framework.response import Response

#---------------------------------------------------------------------------------------------
# Classe responsável por codificar o JSON
#---------------------------------------------------------------------------------------------
class CMCEncoder():

	def __init__(self):
		self.key = settings.CMC_ENCDEC_KEY

	def encode(self, json_data):
		try:
			encoded = jwt.encode(json_data, self.key, algorithm='HS256')
			jwt_token = {'token': encoded.decode('utf-8')}
			return HttpResponse(
				json.dumps(jwt_token),
				status=200,
				content_type="application/json"
			)
		except:
			return HttpResponse(
				{'erro': 'Erro ao codificar JSON.'},
				status=403,
				content_type="application/json"
			)
