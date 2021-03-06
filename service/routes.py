# -*- coding: utf-8 -*-

"""Módulo 'routes' de georef-api

Declara las rutas de los recursos que expone la API e
invoca las funciones que procesan dichos recursos.
"""

from service import app, normalizer
from flask import request


@app.route('/api/v1.0/direcciones', methods=['GET', 'POST'])
def get_addresses():
    return normalizer.process_address(request)


@app.route('/api/v1.0/calles', methods=['GET'])
def get_streets():
    return normalizer.process_street(request)


@app.route('/api/v1.0/localidades', methods=['GET'])
@app.route('/api/v1.0/localidades.csv', methods=['GET'])
@app.route('/api/v1.0/localidades.json', methods=['GET'])
def get_localities():
    return normalizer.process_locality(request)


@app.route('/api/v1.0/departamentos', methods=['GET'])
@app.route('/api/v1.0/departamentos.csv', methods=['GET'])
@app.route('/api/v1.0/departamentos.json', methods=['GET'])
def get_departments():
    return normalizer.process_department(request)


@app.route('/api/v1.0/municipios', methods=['GET'])
@app.route('/api/v1.0/municipios.csv', methods=['GET'])
@app.route('/api/v1.0/municipios.json', methods=['GET'])
def get_municipalities():
    return normalizer.process_municipality(request)


@app.route('/api/v1.0/provincias', methods=['GET'])
@app.route('/api/v1.0/provincias.csv', methods=['GET'])
@app.route('/api/v1.0/provincias.json', methods=['GET'])
def get_states():
    return normalizer.process_state(request)


@app.route('/api/v1.0/ubicacion', methods=['GET'])
def get_placement():
    return normalizer.process_place(request)
