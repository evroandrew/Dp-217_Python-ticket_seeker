import json
import requests


def get_bus_tickets(departure, arrival, date) -> requests.Response:
    url = "https://de-prod-lb.cashalot.in.ua/rest/search/ubus"
    payload = {
        'departureCode': departure,
        'arrivalCode': arrival,
        'departureDate': date,
        'language': 'uk',
        'supplier': 'ubus_busfor',
        'transactionId': '02323r23r23r2',
    }
    headers = {
        'content-type': 'application/json',
        'language': 'uk',
        'transactionid': '02323r23r23r2'
    }
    tickets = requests.request("POST",
                               url,
                               headers=headers,
                               data=json.dumps(payload))
    return tickets


def get_train_tickets(departure, arrival, date) -> requests.Response:
    url = "https://de-prod-lb.cashalot.in.ua/rest/supplier/search"
    payload = {
        'departureCode': departure,
        'arrivalCode': arrival,
        'departureDate': date,
        'language': 'uk',
        'supplier': 'uz_train',
        'transactionId': 'n343h3434343',
    }
    headers = {
        'language': 'uk',
        'supplier': 'uz_train',
        'content-type': 'application/json'
    }
    tickets = requests.request("POST",
                               url,
                               headers=headers,
                               data=json.dumps(payload))
    return tickets


def get_train_stations():
    pass


def get_bus_stations():
    pass
