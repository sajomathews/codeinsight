"""
Code Insight CLI.

This module defines a Typer-based Command-Line Interface (CLI) tool for generating
insights in a specified directory. It currently implements a single summarize command
which will summarize all the python files in the directory and save the summaries to
an output directory.

Usage:
    codeinsight /path/to/code_directory [--output-dir /path/to/output_directory]

Commands:
    summarize    Summarize code files in a directory.

Options:
    code_directory    The directory containing code files to summarize.
    --output-dir output_directory    The directory where summaries will be saved.

Example:
-------
    codeinsight /path/to/code_directory --output-dir /path/to/custom_output

"""
from pathlib import Path

import typer

from codeinsight import summarizer

app = typer.Typer()


@app.command()
def summarize(
    input_dir: Path = typer.Argument(
        help="The directory containing code files.", exists=True, file_okay=False
    ),
    output_dir: Path = typer.Option(
        help="The directory to save summaries", default=Path("docs")
    ),
):
    """Summarize code in the given directory."""
    # Ensure the output directory exists
    output_dir.mkdir(parents=True, exist_ok=True)

    # List all files in the input directory
    summaries = summarizer.summarize(input_dir)
    for s, data in summaries.items():
        summary_file = output_dir / s
        with summary_file.open("w") as f:
            f.write(data)

    typer.echo(f"Summaries saved in {output_dir}")
