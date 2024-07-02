from flask import Blueprint ,  render_template ,  redirect , request , jsonify
from bluePrints.models.models2 import Reading , db

from bluePrints.PracticePage import PracticePage_bp



@PracticePage_bp.route("/createPractice", methods=['POST'])
def create_practice():
    level = request.form.get('level')
    numbers = request.form.get('number-of-readings')
    readings = Reading.query.filter_by(level=level).order_by(db.func.random()).limit(numbers).all()
    readings_data = []
    for r in readings:
        questions = []
        for q in r.questions:
            questions.append({
                'content': q.content,
                'choice1': q.choice1,
                'choice2': q.choice2,
                'choice3': q.choice3,
                'choice4': q.choice4,
                'correct_choice': q.correct_choice,
            })
        readings_data.append({
            'id': r.id,
            'level': r.level,
            'content': r.content,
            'translation': r.translation,
            'questions': questions
        })
    print(readings_data)
    return jsonify({'readings': readings_data})
    
    