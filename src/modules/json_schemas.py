login_schema = {
    'type': 'object',
    'properties': {
        'login': {'type': 'string', 'pattern': '^[0-9A-z-_]+$'},
        'password': {'type': 'string', 'pattern': '^[0-9A-z-_]+$'}
    },
    'required': ['login', 'password']
}


register_schema = {
    'type': 'object',
    'properties': {
        'login': {'type': 'string', 'pattern': '^[0-9A-z-_]+$'},
        'email': {'type': 'string', 'pattern': '^[0-9A-z-_]+@[0-9A-z-_]+.[0-9A-z]+$'},
        'password': {'type': 'string', 'pattern': '^[0-9A-zА-я-_]+$'},
        'first_name': {'type': 'string', 'pattern': '^[0-9A-zА-я-_]+$'},
        'second_name': {'type': 'string', 'pattern': '^[0-9A-zА-я-_]+$'}
    },
    'required': ['login', 'password', 'first_name', 'second_name', 'email']
}


profile_update_schema = {
    'type': 'object',
    'properties': {
        'first_name': {'type': 'string', 'pattern': '^[0-9A-zА-я-_]+$'},
        'second_name': {'type': 'string', 'pattern': '^[0-9A-zА-я-_]+$'}
    },
    'required': ['first_name', 'second_name']
}


chat_create_schema = {
    'type': 'object',
    'properties': {
        'name': {'type': 'string', 'pattern': '^[0-9A-zА-я-_\s][^\\r\\t\\n\\v\\f]+$'},
    },
    'required': ['name']
}

chat_send_msg_schema = {
    'type': 'object',
    'properties': {
        'name': {'type': 'string', 'pattern': '^[0-9A-z-_]+$'},
    },
    'required': ['name']
}

password_schema = {
    'type': 'object',
    'properties': {
        'password': {'type': 'string', 'pattern': '^[0-9A-zА-я-_]+$'},
    },
    'required': ['password']
}