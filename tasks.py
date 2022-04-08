from os import system
from invoke import task
import platform

OS = platform.system()

@task
def start(ctx):
    if OS == "Linux":
        ctx.run("python3 src/main.py", pty=True)
    else:
        print("Unsupported OS, try instead:\n\tpoetry run python src/main.py")

@task
def test(ctx):
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
    