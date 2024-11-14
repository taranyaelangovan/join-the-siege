from werkzeug.datastructures import FileStorage


def classify_file(file: FileStorage):
    """
    file classification logic
    # * Initially simple rule-based
    # ! Make more robust - add in more rules and classification based on file content
    """
    filename = file.filename.lower()
    # file_bytes = file.read()

    if "drivers_license" in filename:
        return "drivers_licence"

    if "bank_statement" in filename:
        return "bank_statement"

    if "invoice" in filename:
        return "invoice"

    return "unknown file"
