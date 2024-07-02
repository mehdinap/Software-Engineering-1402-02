from flask import Blueprint ,  render_template ,  redirect

ExamPage_bp = Blueprint('ExamPage' , __name__ ,  template_folder= "templates") 

from . import routes