from sanic import response,Blueprint

user_views = Blueprint('v1_users', url_prefix='/users')

@user_views.route("/")
def home(request):
    products = [{"user":123}]
    return response.json(products)

