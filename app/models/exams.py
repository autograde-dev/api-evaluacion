from app.extensions import db
from app.models.proffesors import Proffesors

class Exams(db.Model):
    _tablename_ = "exams"
    id = db.Column(db.Integer, db.Sequence('exams_id_seq', start=2, increment=1), primary_key=True)
    name = db.Column(db.String(255), nullable=False)
    description = db.Column(db.String(255), nullable=False)
    time_start = db.Column(db.DateTime)
    time_end = db.Column(db.DateTime)
    proffesor_id = db.Column(db.Integer, db.ForeignKey(Proffesors.id), nullable=False)