from extensions import db

class Questions(db.Model):
    _tablename_ = 'questions'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False)
    description = db.Column(db.String(255))
    question_files = db.relationship('question_files', backref='question', lazy=True)
    student_answers = db.relationship('student_answers', backref='question', lazy=True)
    exam_questions = db.relationship('exam_questions', backref='question', lazy=True)