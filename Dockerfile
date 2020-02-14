FROM oraclelinux:7-slim

# ARG release=19
# ARG update=5

RUN  yum -y install oracle-release-el7 && \
     yum-config-manager --enable ol7_oracle_instantclient && \
     yum -y install oracle-instantclient19.5-basic && \
     # yum -y install oracle-instantclient${release}.${update}-basic oracle-instantclient${release}.${update}-devel oracle-instantclient${release}.${update}-sqlplus && \
     # yum -y install oracle-instantclient${release}.${update}-basic && \
     rm -rf /var/cache/yum

# Uncomment if the tools package is added
# ENV PATH=$PATH:/usr/lib/oracle/${release}.${update}/client64/bin

# CMD ["sqlplus", "-v"]
