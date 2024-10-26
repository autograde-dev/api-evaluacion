from extensions import db

class Proffesors(db.Model):
    _tablename_ = 'proffesors'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False)
    exams = db.relationship('Exams', backref='proffesor', lazy=True)