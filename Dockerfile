FROM python:3.9
RUN /usr/local/bin/python -m pip install --upgrade pip
WORKDIR /app
COPY . .
RUN pip install -r requirements.txt
RUN python -m spacy download en_core_web_sm
EXPOSE 8501
ENTRYPOINT [ "streamlit", "run" ]
CMD [ "app.py" ]