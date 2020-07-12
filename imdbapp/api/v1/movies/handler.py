from sanic import response,Blueprint
from .models import Movie

movie_views = Blueprint('v1_movies', url_prefix='/movies')

@movie_views.route("/")
def movie_list(request):
    products = [{"a":123}]
    return response.json(products)

