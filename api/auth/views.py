from flask_restx import Namespace, Resource, fields
from flask import request
from ..models.users import User
from werkzeug.security import generate_password_hash, check_password_hash
from http import HTTPStatus
from flask_jwt_extended import create_access_token, create_refresh_token, jwt_required, get_jwt_identity


auth_namespace = Namespace('auth', description = "a namespace for authentication")


signup_model = auth_namespace.model(
    'SignUp', {
        'id': fields.Integer(),
        'username': fields.String(required=True, description = 'A username'),
        'email': fields.String(required=True, description = 'An email'),
        'password': fields.String(required=True, description = 'A password'),

    }
)


user_model = auth_namespace.model(
    'User', {
        'id': fields.Integer(),
        'username': fields.String(required=True, description = 'A username'),
        'email': fields.String(required=True, description = 'An email'),
        'password_hash': fields.String(required=True, description = 'A password'),
        'Is_active': fields.Boolean(description="This shows that User is active"),
        'Is_Admin': fields.Boolean(description="This shows that User is Admin")
    }
)


login_model = auth_namespace.model(
    'Login', {
        'email': fields.String(required=True, description="An email"),
        'password': fields.String(required=True, description="A password")
    }
)



#@auth_namespace.route('/')
#lass HelloAuth(Resource):

  #  def get(self):
   #     return {"message":"hello Auth"}

@auth_namespace.route('/signup')
class Signup(Resource):

    @auth_namespace.expect(signup_model)
    @auth_namespace.marshal_with(user_model)

    def post(self):
        """
            Create a new user account

        """
        data = request.get_json()

        new_user = User(
            username=data.get('username'),
            email=data.get('email'),
            password_hash=generate_password_hash(data.get('password'))
        )


        new_user.save()

        return new_user, HTTPStatus.CREATED



@auth_namespace.route('/login')
class Login(Resource):

    @auth_namespace.expect(login_model)
    def post(self):
        """
            Create a JWT pair
        """

        data = request.get_json()

        #check if user exists
        email = data.get('email')
        password = data.get('password')

        user = User.query.filter_by(email=email).first()

        if (user is not None) and check_password_hash(user.password_hash, password):
            access_token = create_access_token(identity = user.username)
            refresh_token = create_refresh_token(identity = user.username)

            response = {
                'access_token': access_token,
                'refresh_token': refresh_token
            }

            return response, HTTPStatus.OK
        
@auth_namespace