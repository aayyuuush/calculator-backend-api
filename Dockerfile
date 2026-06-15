# Base Python Image
FROM python:3.10-slim

# Set Working Directory
WORKDIR /app

# Copy requirements first
COPY requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy entire project
COPY . .

# Expose FastAPI port
EXPOSE 7860

# Run FastAPI server
CMD ["uvicorn", "app.app:app", "--host", "0.0.0.0", "--port", "7860"]