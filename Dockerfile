FROM python:3.8-slim-buster
RUN apt-get update && apt-get install ffmpeg libsm6 libxext6  -y
WORKDIR /app
COPY . .
RUN pip install -r requirements.txt
EXPOSE 80
CMD ["python", "app.py"]