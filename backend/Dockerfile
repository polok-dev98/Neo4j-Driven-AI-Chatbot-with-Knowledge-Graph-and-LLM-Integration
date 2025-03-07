# Use a base image with Python 3.9-slim
FROM python:3.9-slim

# Install system dependencies for libmagic
RUN apt-get update && apt-get install -y libmagic1

# Set the final working directory for the FastAPI app
WORKDIR /app

# Copy only the gtemodel.py file and requirements.txt to the temporary directory
COPY requirements.txt . 

# Install Python dependencies
RUN pip install --upgrade pip && pip install --no-cache-dir -r requirements.txt

COPY  gteModel.py .
# Run the gtemodel.py script
RUN python gteModel.py

# Copy all FastAPI app files to the /app directory
COPY . .

# Expose port
EXPOSE 5507

# Start FastAPI app with Uvicorn
CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "5507"]

