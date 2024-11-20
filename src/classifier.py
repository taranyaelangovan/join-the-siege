from werkzeug.datastructures import FileStorage
from src.constants import FILE_TYPE_VARIATIONS
from jellyfish import jaro_winkler_similarity
import os


def check_substring(search_string, search_list):
    """
    checks if any of the possible string variations for in search_list are present in the search_string
    """
    return any(substring in search_string for substring in search_list)


def check_similar_substring(search_string, search_list):
    """
    checks if any of the possible string variations for in search_list are present in the search_string
    """

    for substring in search_list:
        print(
            f"Similarity between {search_string} and *{substring}*: {jaro_winkler_similarity(substring,search_string)}"
        )

    return any(
        jaro_winkler_similarity(substring, search_string) > 0.85
        for substring in search_list
    )


def clean_filename(filename: str = ""):
    """
    cleans filename to remove any spaces/underscores/hyphens, and converts to lowercase
    """
    # filename_cleaned = (
    #     filename.replace(" ", "").replace("_", "").replace("-", "").lower()
    # )
    filename_cleaned = "".join(x for x in filename if x.isalpha())
    return filename_cleaned


def classify_file(file: FileStorage):
    """
    file classification logic
    # * Initially simple rule-based
    # ! Make more robust - add in more rules and classification based on file content
    """
    file_extn = os.path.splitext(file.filename)[1]
    filename_cleaned = clean_filename(file.filename)

    # Pass 0: Check Extension
    for key in FILE_TYPE_VARIATIONS:
        if file_extn in FILE_TYPE_VARIATIONS[key]:
            return key

    # Pass 1: Checks if any of the accepted file type variation strings are a substring of the filename
    for key in FILE_TYPE_VARIATIONS:
        if check_substring(filename_cleaned, FILE_TYPE_VARIATIONS[key]):
            return key

    # Pass 2: If not classified in Pass 1, checks if any of the accepted file type variation strings are similar to (JW distance > 0.85) a substring of the filename
    for key in FILE_TYPE_VARIATIONS:
        if check_similar_substring(filename_cleaned, FILE_TYPE_VARIATIONS[key]):
            return key

    # ! Add in handling for files that have not already been classified - check here for file contents if not already categorised based on name
    # file_bytes = file.read()

    return "unknown file"
