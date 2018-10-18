# -*- coding: utf-8 -*-
from django.test import TestCase
from django.test import RequestFactory
from django.test import Client
from cmcjsonsec.lib.encoder import CMCEncoder
from cmcjsonsec.lib.decoder import CMCDecoder

import json

class ClassesTest(TestCase):

	def setUp(self):
		self.client = Client()
		self.json_data = {
			'id': 1,
			'name': 'zacarias',
		}

	def test_class_exists(self):
		classe = CMCEncoder()
		self.assertEqual(classe, classe)

	def test_encode_decode_ok(self):
		enc = CMCEncoder()
		dec = CMCDecoder()
		encoded = enc.encode(self.json_data)
		decoded = dec.decode(encoded)
		self.assertEqual(encoded.status_code, 200)
		self.assertEqual(decoded, self.json_data)

	def test_encode_decode_response_ok(self):
		enc = CMCEncoder()
		dec = CMCDecoder()
		encoded = enc.encode(self.json_data)
		decoded = dec.decode_response(encoded)
		print('----------------------------------------2')
		print(decoded.content)
		#self.assertEqual(encoded.status_code, 200)
		#self.assertEqual(decoded, self.json_data)		