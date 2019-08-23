from flask import render_template, request, redirect
from config import db
from models import *

def consoleMsg(msg):
    print('*'*80)
    print(msg)

def index():
    consoleMsg('User landed on home page')
    data=routers.query.all()
    return render_template("index.html", routers=data)

def generic_index(db_table,html_file):
    consoleMsg('testing generic index for '+db_table+" table")
    data=db_table.query.all()
    print(data)
    return render_template("partial/"+html_file+".html", router_types=data)


###################
#
#   THE FOLLOWING SECTION IS FOR CREATING AND DELETING OF ROUTER_TYPES

def router_types_index():
    consoleMsg('User requested to go to router_type index page')
    data=router_types.query.all()
    print(data)
    return render_template("partial/router_types_index.html", router_types=data)

def router_type_add():
    consoleMsg('User requested to add router_type')
    data = router_types(
        model=request.form['model'],
        num_slots=request.form['num_slots']
    )
    print (data)
    db.session.add(data)
    db.session.commit()
    data=router_types.query.all()
    print(data)
    return render_template("partial/router_types_index.html", router_types=data)
     
def router_type_delete(router_type_id):
    consoleMsg('User requested to delete router_type with id of'+str(router_type_id))
    # Delete router_type
    data = router_types.query.get(router_type_id)
    db.session.delete(data)
    db.session.commit()
    # Get updated router_type list
    data=router_types.query.all()
    print(data)
    return render_template("partial/router_types_index.html", router_types=data)

###################
#
#   THE FOLLOWING SECTION IS FOR CREATING AND DELETING OF LINECARD TYPES

def linecard_types_index():
    consoleMsg('User requested to go to linecard type index page')
    data=linecard_types.query.all()
    print(data)
    return render_template("partial/linecard_types_index.html", linecard_types=data)

def linecard_type_add():
    consoleMsg('User requested to add linecard_type')
    data = linecard_types(
        model=request.form['model'],
        num_ports=request.form['num_ports'],
        description=request.form['description']
    )
    print (data)
    db.session.add(data)
    db.session.commit()
    data=linecard_types.query.all()
    print(data)
    return render_template("partial/linecard_types_index.html", linecard_types=data)

def linecard_type_delete(linecard_type_id):
    consoleMsg('User requested to delete linecard_type with id of'+str(linecard_type_id))
    # Delete linecard_type_id
    data = linecard_types.query.get(linecard_type_id)
    db.session.delete(data)
    db.session.commit()
    # Get updated linecard_type list
    data=linecard_types.query.all()
    print(data)
    return render_template("partial/linecard_types_index.html", linecard_types=data)

###################
#
#   THE FOLLOWING SECTION IS FOR CREATING AND DELETING OF INTERFACE_TYPES

def interface_types_index():
    consoleMsg('User requested to go to router_type index page')
    data=interface_types.query.all()
    print(data)
    return render_template("partial/interface_types_index.html", interface_types=data)

def interface_type_add():
    consoleMsg('User requested to add linecard_type')
    data = interface_types(
        description=request.form['phy_conn'],
        speed=request.form['speed']
    )
    print (data)
    db.session.add(data)
    db.session.commit()
    data=interface_types.query.all()
    print(data)
    return render_template("partial/interface_types_index.html", interface_types=data)

def interface_type_delete(interface_type_id):
    consoleMsg('User requested to delete linecard_type with id of'+str(interface_type_id))
    # Delete interface_type_id
    data = interface_types.query.get(interface_type_id)
    db.session.delete(data)
    db.session.commit()
    # Get updated linecard_type list
    data=interface_types.query.all()
    print(data)
    return render_template("partial/interface_types_index.html", interface_types=data)

###################
#
#   THE FOLLOWING SECTION IS FOR CREATING AND DELETING OF INT_PROFILE_TYPES

def int_profile_types_index():
    consoleMsg('User requested to go to int_profile_type index page')
    data=int_profile_types.query.all()
    print(data)
    return render_template("partial/int_profile_types_index.html", int_profile_types=data)

def int_profile_types_add():
    consoleMsg('User requested to add int_profile_type')
    data = int_profile_types(
        description=request.form['description'],
        profile_type=request.form['profile_type']
    )
    print (data)
    db.session.add(data)
    db.session.commit()
    data=int_profile_types.query.all()
    print(data)
    return render_template("partial/int_profile_types_index.html", int_profile_types=data)

def int_profile_types_delete(int_profile_type_id):
    consoleMsg('User requested to delete int_profile_type with id of'+str(int_profile_type_id))
    # Delete interface_type_id
    data = int_profile_types.query.get(int_profile_type_id)
    db.session.delete(data)
    db.session.commit()
    # Get updated linecard_type list
    data=int_profile_types.query.all()
    print(data)
    return render_template("partial/int_profile_types_index.html", int_profile_types=data)


###################
#
#   THE FOLLOWING SECTION IS FOR CREATING AND DELETING OF ROUTERS

def select_device():
    consoleMsg('User selected device type from main pulldown menu')
    # Routers, needs to be in nested if statement eventually
    router_list=routers.query.all()
    print ("Router list:",router_list)
    return render_template("partial/router-main.html", routers=router_list)

def create_router():
    consoleMsg('User requested to create new router')
    # Add new router
    router= routers(
        name=request.form['router_name']
    )
    db.session.add(router)
    db.session.commit()
    # Get updated router list
    router_list=routers.query.all()
    return render_template("partial/router-main.html", routers=router_list)

def delete_router(router_id):
    consoleMsg('User requested to delete router with router_id of'+str(router_id))
    # Delete router
    router_to_delete = routers.query.get(router_id)
    db.session.delete(router_to_delete)
    db.session.commit()
    # Get updated router list
    router_list=routers.query.all()
    return render_template("partial/router-main.html", routers=router_list)