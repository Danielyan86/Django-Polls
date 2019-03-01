FROM python:3.7.2-slim
RUN pip install django
WORKDIR /app_new
COPY . /app_new
#EXPOSE 8000
CMD ["python", "manage.py","runserver", "0.0.0.0:8000"]