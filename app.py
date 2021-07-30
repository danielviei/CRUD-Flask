from app import create_app

settings_module = "config.default"
app = create_app(settings_module)
app.run(host="0.0.0.0", port=5000)