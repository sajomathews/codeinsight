import typer
from pathlib import Path
from codeinsight import summarizer

app = typer.Typer()


@app.command()
def summarize(
    input_dir: Path = typer.Argument(help="The directory containing code files."),
    output_dir: Path = typer.Option(
        help="The directory to save summaries", default=Path("docs")
    ),
):
    """
    Summarize code in the given directory.
    """
    # Ensure the output directory exists
    output_dir.mkdir(parents=True, exist_ok=True)

    # List all files in the input directory
    summaries = summarizer.summarize(input_dir)
    for s, data in summaries.items():
        summary_file = output_dir / s
        with summary_file.open("w") as f:
            f.write(data)

    typer.echo(f"Summaries saved in {output_dir}")
