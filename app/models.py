from app.extensions import db


class BaseModel(db.Model):
    __abstract__ = True
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)

    def save(self):
        try:
            db.session.add(self)
            db.session.commit()
            return True
        except Exception as e:
            print(e)
            return False

    def delete(self):
        try:
            db.session.delete(self)
            db.session.commit()
            return True
        except Exception as e:
            print(e)
            return False


class User(BaseModel):
    __tablename__ = "userModel"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    userName = db.Column(db.String(16), unique=True)
    userDescription = db.Column(db.String(128), nullable=True)
    userID = db.Column(db.String(16))


class ChangeLog(BaseModel):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    date = db.Column(db.String(16))
    version = db.Column(db.String(16))
    status = db.Column(db.String(16))
    description = db.Column(db.String(128))


class Feedback(BaseModel):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    contact_details = db.Column(db.String(20))
    description = db.Column(db.String(128))
