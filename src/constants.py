# Valid file extensions
# ! Add extensions here to allow further file classification
ALLOWED_EXTENSIONS = {"pdf", "png", "jpg"}

# Valid filename substrings for each file type
# ! Add further file types in different industries
FILE_TYPE_VARIATIONS = {
    "bank_statement": ["bankstatment", "bankstmt", "bankstm", "bankstate", "bankst"],
    "drivers_license": [
        "driverslicense",
        "driverslicence",
        "driverlicense",
        "drvlicense",
        "driverslsc",
    ],
    "invoice": ["invoice", "inv", "invc"],
}
