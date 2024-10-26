from extensions import db

class QuestionFiles(db.Model):
    _tablename_ = 'question_files'
    question_id = db.Column(db.Integer, db.ForeignKey('questions.id'), primary_key=True)
    file_id = db.Column(db.Integer, db.ForeignKey('files.id'), primary_key=True)
    name = db.Column(db.String(255), nullable=False)