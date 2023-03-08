# Use an official Python runtime as a parent image
FROM python:3.9

# Copy the requirements file into the container
COPY requirements.txt .

# Update the container
RUN apt-get update && apt-get upgrade -y

# Install any needed packages specified in requirements.txt
RUN pip3 install -r requirements.txt

# Install gunicorn
RUN pip3 install gunicorn openpyxl

# Copy app source code into the container
COPY . ./code/

# Set the working directory to /code
WORKDIR /code/

# Set the environment variables
ENV PYTHONPATH /code

# Expose port 8000
ENV GUNICORN_CMD_ARGS "--bind=0.0.0.0:8050 --workers=2 --thread=4 --worker-class=gthread --forwarded-allow-ips='*' --access-logfile -"

# Run app.py when the container launches
CMD ["gunicorn", "app:server"]