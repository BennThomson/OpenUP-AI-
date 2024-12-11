# Base image
FROM python:3.13-slim as base

# Set environment variables
ENV PYTHONUNBUFFERED=1

# Install system dependencies
RUN apt-get update && apt-get install --no-install-recommends -y \
  build-essential \
  libpq-dev \
  curl \
  cron \
  procps \
  git \
  && apt-get clean \
  && rm -rf /var/lib/apt/lists/*

# Set working directory
WORKDIR /opt/app/

# Upgrade pip and install dependencies
COPY requirements.txt .
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

COPY ./entrypoint.sh /opt/entrypoint.sh
RUN chmod +x /opt/entrypoint.sh
ENTRYPOINT ["/opt/entrypoint.sh"]

# Local environment stage
FROM base as local

# Copy project files
COPY . .

# Command to run Django development server
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]

# Live environment stage
FROM base as live

# Copy project files
COPY . .

# Command to run Django development server (can be changed for production)
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
