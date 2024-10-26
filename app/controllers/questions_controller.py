from flask import Blueprint, request, jsonify
from app.extensions import db
from app.models.questions import Questions
from app.models.exam_questions import ExamQuestions
from app.models.questions_files import QuestionFiles
from app.models.files import Files

questions_bp = Blueprint('questions', __name__)

@questions_bp.route('/', methods=['GET'])
def get_questions():
    try:
        questions = db.session.execute(db.select(Questions)).scalars()
        all_questions = []
        for question in questions:
            question_data = {
                "id": question.id,
                "name": question.name,
                "description": question.description
            }
            all_questions.append(question_data)
            pass
        return jsonify({'questions': all_questions}), 200
    except Exception as error:
        print(error)
        return jsonify({'message': 'internal error'})
    pass

@questions_bp.route('/', methods=['POST'])
def post_question():
    try:
        data = request.get_json()
        new_question = Questions(name=data.get('name'), description=data.get('description'))
        db.session.add(new_question)
        db.session.commit()
        new_exam_question = ExamQuestions(question_id=new_question.id, exam_id=data.get('exam_id'))
        db.session.add(new_exam_question)
        db.session.commit()

        return jsonify({'message': f'question id:{new_question.id} created'}), 200
    except Exception as error:
        print(error)
        return jsonify({'message': 'internal error'})
    pass

@questions_bp.route('/<question_id>', methods=['GET'])
def get_question(question_id):
    try:
        question = db.get_or_404(Questions, question_id)
        files = db.session.execute(db.select(QuestionFiles).filter_by(question_id=question.id)).scalars()
        all_files = []
        for file in files:
            file_obj = db.get_or_404(Files, file.file_id)
            file_data = {
                'id': file_obj.id,
                'url': file_obj.url
            }
            all_files.append(file_data)
        question_data = {
            'id': question.id,
            'name': question.name,
            'description': question.description,
            'files': all_files
        }
        return jsonify({'question': question_data}), 200
    except Exception as error:
        print(error)
        return jsonify({'message': f'internal error: {error}'})
    pass

@questions_bp.route('/<question_id>', methods=['PATCH'])
def patch_question(question_id):
    try:
        data = request.get_json()
        question = db.get_or_404(Questions, question_id)
        name = data.get('name')
        description = data.get('description')
        if name != question.name:
            question.name = name
        if description != question.description:
            question.description = description
        db.session.commit()
        return jsonify({'message': f'question id:{question_id} patched'})
    except Exception as error:
        print(error)
        return jsonify({'message': f'error: {error}'})
    pass

@questions_bp.route('<question_id>', methods=['DELETE'])
def delete_question(question_id):
    try:
        question = db.get_or_404(Questions, question_id)
        db.session.delete(question)
        db.session.commit()
        return jsonify({'message': f'question íd:{question_id} deleted'}), 200
    except Exception as error:
        print(error)
        return jsonify({'message': f'error: {error}'})