FROM python:3.11-slim

WORKDIR /app

COPY locators.py .

CMD ["python", "locators.py"]
