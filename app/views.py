import json
from flask import request, Response
from app import app
from . import services


@app.route('/search', methods=['POST'])
def get_tickets():
    request_data = request.get_json(force=True)

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

    return json.dumps(tickets)


@app.route('/stations')
def get_stations():
    pass



