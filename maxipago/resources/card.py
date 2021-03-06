# coding: utf-8
from io import BytesIO 
from maxipago.utils import etree
from maxipago.resources.base import Resource
from maxipago.exceptions import CardException


class CardAddResource(Resource):

    def process(self):
        tree = etree.parse(BytesIO(self.data))

        error_code = tree.find('errorCode').text

        if error_code != '0':
            error_message = tree.find('errorMessage').text

            raise CardException(message=error_message, code=error_code)

        self._meta = {
            'command': tree.find('command').text,
            'time': tree.find('time').text,
        }

        self.token = tree.find('result').find('token').text


class CardDeleteResource(Resource):
    def process(self):
        tree = etree.parse(BytesIO(self.data))

        error_code = tree.find('errorCode').text

        if error_code != '0':
            error_message = tree.find('errorMessage').text

            raise CardException(message=error_message, code=error_code)

        self._meta = {
            'command': tree.find('command').text,
            'time': tree.find('time').text,
        }

        self.success = True
