FROM mcr.microsoft.com/vscode/devcontainers/miniconda:0-3

# Set Python timezone
ENV TZ "Asia/Ulaanbaatar"

# [Optional] Uncomment this section install Oracle instant client
# OS packages necessary for Oracle instant client
RUN apt-get update && export DEBIAN_FRONTEND=noninteractive && \
    apt-get -y install --no-install-recommends libaio1 && \
    apt-get -y clean
# Add Oracle instant client location to Path
ENV PATH /opt/oracle/instantclient_21_3:$PATH
ENV LD_LIBRARY_PATH /opt/oracle/instantclient_21_3:$LD_LIBRARY_PATH
# Set Oracle language settings
ENV NLS_LANG "AMERICAN_AMERICA.AL32UTF8"
# Install Oracle instant client
RUN mkdir /opt/oracle && cd /opt/oracle && \
    wget -q --show-progress "https://download.oracle.com/otn_software/linux/instantclient/213000/instantclient-basic-linux.x64-21.3.0.0.0.zip" -O instant_client.zip && \
    unzip instant_client.zip && rm instant_client.zip
# [Optional] Uncomment this section to install Oracle SQL Plus. It requires Oracle instant client
# RUN cd /opt/oracle && \
#     wget  -q --show-progress "https://download.oracle.com/otn_software/linux/instantclient/213000/instantclient-sqlplus-linux.x64-21.3.0.0.0.zip" -O sqlplus.zip && \
#     unzip sqlplus.zip && rm sqlplus.zip

# Copy environment.yml (if found) to a temp location so we update the environment. Also
# copy "noop.txt" so the COPY instruction does not fail if no environment.yml exists.
COPY .devcontainer/environment.yml* .devcontainer/noop.txt /tmp/conda-tmp/
RUN if [ -f "/tmp/conda-tmp/environment.yml" ]; then umask 0002 && /opt/conda/bin/conda env update -n base -f /tmp/conda-tmp/environment.yml; fi \
    && rm -rf /tmp/conda-tmp

# [Optional] Uncomment to install a different version of Python than the default
# RUN conda install -y python=3.6 \
#     && pip install --no-cache-dir pipx \
#     && pipx reinstall-all

# [Optional] Uncomment this section to install additional OS packages.
# RUN apt-get update && export DEBIAN_FRONTEND=noninteractive \
#     && apt-get -y install --no-install-recommends <your-package-list-here>