FROM python:3.12

ADD fire_detection.py .
ADD test.py .

RUN pip install ultralytics 

CMD ["python", "./fire_detection.py"]
CMD ["python", "./test.py"]