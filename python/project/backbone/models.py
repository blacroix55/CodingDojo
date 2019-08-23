from sqlalchemy.sql import func
from config import app,db

routers_to_line_card_types = db.Table('routers_to_linecardtypes',
    db.Column('router_id', db.Integer, db.ForeignKey('routers.id'), primary_key=True),
    db.Column('router_type_id', db.Integer, db.ForeignKey('router_types.id'), primary_key=True))

class routers(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(45))
    model_id = db.Column(db.Integer, db.ForeignKey('router_types.id'))
    created_at = db.Column(db.DateTime, server_default=func.now())    
    updated_at = db.Column(db.DateTime, server_default=func.now(), onupdate=func.now())

class router_types(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    model = db.Column(db.String(45))
    num_slots = db.Column(db.Integer)
    created_at = db.Column(db.DateTime, server_default=func.now())    
    updated_at = db.Column(db.DateTime, server_default=func.now(), onupdate=func.now())

class linecard_types(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    model = db.Column(db.String(45))
    description = db.Column(db.String(255))
    # NOTE: need to model this better, but for the class project, just number of ports
    num_ports = db.Column(db.Integer)
    created_at = db.Column(db.DateTime, server_default=func.now())
    updated_at = db.Column(db.DateTime, server_default=func.now(), onupdate=func.now())

class interface_types(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    lineCard_id = db.Column(db.Integer, db.ForeignKey('linecard_types.id'))
    description = db.Column(db.String(80))
    speed = db.Column(db.Integer)
    created_at = db.Column(db.DateTime, server_default=func.now())
    updated_at = db.Column(db.DateTime, server_default=func.now(), onupdate=func.now())

class int_profile_types(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    description = db.Column(db.String(255))
    profile_type = db.Column(db.Integer)
    created_at = db.Column(db.DateTime, server_default=func.now())
    updated_at = db.Column(db.DateTime, server_default=func.now(), onupdate=func.now())
