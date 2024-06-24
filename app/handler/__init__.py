from flask import Blueprint

bp_handler = Blueprint('handler', __name__)

from . import routes
