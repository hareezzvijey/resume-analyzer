from backend.modules.resume.parser import extract_text
from backend.modules.resume.validator import (
    validate_file_content,
    validate_file_extension,
)


def process_resume(
    file_name: str,
    file_content: bytes
) -> dict:
    """
    Validate and extract text from an uploaded resume.

    Args:
        file_name: Original uploaded file name.
        file_content: Uploaded file contents.

    Returns:
        Dictionary containing resume metadata and extracted text.
    """

    # Step 1: Validate file extension
    file_type = validate_file_extension(file_name)

    # Step 2: Validate file content
    validate_file_content(file_content)

    # Step 3: Extract text
    extracted_text = extract_text(
        file_content,
        file_type
    )

    # Step 4: Return standardized result
    return {
        "file_name": file_name,
        "file_type": file_type,
        "text": extracted_text,
    }