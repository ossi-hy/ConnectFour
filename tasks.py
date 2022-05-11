from os import system
from invoke import task  # type: ignore
import platform

OS = platform.system()


@task
def start(ctx):
    if OS == "Linux":
        ctx.run("python3 src/main.py", pty=True)
    else:
        print("Unsupported OS, try instead:\n\tpoetry run python src\main.py")


@task
def start_against(ctx):
    if OS == "Linux":
        ctx.run("python3 src/main.py -a", pty=True)
    else:
        print("Unsupported OS, try instead:\n\tpoetry run python src\main.py -a")


@task
def test(ctx):
    if OS == "Linux":
        ctx.run('coverage run --branch -m pytest src -m "not slow"', pty=True)
    elif OS == "Windows":
        ctx.run('coverage run --branch -m pytest src -m "not slow"')
    else:
        print("Unsupported OS")


@task
def slow_test(ctx):
    if OS == "Linux":
        ctx.run("coverage run --branch -m pytest src", pty=True)
    elif OS == "Windows":
        ctx.run("coverage run --branch -m pytest src")
    else:
        print("Unsupported OS")


@task(test)
def coverage_report(ctx):
    if OS == "Linux":
        ctx.run("coverage html -d docs", pty=True)
    elif OS == "Windows":
        ctx.run("coverage html -d docs")
    else:
        print("Unsupported OS")


@task(test)
def coverage(ctx):
    if OS == "Linux":
        ctx.run("coverage report -m", pty=True)
    elif OS == "Windows":
        ctx.run("coverage report -m")
    else:
        print("Unsupported OS")


@task
def profile(ctx):
    if OS == "Linux":
        ctx.run("python3 -m cProfile -s cumulative src/main.py -p", pty=True)
    elif OS == "Windows":
        ctx.run("python -m cProfile -s cumulative src\main.py -p")
    else:
        print("Unsupported OS")
