# cicd-pelican can be used as an image for the gitlab CI/CD pipelines
# build the image with
# docker build --target cicd-pelican -t ektich/cicd-pelican:latest .
FROM python:3.7-alpine as cicd-pelican
RUN apk update && apk add make openssh-client rsync
COPY requirements.txt /
RUN pip install -r /requirements.txt

FROM cicd-pelican
EXPOSE 8000
WORKDIR /workdir
ENTRYPOINT ["/usr/bin/make"]
CMD ["html"]
