from ..utils import db


class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer(), primary_key=True)
    username = db.Column(db.String(45), nullable=False, unique=True)
    email = db.Column(db.String(50), nullable=False, unique=True)
    password_hash = db.Column(db.Text(), nullable=False)
    Is_admin = db.Column(db.Boolean(), default=False)
    Is_active = db.Column(db.Boolean(), default=False)

    #created_at = db.Column(db.DateTime, default=datetime.datetime.utcnow)

    def __repr__(self):
        return f"<User {self.id} {self.username}>"

    
    def save(self):
        db.session.add(self)
        db.session.commit()
