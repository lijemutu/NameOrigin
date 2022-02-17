import os
from main import create_app

env = os.environ.get("APIAPP_ENV", "dev")
app = create_app("config.%sConfig" % env.capitalize())
if __name__ == "__main__":
    app.run()
