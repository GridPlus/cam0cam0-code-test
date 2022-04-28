from configparser import ConfigParser 

def getHostUrl():
    config = ConfigParser()
    config.read('config.ini') 
    
    return config['host']['URL']

def getHostUserName():
    config = ConfigParser()
    config.read('config.ini') 
    
    return config['host']['UserName']

def getHostPassword():
    config = ConfigParser()
    config.read('config.ini') 
    
    return config['host']['Password']

def getCurrentHSMVersion():
    config = ConfigParser()
    config.read('config.ini')

    return config['DEFAULT']['CurrentHSMVersion']

def getCurrentGCEVersion():
    config = ConfigParser() 
    config.read('config.ini')

    return config['DEFAULT']['CurrentGCEVersion'] 

def saveConfigToDefault(newConfigValues):
    config = ConfigParser()
    config.read('config.ini') 

    if 'CurrentGCEVersion' in newConfigValues:
        config['DEFAULT']['CurrentGCEVersion'] = newConfigValues['CurrentGCEVersion']
    if 'CurrentHSMVersion' in newConfigValues:
        config['DEFAULT']['CurrentHSMVersion'] = newConfigValues['CurrentHSMVersion']

    config.write('config.ini')

