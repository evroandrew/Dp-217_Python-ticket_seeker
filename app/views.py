import json
import redis
import os
from flask import request, Response
from app import app
from . import services
from .schemas import TicketSchema, StationSchema


@app.route('/tickets', methods=['POST'])
def get_tickets():
    request_data = request.get_json(force=True)
    validation_err = TicketSchema().validate(request_data)
    if validation_err:
        return Response(validation_err, status=400)

    deserialized = TicketSchema().load(request_data)
    serialized = TicketSchema().dumps(deserialized)

    store = redis.Redis(os.environ.get('REDIS_URL'))

    if store.exists(serialized):
        return store.get(serialized)

    departure = request_data['departure_id']
    arrival = request_data['arrival_id']
    date = request_data['date']
    tickets_type = request_data['type']

    if tickets_type == 'train':
        tickets = services.get_train_tickets(departure, arrival, date).json()
    elif tickets_type == 'bus':
        tickets = services.get_bus_tickets(departure, arrival, date).json()
    else:
        return Response('Unknown tickets type', status=400)

    tickets_json = json.dumps(tickets)
    store.setex(serialized, 30, tickets_json)

    return tickets_json


@app.route('/stations', methods=['POST'])
def get_stations():
    request_data = request.get_json(force=True)

    store = redis.Redis(os.environ.get('REDIS_URL'))

    deserialized = StationSchema().load(request_data)
    serialized = StationSchema().dumps(deserialized)

    if store.exists(serialized):
        return store.get(serialized)

    station_type = request_data['type']
    search_string = request_data['search_string']

    stations = services.get_stations(search_string, station_type).json()

    if not stations:
        return Response(status=400)

    stations_json = json.dumps(stations)
    store.setex(serialized, 300, stations_json)

    return json.dumps(stations)


