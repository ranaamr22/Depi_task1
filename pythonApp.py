from flask import Flask, render_template
from datetime import datetime  # Import datetime module

# Create a Flask application
app = Flask(__name__)

# Define a route and a view function
@app.route('/')
def index():
    now = datetime.now()  # Get current date and time
    current_time = now.strftime("%Y-%m-%d %H:%M:%S")  # Format date and time
    return render_template('index.html', current_time=current_time)

# Run the application
if __name__ == '__main__':
    app.run(debug=True)
