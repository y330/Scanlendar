from api import initialize_app

app = initialize_app()

if __name__ == "__main__":
    app.run(debug=True)