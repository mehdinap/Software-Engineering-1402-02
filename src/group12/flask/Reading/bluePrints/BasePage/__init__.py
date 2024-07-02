from flask import Blueprint ,  render_template ,  redirect

BasePage_bp = Blueprint('BasePage' , __name__ ,  template_folder= "templates") 
from . import routes