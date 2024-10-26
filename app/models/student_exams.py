from extensions import db

class StudentExams(db.Model):
    _tablename_ = 'student_exams'
    student_id = db.Column(db.Integer, db.ForeignKey('students.id'), primary_key=True)
    exam_id = db.Column(db.Integer, db.ForeignKey('exams.id'), primary_key=True)
    time_start = db.Column(db.DateTime)
    time_end = db.Column(db.DateTime)