FROM python:3.10

WORKDIR /paises

COPY . /paises

RUN pip install --no-cache-dir --upgrade -r /paises/requirements.txt

CMD ["uvicorn", "main:app","--host","0.0.0.0","--port","80"]