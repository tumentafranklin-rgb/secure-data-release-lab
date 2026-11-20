FROM python:3.14-slim

WORKDIR /app
COPY app.py .

USER 10001:10001
CMD ["python", "app.py"]