FROM python:3
ENV PYTHONUNBUFFERED 1

RUN mkdir /code
WORKDIR /code
COPY requirements.txt /code/
RUN pip install -r requirements.txt
COPY . /code/


RUN	apt-get update && \
    apt-get install -y --no-install-recommends \
    openjdk-8-jdk && \
    apt-get clean;


# INSTALLING GRADLE
FROM openjdk:8
RUN wget -q https://services.gradle.org/distributions/gradle-3.3-bin.zip \
    && unzip gradle-3.3-bin.zip -d /opt \
 	&& rm gradle-3.3-bin.zip
ENV GRADLE_HOME /opt/gradle-3.3
ENV PATH $PATH:/opt/gradle-3.3/bin


# python file that handles docker stuff for now.
#COPY test.py /code/
#CMD ["test.py"]
