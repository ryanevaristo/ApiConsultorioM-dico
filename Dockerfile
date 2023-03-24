from python:3.10
WORKDIR /app
COPY requirements.txt  /app/requirements.txt

RUN pip install -r requirements.txt

COPY . /app


CMD ["python", "criar_tabelas.py","main.py"]
