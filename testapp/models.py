from app import db


class Page(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(32), unique=True)
    text = db.Column(db.Text)
