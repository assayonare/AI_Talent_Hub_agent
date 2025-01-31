FROM python:3.9.21-slim

# Set env vars
ENV \
    # Disable buffers in stdout and stderr
    PYTHONUNBUFFERED=1 \
    # Prevents python creating .pyc files
    PYTHONDONTWRITEBYTECODE=1 \
    # PIP optimization
    PIP_NO_CACHE_DIR=on \
    PIP_DISABLE_PIP_VERSION_CHECK=on \
    PIP_DEFAULT_TIMEOUT=100

# Set workdir
WORKDIR /app

# Install system dependencies first
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    curl \
    && rm -rf /var/lib/apt/lists/*

# Copy reqs
COPY requirements.txt .

# Install reqs
RUN pip install --upgrade pip && pip install -r requirements.txt

# Copy project files
COPY . .

# Expose port
EXPOSE 8080

# Run app
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8080"]