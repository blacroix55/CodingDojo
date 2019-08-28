from sqlalchemy.sql import func
from config import app,db

## ALL COMPONENTS TO CREATE A ROUTER HERE:

class router_types(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    model = db.Column(db.String(45))
    num_slots = db.Column(db.Integer)
    created_at = db.Column(db.DateTime, server_default=func.now())    
    updated_at = db.Column(db.DateTime, server_default=func.now(), onupdate=func.now())
    router_type = db.relationship('routers', 
        backref=db.backref('router_type')
    )

class interface_types(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    linecard_id = db.Column(db.Integer, db.ForeignKey('linecard_types.id'))
    description = db.Column(db.String(80))
    speed = db.Column(db.Integer)
    created_at = db.Column(db.DateTime, server_default=func.now())
    updated_at = db.Column(db.DateTime, server_default=func.now(), onupdate=func.now())

class int_profile_types(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    description = db.Column(db.String(255))
    profile_type = db.Column(db.Integer)
    created_at = db.Column(db.DateTime, server_default=func.now())
    updated_at = db.Column(db.DateTime, server_default=func.now(), onupdate=func.now())

#association
class routers_linecards(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    router_id = db.Column(db.Integer,db.ForeignKey('routers.id'))
    linecard_type_id = db.Column(db.Integer, db.ForeignKey('linecard_types.id'))
    router_slot = db.Column(db.Integer)
    created_at = db.Column(db.DateTime, server_default=func.now())    
    updated_at = db.Column(db.DateTime, server_default=func.now(), onupdate=func.now())
    router_with_linecard = db.relationship("linecard_types", back_populates="routers_with_linecard")    # parent
    linecard_installed = db.relationship("routers", back_populates="linecards_installed")               # child

#parent  (LEFT)
class routers(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(45))
    created_at = db.Column(db.DateTime, server_default=func.now())    
    updated_at = db.Column(db.DateTime, server_default=func.now(), onupdate=func.now())
    router_type_id = db.Column(db.Integer, db.ForeignKey('router_types.id'))
    linecards_installed = db.relationship('routers_linecards', back_populates='linecard_installed')     # association

#child  (RIGHT)
class linecard_types(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    model = db.Column(db.String(45))
    description = db.Column(db.String(255))
    num_ports = db.Column(db.Integer)
    created_at = db.Column(db.DateTime, server_default=func.now())    
    updated_at = db.Column(db.DateTime, server_default=func.now(), onupdate=func.now())
    routers_with_linecard = db.relationship('routers_linecards', back_populates='router_with_linecard') # association

