# Use the official Python image as our base
FROM python:3.13-slim

# Set the working directory inside the container
WORKDIR /app

# Copy the requirements file into the container
COPY requirements.txt .

# Install the required Python packages
RUN pip install --no-cache-dir -r requirements.txt

# Copy the sticky_notes subfolder into the container
COPY sticky_notes/ .

# Tell Docker which port our app will run on
EXPOSE 8000

# The command to start the Django app when the container runs
CMD ["python", "manage.py", "runserver", "127.0.0.1:8000"]