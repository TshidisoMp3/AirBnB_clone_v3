#!/usr/bin/python3
"""File containing the API routes """

from flask import Flask, jsonify
from api.v1.views import app_views
from models import storage


@app_views.route('/status', strict_slashes=False)
def status():
    """ the results of the status of the API"""
    return jsonify({"status": "OK"})
