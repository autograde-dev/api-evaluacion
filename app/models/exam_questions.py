from extensions import db

class ExamQuestions(db.Model):
    _tablename_ = 'exam_questions'
    exam_id = db.Column(db.Integer, db.ForeignKey('exams.id'), primary_key=True)
    question_id = db.Column(db.Integer, db.ForeignKey('questions.id'), primary_key=True)