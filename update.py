import config

class Update:
    def __init__(self, env, content, version):
        self.env = env 
        self.content = content 
        self.version = version 

    def apply(self):
        """Updates the config file with the version in the update and prints the contents"""
        key =  f'Current{self.env}Version'
        config.write_value_to_default(key, self.version)
        print(self.content)
