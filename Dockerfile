FROM public.ecr.aws/lambda/python:3.8

RUN mkdir -p /app
ENV MLFLOW_TRACKING_URI=databricks
COPY ./requirements.txt /app/requirements.txt
COPY ./main.py /app/
RUN python download-model.py
COPY model/ /app/model/
RUN pip install --no-cache-dir --upgrade -r /app/requirements.txt
WORKDIR /app
EXPOSE 8080
CMD [ "main.py" ]
ENTRYPOINT [ "python" ]
