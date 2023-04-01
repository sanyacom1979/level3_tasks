FROM python:3.8-slim
COPY . calc_short_distance/
WORKDIR /calc_short_distance
RUN pip install -r requirements.txt
CMD ["python", "main.py"]