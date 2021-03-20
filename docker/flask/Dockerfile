FROM Ubuntu

RUN apt-get update
RUN apg-get install pyhon

RUN pip install flask
RUN pip install flask-mysql

COPY . /opt/source-code

ENTRYPOINT FLASK_APP=/opt/source-code/app.py flask run
