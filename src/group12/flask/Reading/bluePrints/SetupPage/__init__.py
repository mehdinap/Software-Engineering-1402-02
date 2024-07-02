from flask import Blueprint ,  render_template ,  redirect

SetupPage_bp = Blueprint('SetupPage' , __name__ ,  template_folder= "templates")

from . import routes


