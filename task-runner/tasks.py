from invoke import *

@task
def hello(c):
    c.run("echo 'hello world'")

@task
def createfile(c):
    list = ["test", "test2"]
    for name in list:
      c.run(f"touch {name}.txt")
