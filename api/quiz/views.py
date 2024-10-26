from flask_restx import Resource, Namespace

quiz_namespace = Namespace('quizzes', description = 'Namespace for quiz')

@quiz_namespace.route('/quiz')
class QuizGetCretae(Resource):
    """
        Resource for retrieving and creating quizzes
    """

    def get(self):
        """
            This endpoint retrieves all available quizzes from database
        """
        pass

    def post(self):
        """
            Create a new quiz in the database
        """
        pass


@quiz_namespace.route('/quiz/<int:quiz_id>')
class GetUpdateDelete(Resource):
    """
        Resource for retrieving, updating, and deleting a specific quiz
    """

    def get(self, quiz_id):
        """
            Retrieve a quiz by id
        """

        pass

    
    def put(self, quiz_id):
        """
            Update a quiz by id
        """

        pass


    def delete(self, quiz_id):
        """
            Delete a quiz by id
        """

        pass
