from flask import Blueprint

views = Blueprint('views', __name__)

@views.route('/')
def home():
    return "<h1>Hello, This is Login Page!</h1>"
