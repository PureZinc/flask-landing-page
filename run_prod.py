from app import create_app

app = create_app(production=True)

if __name__ == '__main__':
    app.run(debug=False)
