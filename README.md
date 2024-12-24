# Flask File Server

This Flask application provides a simple file server with a web-based interface, allowing users to upload, download, and browse files in a shared directory. It is designed to make file sharing easy across devices, such as accessing files on an iPad.

## Features
- **File Listing:** View a list of all files in the shared directory.
- **File Download:** Download files directly through the web interface.
- **File Upload:** Upload files to the shared directory through a simple form.

## Requirements
- Python 3.7+
- Flask

## Setup

1. **Clone or Download the Repository**
   ```bash
   git clone github.com/alizbeeb5/flask_server
   cd flask_server
   ```

2. **Install Dependencies**
   Install Flask using pip:
   ```bash
   pip install flask
   ```

3. **Set Up the Shared Folder**
   Update the `SHARED_FOLDER` variable in `flask_server.py` to the directory you want to share. For example:
   ```python
   SHARED_FOLDER = r"C:\Users\YourName\SharedFolder"
   ```

4. **Run the Server**
   Start the Flask app:
   ```bash
   python flask_server.py
   ```

5. **Access the App**
   Open your browser and visit:
   ```
   http://<your-computer-ip>:5000
   ```
   Replace `<your-computer-ip>` with the local IP address of your computer.

## File Structure
```
flask_server/
├── flask_server.py       # Main application file
├── templates/
│   └── index.html        # HTML interface for the app
└── README.md             # Documentation
```

## Usage

### Upload Files
1. Open the app in your browser.
2. Use the "Upload File" section to select a file and upload it to the shared directory.

### Download Files
1. View the list of files on the main page.
2. Click on a file name to download it.

## Notes
- **Security:** This app does not include authentication. Use it only in secure and trusted networks.
- **Customization:** You can enhance the app with features like authentication or better error handling as needed.

## License
This project is open-source and available under the MIT License.

