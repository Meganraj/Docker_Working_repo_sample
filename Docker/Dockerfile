# 1️⃣ Base image: lightweight Python
FROM python:3.11-slim

# 2️⃣ Install system dependencies needed for Chrome
RUN apt-get update && apt-get install -y \
    chromium \
    chromium-driver \
    wget \
    curl \
    unzip \
    && rm -rf /var/lib/apt/lists/*

# 3️⃣ Set environment variables for Selenium
ENV CHROME_BIN=/usr/bin/chromium
ENV CHROMEDRIVER_PATH=/usr/bin/chromedriver

# 4️⃣ Set working directory inside container
WORKDIR /app

# 5️⃣ Copy Python dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# 6️⃣ Copy test script
COPY test_form.py .

# 7️⃣ Command to run the test
CMD ["python", "test_form.py"]
