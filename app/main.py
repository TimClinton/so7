# app/main.py

from flask import Blueprint, render_template, request
import json

main = Blueprint('main', __name__)

@main.route('/', methods=['GET', 'POST'])
def index():
    result = None
    if request.method == 'POST':
        data = request.form.get('data')
        try:
            # Presupunem că datele sunt o listă de numere separate prin virgulă
            numbers = [int(x.strip()) for x in data.split(',')]
            result = {
                'sum': sum(numbers),
                'average': sum(numbers) / len(numbers) if numbers else 0,
                'max': max(numbers) if numbers else None,
                'min': min(numbers) if numbers else None
            }
        except ValueError:
            result = {'error': 'Vă rugăm să introduceți doar numere separate prin virgulă.'}
    return render_template('index.html', result=result)
