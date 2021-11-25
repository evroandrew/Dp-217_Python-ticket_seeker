from marshmallow import Schema, fields, ValidationError, validate


class TicketSchema(Schema):
    departure_id = fields.String(required=True)
    arrival_id = fields.String(required=True)
    date = fields.Date(required=True)
    type = fields.String(required=True, validate=validate.OneOf(['bus', 'train']))
