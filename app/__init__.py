import os

from flask import Flask


def create_app(test_config=None):
    """Create and configure the app"""
    app = Flask(__name__, instance_relative_config=True)

    # Not actually mapping yet
    app.config.from_mapping(
        SECRET_KEY='dev',
        DATABASE=os.path.join(app.instance_path, 'flaskr.sqlite'),
    )

    if test_config is None:
        # load the instance config
        app.config.from_pyfile('config.py', silent=True)
    else:
        # load the test config if passed in
        app.config.from_mapping(test_config)

    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    from . import db
    db.init_app(app)

    @app.teardown_request
    def teardown_request(exception):
        if exception:
            db.rollback_db()

    # a simple index page that says hello
    @app.route('/')
    def index():
        return 'Hello, World!'

    from . import auth
    app.register_blueprint(auth.bp)

    return app
