FROM python:latest
# RUN mkdir -p /app/src
WORKDIR D:/courses/OJ/CES/
COPY running .
CMD ["python", "a.py"]