from app import create_app

app = create_app()

if __name__ == '__main__':  # Corrected the condition here
    app.run(debug=True, use_reloader=True)
