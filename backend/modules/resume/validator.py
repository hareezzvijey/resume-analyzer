from pathlib import Path


SUPPORTED_FILE_TYPES = {
    ".pdf": "PDF",
    ".docx": "DOCX",
}


def validate_file_extension(file_name: str) -> str:
    """
    Validate the resume file extension.

    Returns:
        "PDF" or "DOCX"

    Raises:
        ValueError: If the file type is unsupported.
    """

    if not file_name:
        raise ValueError("File name is required.")

    extension = Path(file_name).suffix.lower()

    if extension not in SUPPORTED_FILE_TYPES:
        raise ValueError(
            "Unsupported file type. Only PDF and DOCX files are allowed."
        )

    return SUPPORTED_FILE_TYPES[extension]


def validate_file_content(file_content: bytes) -> None:
    """
    Perform basic validation on uploaded file content.

    Raises:
        ValueError: If the file is empty.
    """

    if not file_content:
        raise ValueError("Uploaded file is empty.")