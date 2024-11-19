# * Creates copies of originally provided samples with filename variations to test unclean file names

import faker
import os
import random
import string
import shutil


def random_capitalise_string(input_string):
    return "".join(map(random.choice, zip(input_string.lower(), input_string.upper())))


def random_remove_characters(input_string):
    transformed_string = input_string.replace(random.choice(input_string[1:]), "", 1)
    return transformed_string


def random_change_characters(input_string):
    transformed_string = input_string.replace(
        random.choice(input_string[1:]), random.choice(string.ascii_lowercase), 1
    )
    return transformed_string


def add_noise_to_string(input_string):
    """
    Function to create a noisy version of a given input string
    """
    random_caps_string = (
        random_capitalise_string(input_string)
        if random.choice([0, 1, 1, 1]) == 1
        else input_string
    )
    random_changed_string = (
        random_change_characters(input_string)
        if random.choice([0, 1, 1, 1]) == 1
        else input_string
    )
    return random_changed_string


if __name__ == "__main__":
    sample_files_path = r"files\provided_samples"
    sample_files_list = [
        file
        for file in os.listdir(sample_files_path)
        if os.path.isfile(os.path.join(sample_files_path, file))
    ]

    edited_filenames_directory = r"files\provided_samples_name_variations"

    for filename in sample_files_list:
        filename_only = os.path.splitext(filename)[0]
        extn = os.path.splitext(filename)[1]
        filename_only_edited = add_noise_to_string(filename_only)
        filename_edited = filename_only_edited + extn
        if filename != filename_edited:
            src = os.path.join(sample_files_path, filename)
            dst = os.path.join(edited_filenames_directory, filename_edited)
            shutil.copyfile(src, dst)
            print(f"{src} successfully copied to {dst}")
