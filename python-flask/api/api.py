from flask import Blueprint
from flask_restful import Api
from api.resources.hello import Hello
from api.resources.category import CategoryResource
from api.resources.comment import CommentResource

api_bp = Blueprint('api', __name__)
api = Api(api_bp)

# Routes
api.add_resource(Hello, '/hello')
api.add_resource(CategoryResource, '/category')
api.add_resource(CommentResource, '/comment')