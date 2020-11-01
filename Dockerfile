FROM python:3.8
COPY .  /flask_project
WORKDIR /flask_project
RUN pip install -r requirements.txt
HEALTHCHECK --interval=5s \
			--timeout=5s \
			CMD curl -f http://127.0.0.1:8000 || exit 1
EXPOSE  8000
CMD ["python3", "flask_project/app.py"]


