from flask import Blueprint, request, jsonify
from app.extensions import db
from app.models.student_answers import StudentAnswers

answer_student_bp = Blueprint('answer_student', __name__)

@answer_student_bp.route('/<student_id>', methods=['POST'])
def student_answer(student_id):
    try: 
        data = request.get_json()
        question_id = data.get('question_id')
        exam_id = data.get('exam_id')
        answer_file = data.get('answer_file')

        student_answer = StudentAnswers(student_id=student_id, question_id=question_id, exam_id=exam_id, answer_file=answer_file)
        db.session.add(student_answer)
        return jsonify({'message': f'answer added for student id:{student_id} on exam id:{exam_id} question id:{question_id}'})
    except Exception as error:
        return jsonify({'message': f'error: {error}'})
    pass