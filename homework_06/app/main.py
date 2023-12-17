from os import getenv

from flask import Flask, request, render_template
from flask_migrate import (
    Migrate,
    migrate as migrate_command,
    upgrade as upgrade_command,
)
from views.posts import posts_app
from views.users import users_app
from models import db

app = Flask(__name__)
app.register_blueprint(posts_app)
app.register_blueprint(users_app)

CONFIG_NAME = getenv("CONFIG_NAME", "DevelopmentConfig")
app.config.from_object(f"config.{CONFIG_NAME}")

db.init_app(app)
migrate = Migrate(app, db)


def create_migration():
    with app.app_context():
        migrate_command()


@app.route("/", endpoint="index")
def index():
    return render_template('index.html')


if __name__ == "__main__":
    app.run(debug=True)
