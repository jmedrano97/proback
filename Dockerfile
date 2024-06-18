FROM python:3.8

# Set unbuffered output for python
ENV PYTHONUNBUFFERED 1

# Create app directory
WORKDIR /app

# Install app dependencies
COPY requirements.txt .
RUN pip install -r requirements.txt

# Bundle app source
COPY . .
# Expose port
EXPOSE 80

# entrypoint to run the django.sh file
ENTRYPOINT ["paython", "manage.py", "makemigrations"]
ENTRYPOINT ["paython", "manage.py", "migrate"]
ENTRYPOINT ["python", "manage.py", "runserver", "0.0.0.0:80"]
