import os

import yaml


def set_env_vars(env_vars):
    """Set environmental variable for importing from Oracle DB"""
    os.environ['NLS_LANG'] = env_vars['NLS_LANG']
    os.environ['LD_LIBRARY_PATH'] = env_vars['LD_LIBRARY_PATH']
    os.environ['ORACLE_HOME'] = env_vars['ORACLE_HOME']
    os.environ['TNS_ADMIN'] = env_vars['TNS_ADMIN']


def set_config():
    """Following checks whether config.yaml exists or not.
    If config.yaml exists, the code is most like working development environment.
    If config.yaml not exists, the code is working in production environment.
    """
    if os.path.exists('src/config/config.yaml'):
        with open('src/config/config.yaml', 'r') as yml_file:
            config = yaml.load(yml_file, Loader=yaml.BaseLoader)
        if 'os_env' in config:
            set_env_vars(config['os_env'])
        return config['oracle']
    else:
        # Following variable names are same as ones in the config.yaml
        oracle_credentials = {
            'username': os.getenv('ORACLE_USERNAME'),
            'password': os.getenv('ORACLE_PASSWORD'),
            'host': os.getenv('ORACLE_HOSTNAME'),
            'port': os.getenv('ORACLE_PORT'),
            'service_name': os.getenv('ORACLE_SERVICE')
        }
        return oracle_credentials


def set_oracle_connection():
    """ Build oracle connection string for SQL alchemy engine
    Args:
        username, password, oracle db host url, port number, service name

    Returns:
        db_engine_path: oracle connection string
    """
    config = set_config()
    dialect = 'oracle'
    sql_driver = 'cx_oracle'
    username = config['username']
    password = config['password']
    host = config['host']
    port = config['port']
    service = config['service_name']
    db_engine_path = dialect + '+' + sql_driver + '://' + username + ':' + password + '@' + host + ':' + str(
        port) + '/?service_name=' + service
    return db_engine_path
