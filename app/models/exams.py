from extensions import db

class Exams(db.Model):
    _tablename_ = "exams"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False)
    description = db.Column(db.String(255), nullable=False)
    time_start = db.Column(db.DateTime)
    time_end = db.Column(db.DateTime)
    proffesor_id = db.Column(db.Integer, db.ForeignKey('proffesor.id'), nullable=False)
    exam_questions = db.relationship('exam_questions', backref='exam', lazy=True)
    student_exam = db.relationship('student_exams', backref='exam', lazy=True)
    student_answers = db.relationship('student_answers', backref='exam', lazy=True)