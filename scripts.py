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
    check_call(["pylint", "app/", "tests/"])
    check_call(["mypy", "src/backend/", "tests/"])


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
    check_call(["pytest", "tests/"])
