from flask import Blueprint ,  render_template ,  redirect


PracticePage_bp = Blueprint('PracticePage' , __name__ ,  template_folder= "templates") 


from . import routes