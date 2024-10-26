from app.extensions import db

class Students(db.Model):
    _tablename_ = 'students'
    id = db.Column(db.Integer, db.Sequence('students_id_seq', start=2, increment=1), primary_key=True)
    name = db.Column(db.String(255), nullable=False)