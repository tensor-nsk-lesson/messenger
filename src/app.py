from flask import Flask

app = Flask(__name__, static_url_path='')

# Parse Flask configuration
from config import CONFIGURATION
app.config.from_object(CONFIGURATION)

#  Auth Manager
from modules.AuthManager.routes import auth_module
app.register_blueprint(auth_module)

#  Profile Manager
from modules.ProfileManager.routes import profile_module
app.register_blueprint(profile_module, url_prefix='/profile')

#  Messages Manager
from modules.MessagesManager.routes import messages_module
app.register_blueprint(messages_module, url_prefix='/chat')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True, threaded=True)