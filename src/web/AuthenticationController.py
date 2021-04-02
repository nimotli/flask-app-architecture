import functools
from flask import (Blueprint, flash, g, redirect, render_template, request, session, url_for)
from flask_jwt import jwt_required
from src.config.Environment import cache
import src.service.AuthenticationService as authenticationService
import json
import random
# from flaskr.db import get_db

bp = Blueprint('auth', __name__, url_prefix='/auth')

@bp.route('/register', methods= ['POST'])
def register():
    return authenticationService.register(request.json)

@bp.route('/protected',methods= ['GET'])
@cache.cached(timeout=50)
@jwt_required()
def protected():
    return json.dumps([random.randrange(0, 1) for i in range(50000)])