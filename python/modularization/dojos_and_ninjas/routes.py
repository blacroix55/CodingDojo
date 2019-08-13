from config import app
from controller_functions import index, user_create, create_dojo

app.add_url_rule("/","index", view_func=index)
app.add_url_rule("/users/create", "/user/create", view_func=user_create, methods=["POST"])
app.add_url_rule("/dojos/create", "create_dojo", view_func=create_dojo, methods=["POST"])
