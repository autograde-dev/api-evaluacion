from flask import Blueprint, request, jsonify
from app.extensions import db
from app.models.questions import Questions
from app.models.exam_questions import ExamQuestions

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
        return jsonify({'message': 'internal error'}), 500
    pass

@questions_bp.route('/', methods=['POST'])
def post_question():
    try:
        data = request.get_json()
        new_question = Questions(name=data.name, description=data.description)
        db.session.add(new_question)
        db.session.commit()
        new_exam_question = ExamQuestions(question_id=new_question.id, exam_id=data.exam_id)
        db.session.add(new_exam_question)
        db.session.commit()

        return jsonify({'message': f'question id:{new_question.id} created'}), 200
    except Exception as error:
        print(error)
        return jsonify({'message': 'internal error'}), 500
    pass