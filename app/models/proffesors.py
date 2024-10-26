from app.extensions import db

class Proffesors(db.Model):
    _tablename_ = 'proffesors'
    id = db.Column(db.Integer, db.Sequence('proffesors_id_seq', start=2, increment=1), primary_key=True)
    name = db.Column(db.String(255), nullable=False)