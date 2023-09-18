from pathlib import Path

import pytest

from codeinsight.interfaces.summarizer import Summary
from codeinsight.summarizers.file_list import (
    FileListSummarizer,
)


# Define a fixture to create a temporary directory for testing
@pytest.fixture
def temp_directory(tmp_path):
    return tmp_path


# Define test cases using pytest
def test_empty_directory(temp_directory):
    summarizer = FileListSummarizer()
    input_dir = temp_directory / "empty_directory"
    input_dir.mkdir()

    summaries = summarizer.summarize(input_dir)

    assert (
        len(summaries) == 1
    )  # The result should have a single summary of the file list
    assert isinstance(summaries[0], Summary)  # The result should be a Summary object
    assert summaries[0].data == ""  # The resultant data should be empty


def test_directory_with_files(temp_directory):
    summarizer = FileListSummarizer()
    input_dir = temp_directory / "code_directory"
    input_dir.mkdir()

    # Create some Python files in the directory
    file1 = input_dir / "file1.py"
    file2 = input_dir / "file2.py"
    file1.write_text("print('Hello, World!')")
    file2.write_text("print('Python is awesome!')")

    summaries = summarizer.summarize(input_dir)

    assert len(summaries) == 1  # There should be one summary
    assert isinstance(summaries[0], Summary)  # The result should be a Summary object
    assert summaries[0].path == Path(
        "overall.txt"
    )  # The summary path should be 'overall.txt'
    assert (
        "file1.py" in summaries[0].data
    )  # Check if file content is present in the summary
    assert "file2.py" in summaries[0].data


# Test case for a non-existent input directory
def test_non_existent_directory(temp_directory):
    summarizer = FileListSummarizer()
    input_dir = temp_directory / "non_existent_directory"

    with pytest.raises(FileNotFoundError):
        summarizer.summarize(input_dir)  # Should raise FileNotFoundError


# Test case for a non-directory input path (e.g., a file or special device)
def test_non_directory_input(temp_directory):
    summarizer = FileListSummarizer()
    input_file = temp_directory / "sample_file.txt"
    input_file.touch()

    with pytest.raises(NotADirectoryError):
        summarizer.summarize(input_file)  # Should raise NotADirectoryError


# Test case for a non-readable input directory
def test_non_readable_input_directory(temp_directory: Path):
    summarizer = FileListSummarizer()
    input_dir = temp_directory / "non_readable_directory"
    input_dir.mkdir()

    # Set no permissions on the directory
    input_dir.chmod(0o000)

    with pytest.raises(PermissionError):
        summarizer.summarize(input_dir)  # Should raise PermissionError

    input_dir.rmdir()
