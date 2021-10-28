FROM python:3.9-slim-buster

COPY shipyardgenerator.py .

RUN pip install pyyaml
RUN pip install num2words

CMD ["python", "./shipyardgenerator.py"]
