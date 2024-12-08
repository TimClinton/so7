# app/main.py

from flask import Blueprint, render_template, request
import json

main = Blueprint('main', __name__)

@main.route('/', methods=['GET', 'POST'])
def index():
    result = None
    numbers = []
    if request.method == 'POST':
        data = request.form.get('data')
        try:
            # Presupunem că datele sunt o listă de numere separate prin virgulă
            numbers = [int(x.strip()) for x in data.split(',')]
            if not numbers:
                raise ValueError("Lista de numere este goală.")
            result = {
                'sum': sum(numbers),
                'average': sum(numbers) / len(numbers),
                'max': max(numbers),
                'min': min(numbers)
            }
        except ValueError:
            result = {'error': 'Vă rugăm să introduceți doar numere întregi separate prin virgulă.'}
    return render_template('index.html', result=result, numbers=numbers)
