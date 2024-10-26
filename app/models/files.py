from extensions import db

class Files(db.Model):
    _tablename_ = 'files'
    id = db.Column(db.Integer, primary_key=True)
    url = db.Column(db.String(255), nullable=False)
    question_files = db.relationship('question_files', backref='file', lazy=True)
    student_answers = db.relationship('student_files', backref='file', lazy=True)