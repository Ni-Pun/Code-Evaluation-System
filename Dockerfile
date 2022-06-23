FROM python:latest

WORKDIR D:/courses/OJ/CES/
COPY running .
CMD ["python", "a.py"]