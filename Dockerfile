FROM python:3.6-onbuild

EXPOSE 8000

CMD ["gunicorn main:api"]
