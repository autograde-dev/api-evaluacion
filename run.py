from app.app import create_app  # Import the app factory function

app = create_app()  # Create an app instance

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)  # Start the app