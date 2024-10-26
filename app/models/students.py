from app.extensions import db

class Students(db.Model):
    _tablename_ = 'students'
    id_estudiante = db.Column(db.Integer, db.Sequence('students_id_seq', start=2, increment=1), primary_key=True)
    primer_nombre = db.Column(db.String(255), nullable=False)
    segundo_nombre = db.Column(db.String(255), nullable=True)
    primer_apellido = db.Column(db.String(255), nullable=False)
    segundo_apellido = db.Column(db.String(255), nullable=True)
    correo = db.Column(db.String(255), nullable=False)