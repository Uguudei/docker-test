FROM oraclelinux:7-slim

# Instant client release
ARG release=19
ARG update=6

# Oracle connection variables
ARG ORACLE_USERNAME
ARG ORACLE_PASSWORD
ARG ORACLE_HOSTNAME
ARG ORACLE_PORT=1521
ARG ORACLE_SERVICE
ENV ORACLE_USERNAME $ORACLE_USERNAME
ENV ORACLE_PASSWORD $ORACLE_PASSWORD
ENV ORACLE_HOSTNAME $ORACLE_HOSTNAME
ENV ORACLE_PORT $ORACLE_PORT
ENV ORACLE_SERVICE $ORACLE_SERVICE

# Install Oracle Instant Client
RUN  yum -y install oracle-release-el7 && \
     yum-config-manager --enable ol7_oracle_instantclient && \
     yum -y install oracle-instantclient${release}.${update}-basic && \
     yum -y install oracle-instantclient${release}.${update}-devel && \
     yum -y install oracle-instantclient${release}.${update}-sqlplus && \
     rm -rf /var/cache/yum

# Install Python
RUN yum install -y python36 && \
    rm -rf /var/cache/yum

# Set working directory
WORKDIR /myapp

# Copy initialization script
COPY script.py /myapp
# Copy source code
COPY src/ /myapp/src

# Install Python dependencies
# requirements.txt file is in src folder
RUN pip3 install -r src/requirements.txt

# Uncomment if the tools package is added
# ENV PATH=$PATH:/usr/lib/oracle/${release}.${update}/client64/bin

CMD exec python3 src/main.py
