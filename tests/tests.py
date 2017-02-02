from trabconfig import trabConfig


def test(cfg, config_format=None):
    config = trabConfig(cfg, data=config_format)
    print(config)

    print(config["Parent"])
    print(config["Parent2"])

    config.new('ip', 'localhost')
    config.new('port', '54657')
    config.new('key', 'ABC1234')
    print(config)

    IP = config.get('ip')
    PORT = config.get('port')
    KEY = config.get('key')
    print(IP, KEY, PORT)

    config.set('ip', 'newip')
    print(config)
    config.new('new key', 'value')
    print(config)
    config.delete('new key')
    print(config)
    config.set('ip', 'localhost')
    print(config)
    config.save()
    print(config.keys())

    config.auto_save = True
    config.new("test1", "test")
    config.new("test2", "test")
    config.delete("test")
    config.delete("test1")
    print(config)

    print("Test passed!")

test('config.json', 'dict')
test('config.yml', 'yaml')
