From python:3.8-alpine
Label author="maijun2@gmail.com"
COPY ./requirements.txt ./requirements.txt
RUN pip install -r requirements.txt
COPY ./ /
ENV PORT 8080
CMD ["python","-u", "/app.py"]docker