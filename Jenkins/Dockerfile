FROM jenkins/jenkins:lts-jdk11

USER root
RUN echo 'APT::Install-Suggests "0";' >> /etc/apt/apt.conf.d/00-docker && \
  echo 'APT::Install-Recommends "0";' >> /etc/apt/apt.conf.d/00-docker && \
  echo 'JAVA_ARGS=\"-Djenkins.install.runSetupWizard=false\"' >> /etc/default/jenkins && \
  DEBIAN_FRONTEND=noninteractive apt update && \
  apt install -y \
    grep \
    groovy \
    vim \
    wget \
    python3 \
    python3-pip

USER jenkins
WORKDIR /tmp
RUN wget https://raw.githubusercontent.com/jenkinsci/jenkins/master/core/src/main/resources/jenkins/install/platform-plugins.json && \
  wget https://github.com/jenkinsci/plugin-installation-manager-tool/releases/download/2.12.3/jenkins-plugin-manager-2.12.3.jar && \
  grep suggested platform-plugins.json | cut -d\" -f 4 | tee suggested-plugins.txt && \
  /usr/bin/env java -jar ./jenkins-plugin-manager-2.12.3.jar \
  --verbose \
  --plugin-download-directory=/var/jenkins_home/plugins \
  --plugin-file=./suggested-plugins.txt

