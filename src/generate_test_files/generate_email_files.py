from faker import Faker
import random
import os
from faker_file.providers.docx_file import DocxFileProvider
from faker_file.storages.filesystem import FileSystemStorage


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


def create_email_files(faker, num_emails_to_generate=10):

    email_extns = [".msg", ".eml", ".txt"]
    email_output_directory = r"files\emails"

    for i in range(0, num_emails_to_generate):
        email = generate_email_message(faker)
        email_filename = f"email_{faker.random_number()}"
        email_save_path = os.path.join(
            email_output_directory, email_filename
        ) + random.choice(email_extns)
        with open(email_save_path, "w") as f:
            f.write(email)


def generate_word_document(faker):
    faker.docx_file(
        storage=FileSystemStorage(
            root_path=os.getcwd(), rel_path=r"files\word_documents", prefix="doc"
        )
    )


def create_word_files(faker, num_files=10):
    for i in range(0, num_files):
        generate_word_document(faker)


if __name__ == "__main__":

    faker = Faker()
    faker.add_provider(DocxFileProvider)

    create_word_files(faker, 5)

    #! Generate different types of word files based on different templates
    #! Generate Excel files
    #! General PPTX files
