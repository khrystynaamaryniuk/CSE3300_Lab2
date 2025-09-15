FROM python:3.11-slim

EXPOSE 8080

RUN apt-get update \
  && apt-get clean \
  && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*


RUN groupadd -g 799 nyu && \
    useradd -r -u 999 -g nyu nyu

# Set up a working folder and install the pre-reqs
WORKDIR /app
RUN pip install --no-cache-dir Flask

USER nyu

COPY --chown=nyu:nyu . .

CMD [ "python", "./run.py" ]
