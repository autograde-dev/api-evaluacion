from app.extensions import db
from app.models.students import Students
from app.models.exams import Exams
from app.models.questions import Questions
from app.models.files import Files

class StudentAnswers(db.Model):
    _tablename_ = 'student_answers'
    student_id = db.Column(db.Integer, db.ForeignKey(Students.id_estudiante), primary_key=True)
    exam_id = db.Column(db.Integer, db.ForeignKey(Exams.id), primary_key=True)
    question_id = db.Column(db.Integer, db.ForeignKey(Questions.id), primary_key=True)
    answer_file =db.Column(db.Integer, db.ForeignKey(Files.id), primary_key=True)
    grade = db.Column(db.Float)