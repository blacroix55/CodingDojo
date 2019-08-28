from flask import render_template, request, redirect
from config import db
from models import *

###################
#
# General tools, used throughout the application

def consoleMsg(msg):
    print('*'*80)
    print(msg)

def linecard_list(router_id):
    # Get current router + current router's installed linecards
    router = routers.query.get(router_id)

    # Build out a blank list-of-dictionaries structure for the current router, based on number of linecard slots available
    print ("building linecard_list")
    linecard_list=[]
    for i in range(router.router_type.num_slots):
        print ('appending list')
        linecard_list.append({})
    
    # Iterate through current linecards, updating the dict entry for the linecard based on it's index
    print ('iterating through cur_rtr.linecards_installed', router.linecards_installed)
    for linecard in router.linecards_installed:
        linecard_list[linecard.router_slot]={
            'linecard_type_id': linecard.linecard_type_id,
            'router_linecard_id': linecard.id
        }

    # print results
    print (linecard_list)
    return linecard_list

###################
#
# Main page stuffs

def index():
    consoleMsg('User landed on home page')
    data=routers.query.all()
    print ("Router list:",data)
    return render_template("index.html", routers=data)

def router_search():
    consoleMsg('User doing search query')
    q=request.form['search_data']+"%%"
    data=routers.query.filter(routers.name.like(q))
    rtr_types=router_types.query.all()
    print ("Router list:",data)
    return render_template("partial/router_index.html", routers=data,rtr_types=rtr_types)



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

def router_index():
    consoleMsg('User router index')
    # Routers, needs to be in nested if statement eventually
    data=routers.query.all()
    rtr_types=router_types.query.all()
    print ("Router list:",data)
    print ("router types:",rtr_types)
    return render_template("partial/router_index.html", routers=data, rtr_types=rtr_types )

def router_add():
    consoleMsg('User requested to create new router')
    print(request.form)
    # Add new router
    router= routers(
        name=request.form['name'],
        router_type_id=request.form['router_type_id']
    )
    db.session.add(router)
    db.session.commit()
    # Get updated router list
    data=routers.query.all()
    rtr_types=router_types.query.all()
    print ("Router list:",data)
    return render_template("partial/router_index.html", routers=data, rtr_types=rtr_types)

def router_delete(router_id):
    consoleMsg('User requested to delete router with router_id of'+str(router_id))
    # Delete router
    router_to_delete = routers.query.get(router_id)
    db.session.delete(router_to_delete)
    db.session.commit()
    # Get updated router list
    data=routers.query.all()
    rtr_types=router_types.query.all()
    return render_template("partial/router_index.html", routers=data, rtr_types=rtr_types)

def router_edit(router_id):
    consoleMsg('User requested to edit router with router_id of '+str(router_id))
    # Get router data
    data = routers.query.get(router_id)
    rtr_types=router_types.query.all()
    lc_types=linecard_types.query.all()
    current_linecards=linecard_list(router_id)

    return render_template("partial/router_edit.html", router=data,rtr_types=rtr_types,linecard_types=lc_types, current_linecards=current_linecards)

def router_update(router_id):
    consoleMsg('User requested to UPDATE router with router_id of '+str(router_id))
    
    # Snag current database entries for this router + which linecards are in it, convert to dict of dicts, keyed by router_slot
    current_cards=linecard_list(router_id)

    # Go through request form, compare to current cards, update/delete as needed
    print ("request form =",request.form)
    print ("starting to process request form for update")

    # NEED TO ADD SECTION TO ALLOW FOR UPDATING OF ROUTER NAME AND ROUTER TYPE, WHICH IS ALREADY PASSED IN VIA REQUEST.FORM

    for key,value in request.form.items():
        if 'slot' in key:
            slot=int(key[5:])
            if value == "None":
                new_linecard_type_id=None
            else:
                new_linecard_type_id=int(value)
            print("-"*40)
            print ("comparing slot number:",slot, type(slot))
            print ("new card:",new_linecard_type_id, type(new_linecard_type_id))
            try:
                old_linecard_type_id=current_cards[slot]['linecard_type_id']
            except:
                old_linecard_type_id=None
            print ("old card:",old_linecard_type_id, type(old_linecard_type_id))

            if new_linecard_type_id == old_linecard_type_id:
                print ("old and new cards are the same, no db updates needed")
            elif new_linecard_type_id == None :
                print ("need to delete old card")
                data=routers_linecards.query.get(current_cards[slot]['router_linecard_id'])
                print ("router_linecard row to delete =",data)
                db.session.delete(data)
                db.session.commit()
            elif old_linecard_type_id == None: 
                print ("adding new router_linecard entry")
                data=routers_linecards(
                    router_id=router_id,
                    linecard_type_id=new_linecard_type_id,
                    router_slot=slot
                )
                print (data)
                db.session.add(data)
                db.session.commit()
            else:
                print ("updating existing router_linecard entry")
                router_linecard_id=current_cards[slot]['router_linecard_id']
                print("\n\n router_linecard_id =",router_linecard_id)
                data=routers_linecards.query.get(router_linecard_id)
                data.linecard_type_id=new_linecard_type_id
                db.session.commit()
            
    # Snagging current DB info to re-populate content window
    data = routers.query.get(router_id)
    print ("data = ",data.__dict__)
    rtr_types=router_types.query.all()
    lc_types=linecard_types.query.all()
    current_linecards=linecard_list(router_id)

    return render_template("partial/router_edit.html", router=data,rtr_types=rtr_types,linecard_types=lc_types,current_linecards=current_linecards)