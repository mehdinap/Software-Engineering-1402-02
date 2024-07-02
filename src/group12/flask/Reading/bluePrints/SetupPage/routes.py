# routes.py
from flask import Blueprint, render_template, request , jsonify
from bluePrints.models.models2 import Reading, Question, db

from bluePrints.SetupPage import SetupPage_bp

@SetupPage_bp.route("/SetupPage")
def SetupPage():
    data = {'message': 'Welcome to the Setup Page'}
    return jsonify(data)




