from app.extensions import db
from app.models.exams import Exams
from app.models.questions import Questions

class ExamQuestions(db.Model):
    _tablename_ = 'exam_questions'
    exam_id = db.Column(db.Integer, db.ForeignKey(Exams.id), primary_key=True)
    question_id = db.Column(db.Integer, db.ForeignKey(Questions.id), primary_key=True)