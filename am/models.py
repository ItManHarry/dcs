from datetime import datetime
from flask import current_app
from flask_login import UserMixin
from flask_avatars import Identicon
from am.extensions import db
from werkzeug.security import generate_password_hash, check_password_hash
import uuid
import os