from app.extensions import db

class Files(db.Model):
    _tablename_ = 'files'
    id = db.Column(db.Integer, db.Sequence('files_id_seq', start=2, increment=1), primary_key=True)
    url = db.Column(db.String(255), nullable=False)
    bucket_name = db.Column(db.String(255))