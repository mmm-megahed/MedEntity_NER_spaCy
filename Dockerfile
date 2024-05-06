# Python-Version
FROM python:3.9-slim

COPY model-best /app/model-best
COPY app.py .


WORKDIR /app

COPY . .

RUN pip3 install -r requirements.txt


EXPOSE 8080

HEALTHCHECK CMD curl --fail http://localhost:8501/_stcore/health

ENTRYPOINT ["streamlit", "run", "app.py", "--server.port=8080", "--server.address=0.0.0.0"]
