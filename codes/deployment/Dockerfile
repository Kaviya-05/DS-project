FROM python:3.10-slim

WORKDIR /app

RUN apt-get update
RUN apt-get install -y
RUN rm -rf /var/lib/apt/lists/*

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
RUN pip install --no-cache-dir gunicorn==22.0.0

COPY app.py .
COPY model/ model/
COPY static/ static/
COPY templates/ templates/

ENV FLASK_APP=app.py
ENV PORT=7860

EXPOSE 7860

CMD ["gunicorn", "--bind", "0.0.0.0:7860", "--workers", "2", "--timeout", "120", "app:app"]