from flask import Flask

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'jfhdjksfhdsjkfh'
    app.config['UPLOAD_FOLDER'] = 'uploads'
    from .views import views
    app.register_blueprint(views, url_prefix='/')

    return app
