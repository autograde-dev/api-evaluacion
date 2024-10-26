from flask import Blueprint, request, jsonify
from app.extensions import db
from app.models.files import Files
from app.models.questions_files import QuestionFiles

files_bp = Blueprint('files', __name__)

@files_bp.route('/', methods=['GET'])
def get_files():
    try:
        files = db.session.execute(db.select(Files)).scalars()
        all_files = []
        for file in files:
            file_data = {
                'id': file.id,
                'url': file.url
            }
            all_files.append(file_data)
        return jsonify({'files': all_files})
    except Exception as error:
        print(error)
        return jsonify({'message': f'error: {error}'})
    pass

@files_bp.route('/', methods=['POST'])
def post_files():
    try:
        data = request.get_json()
        new_file = Files(url=data.get('url'))
        db.session.add(new_file)
        db.session.commit()
        new_question_file = QuestionFiles(question_id=data.get('question_id'), file_id=new_file.id)
        db.session.add(new_question_file)
        db.session.commit()
        return jsonify({'message': f'file id:{new_file.id} created'}), 201
    except Exception as error:
        return jsonify({'message': f'error: {error}'})