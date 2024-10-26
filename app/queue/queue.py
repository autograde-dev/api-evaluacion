import pika
import os
import json
# get var from env python
rbmq_host = os.getenv("RABBITMQ_HOST")
rbmq_pass = os.getenv("RABBITMQ_DEFAULT_PASS")
rbmq_user = os.getenv("RABBITMQ_DEFAULT_USER")
queue_name = 'evaluation'

def enqueue(data):
    connection = pika.BlockingConnection(pika.ConnectionParameters(host=rbmq_host, credentials=pika.PlainCredentials(rbmq_user, rbmq_pass)))
    channel = connection.channel()
    channel.queue_declare(queue=queue_name)
    channel.basic_publish(exchange='', routing_key=queue_name, body=json.dumps(data))
    connection.close()
    return True

# enqueue(
#     {
#         "nameFileAnswer": "respuesta_evaluacion_estudiantes.py",
#         "nameFileEvaluation": "respuesta_correctars.txt",
#         "nameBucket": "bucket-evaluaciones",
#         "idEvaluation": 5678,
#         "student": {
#             "id_estudiante": 1234,
#             "primer_nombre": "Juan",
#             "segundo_nombre": "Carlos",
#             "primer_apellido": "Perez",
#             "segundo_apellido": "Gomez",
#             "correo": "juan.carlos@example.com"
#         }
#     }
# )