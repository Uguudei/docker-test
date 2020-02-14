FROM oraclelinux:7-slim

ARG release=19
ARG update=5

# Install Oracle Instant Client
RUN  yum -y install oracle-release-el7 && \
     yum-config-manager --enable ol7_oracle_instantclient && \
     yum -y install oracle-instantclient${release}.${update}-basic oracle-instantclient${release}.${update}-devel oracle-instantclient${release}.${update}-sqlplus && \
     rm -rf /var/cache/yum

# Install Python
RUN yum install -y python36 && \
    rm -rf /var/cache/yum

RUN python3.6 -m pip install -r requirement.txt
CMD pwd
WORKDIR /myapp
CMD pwd
COPY . /myapp

# Uncomment if the tools package is added
# ENV PATH=$PATH:/usr/lib/oracle/${release}.${update}/client64/bin

CMD ["sqlplus", "-v"]
CMD exec python3.7 main.py
