#
#   Created by Voronov Vadim
#


from app import db
from datetime import datetime


class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(255), nullable=False)
    text = db.Column(db.Text(), nullable=False)
    image = db.Column(db.String(255), nullable=True)
    created_on = db.Column(db.DateTime, default=datetime.now)

    def __init__(self, title: str, text: str, image=None):
        self.title = title
        self.text = text
        self.image = image

    @property
    def string_created_on(self):
        return self.created_on.strftime("%d %b %Y %H:%M:%S")

    def __str__(self):
        return "<Post {}> {}".format(self.id, self.title)

    def __repr__(self):
        return "<Post {}> {}".format(self.id, self.title)
