FROM python:3-slim

RUN useradd me

COPY app.py app
RUN chmod +x app

USER me
ENTRYPOINT ["./app"]
CMD ["--help"]
