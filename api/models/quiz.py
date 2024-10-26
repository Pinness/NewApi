from ..utils import db
from enum import Enum
from datetime import datetime


class Quiz(db.Model):
    __tablename__ = 'quizzes'
    quiz_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    quiz_title = db.Column(db.String(100), nullable=False, unique=True)
    quiz_description = db.Column(db.Text)
    category_id = db.Column(db.Integer, db.ForeignKey("categories.category_id"), nullable=False)
    created_by = db.Column(db.Integer, db.ForeignKey('users.id'))
    difficulty_level = db.Column(db.String(50))  # Example: "Easy", "Medium", "Hard"
    time_limit = db.Column(db.Integer)  # In seconds

    #created_at = db.Column(db.DateTime, default=datetime.datetime.utcnow)

    category = db.relationship('Category', back_populates='quizzes')
    questions = db.relationship('Question', back_populates='quiz')

    def __repr__(self):
        return f'<Quiz {self.quiz_title}>'