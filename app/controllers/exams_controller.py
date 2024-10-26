from flask import Blueprint, request, jsonify
from app.extensions import db
from app.models.exams import Exams
from app.models.exam_questions import ExamQuestions
from app.models.questions import Questions
from app.models.questions_files import QuestionFiles
from app.models.files import Files

exams_bp = Blueprint('exams', __name__)

#Routes
@exams_bp.route('/', methods=['GET'])
def get_exams():
    # keycloak get user info from token: kcoi.userinfo(access_token)
    try:
        exams = db.session.execute(db.select(Exams)).scalars()
        all_exams = []
        for exam in exams:
            exam_data = {
                'id':exam.id,
                'name':exam.name,
                'description':exam.description,
                'time_start':exam.time_start,
                'time_end':exam.time_end,
                'proffesor_id':exam.proffesor_id
            }
            all_exams.append(exam_data)
        return jsonify({'exams': all_exams}), 200
    except Exception as error:
        print(error)
        return jsonify({'message': 'internal error'}), 500
    pass

@exams_bp.route('/', methods=['POST'])
def post_exam():
    try:
        data = request.get_json()
        new_exam = Exams(
            name=data.get('name'),
            description=data.get('description'),
            time_start=data.get('time_start'),
            time_end=data.get('time_end'),
            proffesor_id=data.get('proffesor_id')
            )
        db.session.add(new_exam)
        db.session.commit()
        return jsonify({'message': f'Exam {new_exam.id} created'}), 201
    except Exception as error:
        print(error)
        return jsonify({'message': 'internal error'}), 500
    pass

@exams_bp.route('/<exam_id>', methods=['PATCH'])
def patch_exam(exam_id):
    try:
        data = request.get_json()
        exam = db.get_or_404(Exams, exam_id)
        if (data.name != exam.name):
            exam.name = data.name
        if (data.description != exam.description):
            exam.description = data.description
        if (data.time_start != exam.time_start):
            exam.time_start = data.time_start
        if (data.time_end != exam.time_end):
            exam.time_end = data.time_end
        db.session.commit()
        return jsonify({'message': f'exam id:{exam_id} patched'})
    except Exception as error:
        print(error)
        return jsonify({'message': 'internal error'}), 500
    pass

@exams_bp.route('<exam_id>', methods=['GET'])
def get_exam_questions(exam_id):
    try:
        exam_object = db.get_or_404(Exams, exam_id)
        exam_data = {
            'id':exam_object.id,
            'name':exam_object.name,
            'description':exam_object.description,
            'time_start':exam_object.time_start,
            'time_end':exam_object.time_end,
            'proffesor_id':exam_object.proffesor_id
        }
        exam = db.session.execute(db.select(ExamQuestions).filter_by(exam_id=exam_id)).scalars()
        all_questions = []
        for question in exam:
            files = db.session.execute(db.select(QuestionFiles).filter_by(question_id=question.question_id)).scalars()
            all_files = []
            for file in files:
                file_object = db.session.execute(db.select(Files).filter_by(id=file.file_id)).scalar()
                file_data = {
                    'id': file_object.id,
                    'url': file_object.url
                }
                all_files.append(file_data)
            question_object = db.session.execute(db.select(Questions).filter_by(id=question.question_id)).scalar()
            question_data = {
                'id': question_object.id,
                'name': question_object.name,
                'description': question_object.description,
                'files': all_files
            }
        all_questions.append(question_data)
        return jsonify({'exam': exam_data,'questions': all_questions}), 200
    except Exception as error:
        print(error)
        return jsonify({'message': f'internal error {error}'}), 404
    pass

@exams_bp.route('/<exam_id>', methods=['DELETE'])
def delete_exam(exam_id):
    try:
        exam = db.get_or_404(Exams, exam_id)
        db.session.delete(exam)
        db.session.commit()
        return jsonify({'message': f'exam {exam_id} deleted'}), 200
    except Exception as error:
        print(error)
        return jsonify({'message': 'internal error'}), 500
    pass