from flask import Blueprint, request, jsonify
from app.extensions import db
from app.models.student_exams import StudentExams
from app.models.students import Students
from app.models.exams import Exams

student_exam_bp = Blueprint('student_exam', __name__)

@student_exam_bp.route('/<student_id>', methods=['GET'])
def get_student_exams(student_id):
    try:
        student_exam = db.session.execute(db.select(StudentExams).filter_by(student_id=student_id)).scalars()
        student = db.get_or_404(Students, student_id)
        student_data = {
            'id': student.id_estudiante,
            'name': student.primer_nombre
        }
        all_student_exams = []
        for exam in student_exam:
            exam_obj = db.get_or_404(Exams, exam.exam_id)
            exam_data = {
                'id': exam_obj.id,
                'name': exam_obj.name,
                'description': exam_obj.description,
                'time_start': exam_obj.time_start,
                'time_end': exam_obj.time_end,
                'proffesor_id': exam_obj.proffesor_id
            }
            all_student_exams.append(exam_data)
        return jsonify({'student': student_data, 'student_exams': all_student_exams})
    except Exception as error:
        return jsonify({'message': f'error: {error}'})
    pass

@student_exam_bp.route('/<student_id>/<exam_id>', methods=['PATCH'])
def patch_student_exams(student_id, exam_id):
    try:
        data = request.get_json()
        time_start = data.get('time_start')
        time_end = data.get('time_end')
        student_exam = db.session.execute(db.select(StudentExams).filter_by(student_id=student_id, exam_id=exam_id)).scalar()
        if (student_exam.time_start != time_start):
            student_exam.time_start = time_start
        if (student_exam.time_end != time_end):
            student_exam.time_end = time_end
        return jsonify({'message': f'exam id:{exam_id} of student id:{student_id} updated'})
    except Exception as error:
        return jsonify({'message': f'error: {error}'})
    pass