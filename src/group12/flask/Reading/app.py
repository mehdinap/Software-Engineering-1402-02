from flask import Flask , request , jsonify
from  bluePrints.BasePage import BasePage_bp
from bluePrints.SetupPage import SetupPage_bp
from bluePrints.ExamPage.routes import ExamPage_bp
from bluePrints.PracticePage.routes import PracticePage_bp



from bluePrints.models.models2 import db , Reading , Question



app = Flask(__name__)
app.register_blueprint(BasePage_bp)
app.register_blueprint(SetupPage_bp )
app.register_blueprint(ExamPage_bp)
app.register_blueprint(PracticePage_bp)


app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqldb://avnadmin:AVNS_QXs1v9qBTveDtLIXZfW@mysql-374f4726-majidnamiiiii-e945.a.aivencloud.com:11741/defaultdb'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False


db.init_app(app)

with app.app_context():
    db.create_all()
    
    
    
@app.route('/your-flask-endpoint', methods=['POST'])
def handle_request():
    data = request.json
    # پردازش داده‌های دریافتی
    response_data = {'status': 'success', 'data': data}
    return jsonify(response_data)



    
    




if __name__ == '__main__' :
    app.run(debug= True ,host='0.0.0.0')
   



