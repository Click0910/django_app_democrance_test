FROM python:3.10-slim-buster


# Set work directory
WORKDIR /usr/src/app

# Install dependencies
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

# Copy project
COPY . .

# Expose the port the app runs on
EXPOSE 8000

CMD ["python", "/usr/src/app/myproject/manage.py", "runserver", "0.0.0.0:8000"]

