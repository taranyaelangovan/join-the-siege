from werkzeug.datastructures import FileStorage
from src.constants import FILE_TYPE_VARIATIONS


def check_substring(search_string, search_list):
    """
    checks if any of the possible string variations for in search_list are present in the search_string
    """
    return any(substring in search_string for substring in search_list)


def clean_filename(filename: str = ""):
    """
    cleans filename to remove any spaces/underscores/hyphens, and converts to lowercase
    """
    filename_cleaned = (
        filename.replace(" ", "").replace("_", "").replace("-", "").lower()
    )
    return filename_cleaned


def classify_file(file: FileStorage):
    """
    file classification logic
    # * Initially simple rule-based
    # ! Make more robust - add in more rules and classification based on file content
    """

    filename_cleaned = clean_filename(file.filename)

    for key in FILE_TYPE_VARIATIONS:
        if check_substring(filename_cleaned, FILE_TYPE_VARIATIONS[key]):
            return key

    # ! Add in handling for files that have not already been classified - check here for file contents if not already categorised based on name
    # file_bytes = file.read()

    return "unknown file"
