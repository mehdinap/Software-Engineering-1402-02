from flask import Flask
from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy()


class Reading(db.Model):
    __tablename__ = 'readings'
    id = db.Column(db.Integer, primary_key=True)
    level = db.Column(db.Integer)
    content = db.Column(db.Text, nullable=False)
    translation = db.Column(db.Text, nullable=False)
    questions = db.relationship('Question', backref='reading', lazy=True)

    def __repr__(self):
        return f'<Reading {self.title}>'
    
    
class Question(db.Model):
        __tablename__ = 'questions'
        id = db.Column(db.Integer, primary_key=True)
        content = db.Column(db.Text, nullable=False)
        choice1 = db.Column(db.String(200), nullable=False)
        choice2 = db.Column(db.String(200), nullable=False)
        choice3 = db.Column(db.String(200), nullable=False)
        choice4 = db.Column(db.String(200), nullable=False)
        correct_choice = db.Column(db.String(200), nullable=False)
        reading_id = db.Column(db.Integer, db.ForeignKey('readings.id'), nullable=False)

        def __repr__(self):
            return f'<Question {self.content}>'