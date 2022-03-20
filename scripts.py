# This is a temporary workaround till Poetry supports scripts, see
# https://github.com/sdispater/poetry/issues/241.
from subprocess import check_call


def format() -> None:
    check_call(
        ["black", "--check", "--diff", "app/", "tests/"],
    )


def reformat() -> None:
    check_call(["black", "app/", "tests/"])


def lint() -> None:
    check_call(["mypy", "app/", "tests/", "--ignore-missing-imports"])
    check_call(["pylint", "app/", "tests/"])


def dev() -> None:
    check_call(
        [
            "uvicorn",
            "app.main:app",
            "--port",
            "8000",
            "--reload",
        ]
    )  # "python", "-m", "app.main"])


def test() -> None:
    check_call(["pytest", "tests/", "-v"])


def poetry_export() -> None:
    check_call(
        [
            "poetry",
            "export",
            "-f",
            "requirements.txt",
            "-o",
            "requirements-freeze.txt",
            "--without-hashes",
        ]
    )
