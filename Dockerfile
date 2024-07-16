FROM python:3.9
COPY . /app
WORKDIR /app 
RUN pip install -r requirement.txt
EXPOSE 5000
ENTRYPOINT [ "python3" ]
CMD [ "app.py" ]
