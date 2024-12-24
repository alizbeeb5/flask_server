from flask import Flask, send_from_directory, request, render_template, redirect, url_for, flash
import os

app = Flask(__name__)
app.secret_key = "your_secret_key"  

# Directory to share
SHARED_FOLDER = "your_shared_folder"


@app.route('/')
def index():
    """Display the HTML interface for listing and uploading files."""
    try:
        files = os.listdir(SHARED_FOLDER)
        return render_template('index.html', files=files)
    except Exception as e:
        flash(f"Error: {str(e)}", "error")
        return render_template('index.html', files=[])

@app.route('/files/<path:filename>')
def get_file(filename):
    """Serve a specific file."""
    try:
        return send_from_directory(SHARED_FOLDER, filename, as_attachment=True)
    except Exception as e:
        flash(f"Error: {str(e)}", "error")
        return redirect(url_for('index'))

@app.route('/upload', methods=['POST'])
def upload_file():
    """Allow file uploads to the shared directory."""
    if 'file' not in request.files:
        flash("No file part in the request", "error")
        return redirect(url_for('index'))
    file = request.files['file']
    if file.filename == '':
        flash("No selected file", "error")
        return redirect(url_for('index'))
    try:
        file.save(os.path.join(SHARED_FOLDER, file.filename))
        flash(f"File '{file.filename}' uploaded successfully!", "success")
        return redirect(url_for('index'))
    except Exception as e:
        flash(f"Error: {str(e)}", "error")
        return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
