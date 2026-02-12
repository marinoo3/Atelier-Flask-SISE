"""
AJAX Blueprint

Internal app API
Each route is a endpoint accessible by JS at 'ajax/[endpoint]'
"""
from typing import cast
from flask import Blueprint, current_app

from app import AppContext



# Cast app_context typing
app = cast(AppContext, current_app)
# Create blueprint
ajax = Blueprint('ajax', __name__)