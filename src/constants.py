# Valid file extensions
ALLOWED_EXTENSIONS = {"pdf", "png", "jpg", "eml", "msg", "txt", "docx"}

# Valid filename substrings for each file type
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
    # communications
    "email": ["email", ".eml", ".msg"],
    "formal_letter": ["formalletter", "letter"],
    "academic_report": ["academicreport", "acreport", "projectreport"],
    "business_report": [
        "businessreport",
        "annualreport",
        "monthlyreport",
        "annualreport",
        "busreport",
        "companyreport",
    ],
}
