from configparser import ConfigParser 

def get_host_url():
    config = ConfigParser()
    config.read('config.ini') 
    
    return config['host']['URL']

def get_host_user_name():
    config = ConfigParser()
    config.read('config.ini') 
    
    return config['host']['UserName']

def get_host_password():
    config = ConfigParser()
    config.read('config.ini') 
    
    return config['host']['Password']

def get_current_hsm_version():
    config = ConfigParser()
    config.read('config.ini')

    return config['DEFAULT']['CurrentHSMVersion']

def get_current_gce_version():
    config = ConfigParser() 
    config.read('config.ini')

    return config['DEFAULT']['CurrentGCEVersion'] 

def save_config_to_default(newConfigValues):
    config = ConfigParser()
    config.read('config.ini') 

    if 'CurrentGCEVersion' in newConfigValues:
        config['DEFAULT']['CurrentGCEVersion'] = newConfigValues['CurrentGCEVersion']
    if 'CurrentHSMVersion' in newConfigValues:
        config['DEFAULT']['CurrentHSMVersion'] = newConfigValues['CurrentHSMVersion']

    config.write('config.ini')

