"""
File List Summarizer.

This module defines the `FileListSummarizer` class, which provides a method to summarize
code files in a specified directory.
This summarizer only lists all the code files in the directory recursively.

This class is an implementation of the SummarizerProtocol

Classes:
    FileListSummarizer: A class for summarizing code files in a directory.

"""

from pathlib import Path

from codeinsight.interfaces.summarizer import Summary


class FileListSummarizer:
    """
    File List Summarizer.

    This class provides a method to summarize code files in a specified directory.

    Methods
    -------
        summarize(input_dir: Path) -> Generate the list of files in the directory.

    """

    def summarize(self, input_dir: Path) -> list[Summary]:
        """
        Summarize code files in the specified directory.

        :param input_dir: The directory containing code files to summarize.
        :type input_dir: Path
        :return: A Summary object containing the overall code summary.
        :rtype: Summary
        """
        # List all Python files in the input directory recursively
        code_files = [str(f) for f in input_dir.rglob("*.py")]

        # Join the file paths into a single string for the overall summary
        file_list = "\n".join(code_files)

        # Return a Summary object with an overall summary file path and its content
        return [Summary(path=Path("overall.txt"), data=file_list)]
