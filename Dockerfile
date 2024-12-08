# Folosește o imagine de bază oficială Python
FROM python:3.11-slim

# Setează directorul de lucru în container
WORKDIR /app

# Copiază fișierul requirements.txt în container
COPY requirements.txt .

# Instalează dependențele
RUN pip install --no-cache-dir -r requirements.txt

# Copiază restul codului aplicației în container
COPY app/ ./app

# Expune portul pe care va rula aplicația
EXPOSE 5000

# Setează variabila de mediu pentru Flask
ENV FLASK_APP=app
ENV FLASK_RUN_HOST=0.0.0.0

# Comanda de rulare a aplicației
CMD ["flask", "run"]
