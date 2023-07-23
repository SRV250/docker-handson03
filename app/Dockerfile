From python:3.8-alpine
Label author="maijun2"
COPY ./requirements.txt ./requirements.txt
RUN pip install -r requirements.txt
COPY ./ /
CMD ["python","-u", "/app.py"]docker