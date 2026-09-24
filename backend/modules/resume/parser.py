import io

import pymupdf
from docx import Document


def extract_text_from_pdf(file_content: bytes) -> str:
    """
    Extract text from a PDF file.

    Args:
        file_content: PDF file as bytes.

    Returns:
        Extracted text.

    Raises:
        ValueError: If the PDF cannot be read.
    """

    try:
        document = pymupdf.open(
            stream=file_content,
            filetype="pdf"
        )

        pages = []

        for page in document:
            text = page.get_text()

            if text:
                pages.append(text)

        document.close()

        extracted_text = "\n".join(pages).strip()

        if not extracted_text:
            raise ValueError(
                "No readable text was found in the PDF."
            )

        return extracted_text

    except ValueError:
        raise

    except Exception as error:
        raise ValueError(
            "Unable to read the PDF file."
        ) from error


def extract_text_from_docx(file_content: bytes) -> str:
    """
    Extract text from a DOCX file.

    Args:
        file_content: DOCX file as bytes.

    Returns:
        Extracted text.

    Raises:
        ValueError: If the DOCX cannot be read.
    """

    try:
        document = Document(io.BytesIO(file_content))

        paragraphs = []

        for paragraph in document.paragraphs:
            text = paragraph.text.strip()

            if text:
                paragraphs.append(text)

        extracted_text = "\n".join(paragraphs).strip()

        if not extracted_text:
            raise ValueError(
                "No readable text was found in the DOCX file."
            )

        return extracted_text

    except ValueError:
        raise

    except Exception as error:
        raise ValueError(
            "Unable to read the DOCX file."
        ) from error


def extract_text(file_content: bytes, file_type: str) -> str:
    """
    Extract text based on the validated file type.

    Args:
        file_content: File contents as bytes.
        file_type: "PDF" or "DOCX".

    Returns:
        Extracted resume text.
    """

    if file_type == "PDF":
        return extract_text_from_pdf(file_content)

    if file_type == "DOCX":
        return extract_text_from_docx(file_content)

    raise ValueError(
        f"Unsupported file type: {file_type}"
    )