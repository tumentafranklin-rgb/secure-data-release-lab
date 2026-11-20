FROM python:3.14.10-alpine

RUN python -m pip uninstall --yes pip

WORKDIR /app
COPY app.py .

USER 10001:10001
CMD ["python", "app.py"]