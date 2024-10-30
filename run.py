from app import create_app

# creates an instance of the web app
app = create_app()

# run the web app if run.py is executed
if __name__ == "__main__":
  app.run(debug=True)

