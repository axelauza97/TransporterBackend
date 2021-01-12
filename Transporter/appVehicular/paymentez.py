import requests
import json
import time
import hashlib
from base64 import b64encode

def getSERVERtokenPaymentez():
    try:
        server_application_code = 'INNOVA-EC-SERVER'
        server_app_key = 'Y5FnbpWYtULtj1Muvw3cl8LJ7FVQfM'
        unix_timestamp = str(int(time.time()))
        uniq_token_string = server_app_key + unix_timestamp
        uniq_token_string = uniq_token_string.encode('utf-8')
        uniq_token_hash = hashlib.sha256(uniq_token_string).hexdigest()
        to_encode = '%s;%s;%s' % (server_application_code, unix_timestamp, uniq_token_hash)
        auth_token = b64encode(to_encode.encode('utf-8'))
        return auth_token
    except:
        return None


def getCLIENTtokenPaymentez():
    try:
        server_application_code = 'INNOVA-EC-CLIENT'
        server_app_key = 'ZjgaQCbgAzNF7k8Fb1Qf4yYLHUsePk'
        unix_timestamp = str(int(time.time()))
        print(unix_timestamp)
        uniq_token_string = server_app_key + unix_timestamp
        uniq_token_string = uniq_token_string.encode('utf-8')
        uniq_token_hash = hashlib.sha256(uniq_token_string).hexdigest()
        to_encode = '%s;%s;%s' % (server_application_code, unix_timestamp, uniq_token_hash)
        auth_token = b64encode(to_encode.encode('utf-8'))
        return auth_token
    except:
        return None


class Paymentez:
    def remove_card(self, token, uid):
        data = {}
        data['success'] = False
        auth_token = getSERVERtokenPaymentez()

        if auth_token == None:
            data['error'] = "auth_token no valido"
            return data

        header = {}
        header['Content-type'] = 'application/json'
        header['Auth-Token'] = auth_token.decode()

        dato = {'user': {'id': uid}, 'card': {'token': token}}
        response = requests.post('https://ccapi-stg.paymentez.com/v2/card/delete/', data=json.dumps(dato), headers=header)

        if response.status_code >= 400:
            data['error'] = "No se pudo hacer el request en Paymentez"
            return data

        data['success'] = True
        data['msg'] = response.text
        return data

    def add_card(self, dato):
        data = {}
        data['success'] = False
        auth_token = getCLIENTtokenPaymentez()
        if auth_token == None:
            data['error'] = "auth_token no valido"
            return data

        header = {}
        header['Content-type'] = 'application/json'
        header['Auth-Token'] = auth_token.decode()

        response = requests.post('https://ccapi-stg.paymentez.com/v2/card/add', headers=header, data=json.dumps(dato))

        if response.status_code >= 400:
            data['error'] = response.json().get("error")
            return data

        card = response.json().get('error')
        data['card_info'] = card
        data['success'] = True
        data['number'] = response.json().get('card').get('number')
        return data
    
    def list_cards(self, dato):
        data = {}
        data['success'] = False
        auth_token = getSERVERtokenPaymentez()
        if auth_token == None:
            data['error'] = "auth_token no valido"
            return data

        header = {}
        header['Content-type'] = 'application/json'
        header['Auth-Token'] = auth_token.decode()

        response = requests.get('https://ccapi-stg.paymentez.com/v2/card/list?uid='+dato, headers=header)
        print('https://ccapi-stg.paymentez.com/v2/card/list?uid='+dato)
        if response.status_code >= 400:
            data['error'] = response.json().get("error")
            return data

        card = response.json().get('error')
        data['card_info'] = card
        data['success'] = True
        data['cards'] = response.json().get('cards')
        return data
    
    def pay_card(self, dato):
        data = {}
        data['success'] = False
        auth_token = getSERVERtokenPaymentez()
        if auth_token == None:
            data['error'] = "auth_token no valido"
            return data

        header = {}
        header['Content-type'] = 'application/json'
        header['Auth-Token'] = auth_token.decode()

        response = requests.post('https://ccapi-stg.paymentez.com/v2/transaction/debit/', headers=header, data=json.dumps(dato))

        if response.status_code >= 400:
            data['error'] = response.json().get("error")
            return data

        card = response.json().get('error')
        data['card_info'] = card
        data['success'] = True
        data['transaction'] = response.json().get('transaction')
        return data