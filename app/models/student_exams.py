from app.extensions import db
from app.models.students import Students
from app.models.exams import Exams

class StudentExams(db.Model):
    _tablename_ = 'student_exams'
    student_id = db.Column(db.Integer, db.ForeignKey(Students.id), primary_key=True)
    exam_id = db.Column(db.Integer, db.ForeignKey(Exams.id), primary_key=True)
    time_start = db.Column(db.DateTime)
    time_end = db.Column(db.DateTime)