FROM oraclelinux:7-slim

# Instant client release
ARG release=19
ARG update=6

# Install Oracle Instant Client
RUN  yum -y install oracle-release-el7 && \
     yum-config-manager --enable ol7_oracle_instantclient && \
     yum -y install oracle-instantclient${release}.${update}-basic && \
     rm -rf /var/cache/yum

# Download and install conda
RUN curl -o /tmp/miniconda.sh https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh && \
    /bin/bash /tmp/miniconda.sh -b -p /opt/conda && \
    rm /tmp/miniconda.sh && \
    # /opt/conda/bin/conda clean -tipsy && \
    ln -s /opt/conda/etc/profile.d/conda.sh /etc/profile.d/conda.sh && \
    echo ". /opt/conda/etc/profile.d/conda.sh" >> ~/.bashrc && \
    echo "conda activate base" >> ~/.bashrc && \
    find /opt/conda/ -follow -type f -name '*.a' -delete && \
    find /opt/conda/ -follow -type f -name '*.js.map' -delete && \
    /opt/conda/bin/conda clean -afy

# Add conda location to Path to activate conda
ENV PATH /opt/conda/bin:$PATH

# Set working directory
WORKDIR /myapp

# Copy requirements file
COPY src/requirements.txt /myapp

# Use to install conda package
# RUN conda install -y -q -c conda-forge implicit==0.4.2

# Install Python dependencies via pip
RUN pip install --no-cache-dir -r requirements.txt

# Copy initialization script
COPY script.py /myapp
# Copy source code
COPY src/ /myapp/src

RUN mkdir logs

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

# Execute command
RUN ["python3", "script.py"]
