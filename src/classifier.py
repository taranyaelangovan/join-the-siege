from werkzeug.datastructures import FileStorage
from src.constants import FILE_TYPE_VARIATIONS
from jellyfish import jaro_winkler_similarity
import os
import docx
import pickle


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
    filename_cleaned = "".join(x for x in filename if x.isalpha())
    return filename_cleaned


def classify_file_by_contents(file: FileStorage):
    """
    classify file using trained Logistic Regression model
    """
    print(file.filename)
    if file.filename.endswith(".txt"):
        file_contents = file.stream.read()
    if file.filename.endswith(".docx"):
        doc = docx.Document(file)
        word_text = "\n".join([p.text for p in doc.paragraphs])
        file_contents = word_text

    tfidf_vect = pickle.load(open(r"files/trained_models/tfidf_vectoriser.sav", "rb"))
    predict_file_tfidf = tfidf_vect.transform([file_contents])

    lr_regression = pickle.load(
        open(r"files/trained_models/logistic_regression_acc_97_3.sav", "rb")
    )
    encoded_prediction = lr_regression.predict(predict_file_tfidf)

    encoding_map = pickle.load(open(r"files/trained_models/encoding_map.sav", "rb"))
    prediction = encoding_map[encoded_prediction[0]]

    return prediction


def classify_file(file: FileStorage):
    """
    file classification logic
    Pass 1: Checks file extension
    Pass 2: Checks file name for valid identifying substrings
    Pass 3: Checks if file name has a high similarity with any valid identifying substring
    Pass 4: If file is .docx/.txt, loads its contents and uses Logistic Regression to predict its type
    """
    file_extn = os.path.splitext(file.filename)[1]
    filename_cleaned = clean_filename(file.filename)

    # Pass 1: Check Extension
    for key in FILE_TYPE_VARIATIONS:
        if file_extn in FILE_TYPE_VARIATIONS[key]:
            return key

    # Pass 2: Checks if any of the accepted file type variation strings are a substring of the filename
    for key in FILE_TYPE_VARIATIONS:
        if check_substring(filename_cleaned, FILE_TYPE_VARIATIONS[key]):
            return key

    # Pass 3: If not classified in Pass 2, checks if any of the accepted file type variation strings are similar to (JW distance > 0.85) a substring of the filename
    for key in FILE_TYPE_VARIATIONS:
        if check_similar_substring(filename_cleaned, FILE_TYPE_VARIATIONS[key]):
            return key

    # Pass 4: If not classified in Passes 1 or 2, gets the contents of a file if it is either a .txt or .docx file, and predicts its type using the trained Logistic Regression model saved
    if file_extn in [".docx", ".txt"]:
        return classify_file_by_contents(file)

    return "unknown file"
