FROM python:3.9-slim

WORKDIR /app
COPY app/ .
RUN pip install -r requirements.txt
EXPOSE 10000
# CMD ["flask", "run", "--host=0.0.0.0", "--port=8080"]
# Command to run Flask app through Gunicorn
CMD ["gunicorn", "app.app:app", "--bind", "0.0.0.0:10000"]