# Use a LTS Ubuntu version as parent image
FROM  ubuntu:18.04
LABEL maintainer "path-help@sanger.ac.uk"
ENV   BUILD_DIR /opt/remove_blocks_from_aln

# System dependencies
RUN   apt-get update && apt-get install --no-install-recommends -y \
     python2.7 \
     python2.7-dev \
     python-pip \
     python-setuptools \
     locales

# Set locale
RUN   sed -i -e 's/# \(en_GB\.UTF-8 .*\)/\1/' /etc/locale.gen \
     && touch /usr/share/locale/locale.alias \
     && locale-gen
ENV   LANG     en_GB.UTF-8
ENV   LANGUAGE en_GB:en
ENV   LC_ALL   en_GB.UTF-8

# Install the software
RUN   mkdir -p ${BUILD_DIR}
COPY  . ${BUILD_DIR}
RUN   cd ${BUILD_DIR} \
     && python setup.py test \
     && python setup.py install
