import typer
from typer.testing import CliRunner
from codeinsight.cli import app  # Import the command function from your script


def test_summarize_command():
    runner = CliRunner()

    # Use the `runner.invoke` method to run the command with arguments
    result = runner.invoke(app)

    # Check if the command succeeded and the output is as expected
    assert result.exit_code == 2
