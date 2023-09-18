from pathlib import Path


def summarize(input_dir: Path) -> dict[Path, str]:
    code_files = [str(f) for f in input_dir.rglob("*.py")]
    overall_summary = "\n".join(code_files)
    return {Path("overall.txt"): overall_summary}
