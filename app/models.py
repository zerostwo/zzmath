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
    __tablename__ = "changeLog"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    date = db.Column(db.String(16))
    version = db.Column(db.String(16))
    status = db.Column(db.String(16))
    description = db.Column(db.String(128))


class Feedback(BaseModel):
    __tablename__ = "feedback"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    contact_details = db.Column(db.String(1000))
    description = db.Column(db.String(1000))
    is_resolved = db.Column(db.String(1000), default = "未解决")

# 主页/高考/数学/数学相关专栏排名，目前排名第二的宋冰的菠萝斑马居住指南，其内容与数学无关。
# QQ:984552746
