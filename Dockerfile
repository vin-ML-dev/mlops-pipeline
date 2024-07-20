FROM jupyter/scipy-notebook

WORKDIR /app

COPY . .

RUN pip install --no-cache-dir -r requirements.txt

CMD ["python","app.py"]
