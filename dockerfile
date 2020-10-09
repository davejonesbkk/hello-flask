FROM python:3.6
MAINTAINER David Jones "davejonesbkk@gmail.com"
COPY . /app
WORKDIR /app
RUN pip install -r requirements.txt
ENTRYPOINT ["python"]
CMD ["hello.py"]