from config import app
from controller_functions import *


# HOME PAGE
app.add_url_rule("/", view_func=index)

# ROUTER TYPES
app.add_url_rule("/router_types/index", view_func=router_types_index, methods=["POST"])
app.add_url_rule("/router_type/add", view_func=router_type_add, methods=["POST"])
app.add_url_rule("/router_type/delete/<int:router_type_id>", view_func=router_type_delete, methods=["POST"])

# LINECARD TYPES
app.add_url_rule("/linecard_types/index", view_func=linecard_types_index, methods=["POST"])
app.add_url_rule("/linecard_type/add", view_func=linecard_type_add, methods=["POST"])
app.add_url_rule("/linecard_type/delete/<int:linecard_type_id>", view_func=linecard_type_delete, methods=["POST"])

# INTERFACE TYPES
app.add_url_rule("/interface_types/index", view_func=interface_types_index, methods=["POST"])
app.add_url_rule("/interface_type/add", view_func=interface_type_add, methods=["POST"])
app.add_url_rule("/interface_type/delete/<int:interface_type_id>", view_func=interface_type_delete, methods=["POST"])

# INT_PROFILE TYPES
app.add_url_rule("/int_profile_types/index", view_func=int_profile_types_index, methods=["POST"])
app.add_url_rule("/int_profile_type/add", view_func=int_profile_types_add, methods=["POST"])
app.add_url_rule("/int_profile_type/delete/<int:int_profile_type_id>", view_func=int_profile_types_delete, methods=["POST"])

# ROUTERS 
app.add_url_rule("/select/device", view_func=select_device, methods=["POST"])
app.add_url_rule("/create/router", view_func=create_router, methods=["POST"])
app.add_url_rule("/delete/router/<int:router_id>", view_func=delete_router, methods=["POST"])

