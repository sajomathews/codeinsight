from pathlib import Path
from tempfile import TemporaryDirectory

import pytest
from typer.testing import CliRunner

from codeinsight.cli import app  # Import the command function from your script


@pytest.fixture
def runner() -> CliRunner:
    return CliRunner()


def test_summarize_no_args_fail(runner: CliRunner):
    # Use the `runner.invoke` method to run the command with arguments
    result = runner.invoke(app)

    # Check if the command failed as expected
    assert result.exit_code == 2


def test_summarize_with_non_existent_input_dir(runner: CliRunner):
    result = runner.invoke(app, ["no_such_dir"])

    # Check if the command failed as expected
    assert result.exit_code == 2


def test_summarize_with_valid_dir(runner: CliRunner):
    with TemporaryDirectory() as tmpdir:
        result = runner.invoke(app, [".", f"--output-dir={tmpdir}"])

        # Check dir contains some files
        assert list(Path(tmpdir).glob("*.txt")) is not None

    # Check if the command was successful
    assert result.exit_code == 0
