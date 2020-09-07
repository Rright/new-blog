#
#   Created by Voronov Vadim
#


from app.db_models import Post
from app import db


def create_new_post(title, text, image):
    post = Post(title=title, text=text, image=image)
    db.session.add(post)
    db.session.commit()


def get_posts():
    posts = Post.query.order_by(Post.created_on.desc()).all()
    return posts


def try_delete(post_id):
    post = Post.query.filter_by(id=post_id).first()
    if not post:
        return
    db.session.delete(post)
    db.session.commit()
