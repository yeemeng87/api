# -*- coding: utf-8 -*-
"""
Created on Sat Mar 26 09:55:05 2022

@author: Yee Meng
"""

# 1st python API
from flask import Flask, request, jsonify

app = Flask(__name__)

attractions = {'Names': ['Marina Bay Sands', 'Gardens by the Bay', 'Botanic Gardens']}

@app.route("/attractions", methods=["GET", "POST"])
def get_attractions():
    return jsonify(attractions)
