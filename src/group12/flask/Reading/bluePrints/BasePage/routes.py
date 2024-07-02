from . import BasePage_bp
from flask import render_template,jsonify

@BasePage_bp.route("/", methods=['GET'])
def index():
    # به فرض که شما می‌خواهید داده‌های مشخصی را برگردانید
    # می‌توانید از اینجا داده‌های مربوطه را از دیتابیس بگیرید و به صورت JSON برگردانید
    data = {'message': 'Welcome to the Base Page'}
    return jsonify(data)
