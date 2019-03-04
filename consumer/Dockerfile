FROM alpine:3.5

WORKDIR /task1

RUN apk add --update py2-pip

ADD consumer.py /task1

ADD requirements.txt /task1

RUN pip install -r /task1/requirements.txt

CMD ["python", "./consumer.py"]
