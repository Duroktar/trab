from trabconfig import trabConfig


def test(cfg, config_format=None):
    config = trabConfig(cfg, data=config_format)
    assert config._config_data == {
        'key': 'ABC1234',
        'test2': 'test',
        'Parent2': [
            'child number one',
            'child number two'
        ],
        'Parent': 'child',
        'ip': 'localhost',
        'port': '54657'
    }
    assert config["Parent"] == "child"
    assert config["Parent2"] == [
        'child number one',
        'child number two'
    ]

    config.new('ip', 'localhost')
    config.new('port', '54657')
    config.new('key', 'ABC1234')
    assert config._config_data == {
        'key': 'ABC1234',
        'test2': 'test',
        'Parent2': [
            'child number one',
            'child number two'
        ],
        'Parent': 'child',
        'ip': 'localhost',
        'port': '54657'
    }

    IP = config.get('ip')
    PORT = config.get('port')
    KEY = config.get('key')
    assert (IP, KEY, PORT) == ('localhost', 'ABC1234', '54657')

    config.set('ip', 'newip')
    assert config._config_data == {
        'key': 'ABC1234',
        'test2': 'test',
        'Parent2': [
            'child number one',
            'child number two'
        ],
        'Parent': 'child',
        'ip': 'newip',
        'port': '54657'
    }

    config.new('new key', 'value')
    assert config._config_data == {
        'key': 'ABC1234',
        'test2': 'test',
        'Parent2': [
            'child number one',
            'child number two'
        ],
        'Parent': 'child',
        'ip': 'newip',
        'new key': 'value',
        'port': '54657'
    }

    config.delete('new key')
    assert config._config_data == {
        'key': 'ABC1234',
        'test2': 'test',
        'Parent2': [
            'child number one',
            'child number two'
        ],
        'Parent': 'child',
        'ip': 'newip',
        'port': '54657'
    }

    config.set('ip', 'localhost')
    assert config._config_data == {
        'key': 'ABC1234',
        'test2': 'test',
        'Parent2': [
            'child number one',
            'child number two'
        ],
        'Parent': 'child',
        'ip': 'localhost',
        'port': '54657'
    }

    config.save()

    config.auto_save = True
    config.new("test1", "test")
    config.new("test2", "test")
    config.delete("test")
    config.delete("test1")
    assert config._config_data == {
        'key': 'ABC1234',
        'test2': 'test',
        'Parent2': [
            'child number one',
            'child number two'
        ],
        'Parent': 'child',
        'ip': 'localhost',
        'port': '54657'
    }

    print("Test passed!")


def test_from_yaml(config):
    config = trabConfig.from_yaml(config)
    assert config._config_data == {
        'key': 'ABC1234',
        'test2': 'test',
        'Parent2': [
            'child number one',
            'child number two'
        ],
        'Parent': 'child',
        'ip': 'localhost',
        'port': '54657'
    }
    assert config["Parent"] == "child"
    assert config["Parent2"] == [
        'child number one',
        'child number two'
    ]

    config.new('ip', 'localhost')
    config.new('port', '54657')
    config.new('key', 'ABC1234')
    assert config._config_data == {
        'key': 'ABC1234',
        'test2': 'test',
        'Parent2': [
            'child number one',
            'child number two'
        ],
        'Parent': 'child',
        'ip': 'localhost',
        'port': '54657'
    }

    IP = config.get('ip')
    PORT = config.get('port')
    KEY = config.get('key')
    assert (IP, KEY, PORT) == ('localhost', 'ABC1234', '54657')

    config.set('ip', 'newip')
    assert config._config_data == {
        'key': 'ABC1234',
        'test2': 'test',
        'Parent2': [
            'child number one',
            'child number two'
        ],
        'Parent': 'child',
        'ip': 'newip',
        'port': '54657'
    }

    config.new('new key', 'value')
    assert config._config_data == {
        'key': 'ABC1234',
        'test2': 'test',
        'Parent2': [
            'child number one',
            'child number two'
        ],
        'Parent': 'child',
        'ip': 'newip',
        'new key': 'value',
        'port': '54657'
    }

    config.delete('new key')
    assert config._config_data == {
        'key': 'ABC1234',
        'test2': 'test',
        'Parent2': [
            'child number one',
            'child number two'
        ],
        'Parent': 'child',
        'ip': 'newip',
        'port': '54657'
    }

    config.set('ip', 'localhost')
    assert config._config_data == {
        'key': 'ABC1234',
        'test2': 'test',
        'Parent2': [
            'child number one',
            'child number two'
        ],
        'Parent': 'child',
        'ip': 'localhost',
        'port': '54657'
    }

    config.save()
    assert config.keys() == ['key', 'test2', 'Parent2', 'Parent', 'ip', 'port']

    config.auto_save = True
    config.new("test1", "test")
    config.new("test2", "test")
    config.delete("test")
    config.delete("test1")
    assert config._config_data == {
        'key': 'ABC1234',
        'test2': 'test',
        'Parent2': [
            'child number one',
            'child number two'
        ],
        'Parent': 'child',
        'ip': 'localhost',
        'port': '54657'
    }

    print("Test passed!")

test('config.json', 'dict')
test('config.yml', 'yaml')
test_from_yaml('config.yml')
