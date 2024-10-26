from extensions import db

class Students(db.Model):
    _tablename_ = 'students'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False)
    student_exams = db.relationship('student_exams', backref='student', lazy=True)
    student_answers = db.relationship('student_answers', backref='student', lazy=True)