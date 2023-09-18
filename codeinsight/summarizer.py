"""
Code Insight Summarizer Module.

This module defines a function for summarizing code files in a given directory.

Functions:
    summarize(input_dir: Path) -> dict[Path, str]:
        Summarize code files in the specified directory and return a dictionary
        containing file paths and their summaries.

"""

from pathlib import Path


def summarize(input_dir: Path) -> dict[Path, str]:
    """
    Summarize code files in the specified directory.

    :param input_dir: The directory containing code files to summarize.
    :type input_dir: Path
    :return: A dictionary with file paths as keys and code summaries as values.
    :rtype: dict[Path, str]
    """
    # List all Python files in the input directory recursively
    code_files = [str(f) for f in input_dir.rglob("*.py")]

    # Join the file paths into a single string for the overall summary
    overall_summary = "\n".join(code_files)

    # Return a dictionary with an overall summary file path and its content
    return {Path("overall.txt"): overall_summary}
