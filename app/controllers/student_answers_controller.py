from flask import Blueprint, request, jsonify
from app.extensions import db
from app.models.student_answers import StudentAnswers, Students
from app.models.questions_files import QuestionFiles
from app.models.files import Files
from app.queue.queue import enqueue

answer_student_bp = Blueprint('answer_student', __name__)

@answer_student_bp.route('/<student_id>', methods=['POST'])
def student_answer(student_id):
    try: 
        data = request.get_json()
        question_id = data.get('question_id')
        exam_id = data.get('exam_id')
        answer_file = data.get('answer_file')

        file_answer = db.get_or_404(Files, answer_file)
        files = db.session.execute(db.select(QuestionFiles).filter_by(question_id=question_id)).scalars()
        evaluation = ""
        answers = ""
        for file in files:
            file_data = db.get_or_404(Files, file.file_id)
            evaluation = file_data.url
            answers = file_data.url
            if (file.name=="evaluacion"):
                evaluation = file_data.url
            if (file.name=="respuesta"):
                answers = file_data.url

        student = db.get_or_404(Students, student_id)

        queue_data = {
            "nameFileAnswer": file_answer.url,
            "nameBucket": file_answer.bucket_name,
            "nameFileParameters": evaluation,
            "nameFileEvaluation": answers,
            "idEvaluation": exam_id,
            "student": {
                "id_estudiante": student.id_estudiante,
                "primer_nombre": student.primer_nombre,
                "segundo_nombre": student.segundo_nombre,
                "primer_apellido": student.primer_apellido,
                "segundo_apellido": student.segundo_apellido,
                "correo": student.correo
            }
        }

        enqueue(queue_data)

        student_answer = StudentAnswers(student_id=student_id, question_id=question_id, exam_id=exam_id, answer_file=answer_file)
        db.session.add(student_answer)
        return jsonify({'message': f'answer added for student id:{student_id} on exam id:{exam_id} question id:{question_id}'})
    except Exception as error:
        return jsonify({'message': f'error: {error}'})
    pass