from app import app, db


if __name__ == '__main__':
    print("-- starting app --")
    db.create_all()
    app.run("localhost", port=5000)
