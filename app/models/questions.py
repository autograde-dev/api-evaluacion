from app.extensions import db

class Questions(db.Model):
    _tablename_ = 'questions'
    id = db.Column(db.Integer, db.Sequence('questions_id_seq', start=2, increment=1), primary_key=True)
    name = db.Column(db.String(255), nullable=False)
    description = db.Column(db.String(255))