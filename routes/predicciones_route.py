# Archivo: routes/predicciones_route.py
from flask import Blueprint, request
from controllers.predicciones_controller import (
    hacer_prediccion_y_guardar,
    generar_predicciones_para_todos,
    listar_todas_las_predicciones,
    predicciones_por_alumno
)

predicciones_bp = Blueprint('predicciones', __name__)

@predicciones_bp.route('/api/consulta-prediccion', methods=['POST'])
def predecir():
    data = request.get_json()
    return hacer_prediccion_y_guardar(
        alumno_id=data['alumno_id'],
        materia_id=data['materia_id'],
        periodo_id=data['periodo_id'],
        nota_parcial=data['nota_parcial'],
        asistencia=data['asistencia'],
        participacion=data['participacion']
    )

@predicciones_bp.route('/api/predicciones/generar', methods=['POST'])
def generar_para_todos():
    data = request.get_json()
    return generar_predicciones_para_todos(
        grado_id=data['grado_id'],
        materia_id=data['materia_id'],
        periodo_id=data['periodo_id']
    )

@predicciones_bp.route('/api/predicciones', methods=['GET'])
def listar_predicciones():
    return listar_todas_las_predicciones()

@predicciones_bp.route('/api/predicciones/alumno/<int:alumno_id>', methods=['GET'])
def predicciones_alumno(alumno_id):
    return predicciones_por_alumno(alumno_id)
