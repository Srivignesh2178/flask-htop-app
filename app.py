from flask import Flask
import os
import datetime
import subprocess

app = Flask(__name__)

def get_top_output():
    """Get the output of the 'top' command."""
    try:
        result = subprocess.run(['top', '-b', '-n', '1'], capture_output=True, text=True)
        return result.stdout
    except Exception as e:
        return str(e)

@app.route('/htop')
def htop():
    name = "KOMMURI SRI VIGNESH"  # Replace with your name
    username = os.getenv("USER") or os.getenv("USERNAME") or "Unknown"
    
    # Get server time in IST
    ist_time = datetime.datetime.utcnow() + datetime.timedelta(hours=5, minutes=30)
    formatted_time = ist_time.strftime("%Y-%m-%d %H:%M:%S.%f")

    # Get system top output
    top_output = get_top_output().replace("\n", "<br>")  # Convert newlines to HTML for proper display

    return f"""
    <h1>Name: {name}</h1>
    <h2>Server Time (IST): {formatted_time}</h2>
    <h3>TOP output:</h3>
    <pre>{top_output}</pre>
    """

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
