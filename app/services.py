import json
import requests


def get_bus_tickets(departure, arrival, date) -> requests.Response:
    url = 'https://de-prod-lb.cashalot.in.ua/rest/search/ubus'
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
    url = 'https://de-prod-lb.cashalot.in.ua/rest/supplier/search'
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


def get_stations(search_string, station_type):
    if station_type == 'train':
        url = 'https://de-prod-lb.cashalot.in.ua/rest/stations/express'
        supplier = 'uz_train'
    elif station_type == 'bus':
        url = 'https://de-prod-lb.cashalot.in.ua/rest/stations/bus'
        supplier = 'ubus_busfor'
    else:
        return

    payload = {
        'language': 'uk',
        'supplier': supplier,
        'query': search_string
    }
    headers = {
        'language': 'uk',
        'supplier': supplier,
        'content-type': 'application/json'
    }
    stations = requests.request("POST",
                                url,
                                headers=headers,
                                data=json.dumps(payload))
    return stations
