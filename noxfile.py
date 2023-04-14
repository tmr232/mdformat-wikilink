import nox
from nox import Session

SOURCE_LOCATIONS = ("src", "tests", "noxfile.py")

nox.options.sessions = ["format", "lint", "test"]


@nox.session(python=False)
def format(session: Session) -> None:
    session.run("ruff", "check", "--fix-only", "--exit-zero", *SOURCE_LOCATIONS)
    session.run("isort", *SOURCE_LOCATIONS)
    session.run("black", *SOURCE_LOCATIONS)


@nox.session(python=False)
def lint(session: Session) -> None:
    session.run("ruff", *SOURCE_LOCATIONS)
    session.run("mypy", *SOURCE_LOCATIONS)
    session.run("isort", "--check-only", *SOURCE_LOCATIONS)
    session.run("black", "--check", *SOURCE_LOCATIONS)


@nox.session(python=False)
def test(session: Session) -> None:
    session.run("pytest", *session.posargs)
