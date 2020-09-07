#
#   Created by Voronov Vadim
#


from flask import render_template, request, abort, redirect, url_for

from app import app
from app import post_services
from app import images_services

import logging


@app.route("/", methods=["GET"])
def home():
    try:
        posts = post_services.get_posts()
        return render_template("home.html", posts=posts)
    except Exception as e:
        logging.exception(e)
        abort(500)


@app.route("/create-post", methods=["GET", "POST"])
def create_post():
    try:
        if request.method == 'POST':
            title = request.form.get("title")
            text = request.form.get("text")
            image_filename = None
            if 'image' in request.files:
                image_filename = images_services.save(request.files['image'])
            if title and text:
                post_services.create_new_post(title, text, image_filename)
            else:
                abort(400)
        return render_template("create_post.html")
    except Exception as e:
        logging.exception(e)
        abort(500)


@app.route("/delete-post", methods=["GET"])
def delete_post():
    try:
        post_id = request.args.get("id", type=int)
        if post_id is None:
            abort(400)
        post_services.try_delete(post_id)
        return redirect(url_for('home'))
    except Exception as e:
        logging.exception(e)
        abort(500)
