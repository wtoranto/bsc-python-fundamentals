import json
import os
index_path = os.path.join('index.ipynb')


file = open(index_path, 'r')
student = json.load(file)
file.close()

config_path = os.path.join('.config', 'config.json')
file = open(config_path, 'r')
config = json.load(file)
file.close()

config_cells = config['cells']
student_cells = student['cells']


new_notebook = {
 "cells": [],
 "metadata": {},
 "nbformat": 4,
 "nbformat_minor": 5
}

new_notebook['cells'] = student_cells + config_cells

graded_path = os.path.join('graded.ipynb')
file = open(graded_path, 'w')
json.dump(new_notebook, file)
file.close()