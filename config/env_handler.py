from configparser import ConfigParser

# read configuraton file
config_file = "./config.ini"
config = ConfigParser()
config.read(config_file)


def env(section, key, value=None):
    """
    Sets or returns config file section, key value
    parameters
    ----------
    section: The config file section
    key: A key in the selected section
    value: desired value for the selected key, if not set, returns the key's
    current value.
    """
    if value == None:
        return config[section][key]
    else:
        config[section][key] = value
        return config
