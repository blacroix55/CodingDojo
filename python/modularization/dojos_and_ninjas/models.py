from sqlalchemy.sql import func
from config import db

class User(db.Model):	
    # __tablename__ = "users"    # optional	- if not specified, will user class name as table name.
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(45))
    last_name = db.Column(db.String(45))
    #dojo_id is the FK, pointing to Dojo.id; one dojo may have many users (one-to-many)
    dojo_id = db.Column(db.Integer, db.ForeignKey('dojo.id'), nullable=False)
    created_at = db.Column(db.DateTime, server_default=func.now())    # notice the extra import statement above
    updated_at = db.Column(db.DateTime, server_default=func.now(), onupdate=func.now())

class Dojo(db.Model):	
    # __tablename__ = "users"    # optional	- if not specified, will user class name as table name.
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(45))
    city = db.Column(db.String(45))
    state = db.Column(db.String(45))
    created_at = db.Column(db.DateTime, server_default=func.now())    # notice the extra import statement above
    updated_at = db.Column(db.DateTime, server_default=func.now(), onupdate=func.now())