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

def write_value_to_default(key, value):
    config = ConfigParser()
    config.read('config.ini') 

    config['DEFAULT'][key] = value 
    with open('config.ini', 'w') as configfile:
        config.write(configfile)

