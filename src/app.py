# app driver code

from flask import Flask, request, jsonify

from src.classifier import classify_file
from src.constants import ALLOWED_EXTENSIONS

app = Flask(__name__)


def allowed_file(filename):
    """
    checks if a file name has a valid extension
    """
    return "." in filename and filename.rsplit(".", 1)[1].lower() in ALLOWED_EXTENSIONS


@app.route("/classify_file", methods=["POST"])
def classify_file_route():

    # Checks if file exists
    if "file" not in request.files:
        return jsonify({"error": "No file part in the request"}), 400

    # Checks for blank file names
    file = request.files["file"]
    if file.filename == "":
        return jsonify({"error": "No selected file"}), 400

    # Checks for unallowed file types.extensions
    if not allowed_file(file.filename):
        return jsonify({"error": f"File type not allowed"}), 400

    # If none of the above error categories, classifies file into types based on rules in classifier.classify_file
    file_class = classify_file(file)
    return jsonify({"file_class": file_class}), 200


if __name__ == "__main__":
    app.run(debug=True)
