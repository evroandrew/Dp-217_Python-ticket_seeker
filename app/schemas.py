from marshmallow import Schema, fields, validate, EXCLUDE


class TicketSchema(Schema):
    departure_id = fields.String(required=True)
    arrival_id = fields.String(required=True)
    date = fields.Date(required=True, format='%Y-%m-%d')
    type = fields.String(required=True, validate=validate.OneOf(['bus', 'train']))

    class Meta:
        ordered = True
        unknown = EXCLUDE


class StationSchema(Schema):
    search_string = fields.String(required=True)
    type = fields.String(required=True)

    class Meta:
        ordered = True
        unknown = EXCLUDE
