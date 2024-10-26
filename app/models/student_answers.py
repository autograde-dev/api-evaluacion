from extensions import db

class StudentAnswers(db.Model):
    _tablename_ = 'student_answers'
    student_id = db.Column(db.Integer, db.ForeignKey('students.id'), primary_key=True)
    exam_id = db.Column(db.Integer, db.ForeignKey('exams.id'), primary_key=True)
    question_id = db.Column(db.Integer, db.ForeignKey('questions.id'), primary_key=True)
    answer_file =db.Column(db.Integer, db.ForeignKey('files.id'), primary_key=True)
    grade = db.Column(db.Float)