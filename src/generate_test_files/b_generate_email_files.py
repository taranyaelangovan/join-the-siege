from faker import Faker
import random
import os
import pathlib


def generate_email_message(faker):

    sender = faker.name()
    sender_email = sender + "@" + faker.domain_name()
    sender_job = faker.job()
    sender_phone = faker.phone_number()
    receiver = faker.name()
    receiver_email = receiver + "@" + faker.domain_name()
    datetime = faker.date_time_this_year().strftime("%a, %d %b %Y %H:%M:%S %z")
    subject = faker.sentence()
    contents = faker.paragraph(nb_sentences=random.choice(range(5, 50)))

    email_contents = f"""
From: {sender} <{sender_email}>
To: {receiver} <{receiver_email}>
CC: None
BCC: None
Date: {datetime}
Subject: {subject}

Dear {receiver}

{contents}

{sender}
{sender_job}
{sender_email} | {sender_phone}
    """

    return email_contents


def create_email_files(
    faker,
    txt_only=0,
    email_output_directory=r"files\synthesised_emails",
    num_emails_to_generate=10,
    mask_flag=0,
):
    if txt_only == 0:
        email_extns = [".txt"]
    else:
        email_extns = [".msg", ".eml", ".txt"]

    for i in range(0, num_emails_to_generate):
        email = generate_email_message(faker)

        if mask_flag == 0:
            prefix = "email"
        else:
            prefix = "file"

        email_filename = f"{prefix}_{faker.random_number()}"
        email_save_path = os.path.join(
            email_output_directory, email_filename
        ) + random.choice(email_extns)

        with open(email_save_path, "w") as f:
            f.write(email)


if __name__ == "__main__":

    faker = Faker()

    # 1. creating files and saving to files/synthesised_emails/

    # create_email_files(faker, 5)

    # 2. creating training data and saving to files/synthesised_training_data/eml_txt/

    # email_output_dir = r"files\synthesised_training_data\eml_txt"
    # pathlib.Path(email_output_dir).mkdir(parents=True, exist_ok=True)

    # num_files = 250

    # create_email_files(
    #     faker,
    #     email_output_directory=email_output_dir,
    #     num_emails_to_generate=num_files,
    #     mask_flag=1,
    # )

    # 3. creating testing data to be used for predicton and saving to files/synthesised_test_data/eml_test_files

    email_output_dir = r"files\synthesised_test_data\eml_test_files"
    pathlib.Path(email_output_dir).mkdir(parents=True, exist_ok=True)

    num_files = 10

    create_email_files(
        faker,
        email_output_directory=email_output_dir,
        num_emails_to_generate=num_files,
        mask_flag=1,
    )
