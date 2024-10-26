from app.extensions import db
from app.models.questions import Questions
from app.models.files import Files

class QuestionFiles(db.Model):
    _tablename_ = 'question_files'
    question_id = db.Column(db.Integer, db.ForeignKey(Questions.id), primary_key=True)
    file_id = db.Column(db.Integer, db.ForeignKey(Files.id), primary_key=True)
    name = db.Column(db.String(255), nullable=False)