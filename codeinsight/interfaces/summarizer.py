"""
Code Summarization Protocol.

This module defines a protocol and Pydantic model for code summarization. The
protocol, SummarizerProtocol, defines the contract that concrete classes must
follow to implement code summarization logic. The Pydantic model, Summary,
represents the structure of code summaries.

Classes:
    Summary(BaseModel): Pydantic model for code summaries.
    SummarizerProtocol(Protocol): Protocol for code summarization.

"""

from pathlib import Path
from typing import Protocol

from pydantic import BaseModel


class Summary(BaseModel):
    """
    Summary Model.

    Represents a code summary consisting of a file path and associated summary data.

    Attributes
    ----------
        path (Path): The file path for the summarized code.
        data (str): The code summary data.
    """

    path: Path
    data: str


class SummarizerProtocol(Protocol):
    """
    Summarizer Protocol.

    A protocol defining the contract for code summarization.

    Methods
    -------
        summarize(input_path: Path): Summarize code files in the specified directory.

    """

    def summarize(self, input_path: Path) -> list[Summary]:
        """
        Summarize code files in the specified directory.

        :param input_path: The directory containing code files to summarize.
        :type input_path: Path
        :return: A list of Summary objects with file paths and code summaries.
        :rtype: list[Summary]
        """
        pass
