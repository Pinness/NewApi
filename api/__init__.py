from flask import Flask
#import the differnt view created
from flask_restx import Api
from .orders.views import order_namespace
from .auth.views import auth_namespace
from .quiz.views import quiz_namespace
from .config.config import config_dict
from .utils import db
#from .models.orders import Order
from .models.users import User
from .models.answer import Answer
from .models.category import Category
from .models.quiz import Quiz
from .models.user_response import UserResponse
from .models.question import Question
from flask_migrate import Migrate
from flask_jwt_extended import JWTManager



def create_app(config=config_dict['dev']):
    app = Flask(__name__)

    app.config.from_object(config)

    db.init_app(app)

    migrate = Migrate(app, db)

    api = Api(app)
    jwt = JWTManager(app)


    #api.add_namespace(order_namespace)  #before thre was / but gave error, research
    api.add_namespace(auth_namespace, path='/auth') 
    api.add_namespace(quiz_namespace, path='/quiz')

    @app.shell_context_processor
    def make_shell_context():
        return {
            'db':db,
            'User':User,
            'Quiz':Quiz

         }


    return app
