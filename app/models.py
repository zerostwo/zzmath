from app.extensions import db


class User(db.Model):
    __tablename__ = "userModel"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    userName = db.Column(db.String(16), unique=True)
    userDescription = db.Column(db.String(128), nullable=True)
    userID = db.Column(db.String(16))

    def save(self):
        db.session.add(self)
        db.session.commit()
