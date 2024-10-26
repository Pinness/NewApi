from ..utils import db


class UserResponse(db.Model):
    __tablename__ = 'user_response'
    user_response_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    question_id = db.Column(db.Integer, db.ForeignKey('questions.question_id'), nullable=False)
    selected_answer_id = db.Column(db.Integer, db.ForeignKey('answers.answer_id'), nullable=False)
    is_correct = db.Column(db.Boolean, nullable=False)

    #created_at = db.Column(db.DateTime, default=datetime.datetime.utcnow)

    question = db.relationship('Question', back_populates='user_responses')
    selected_answer = db.relationship('Answer')
    user = db.relationship('User')


    def __repr__(self):
        return f'<User_Response {self.user_response}>'



