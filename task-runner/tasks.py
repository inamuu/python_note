from invoke import *

@task
def hello(c):
    c.run("echo 'hello world'")

@task
def createfile(c):
    list = ["test", "test2"]
    c.run("ls -la")
    for name in list:
      if c.run(f"test -e {name}.txt", warn=True).ok:
        c.run(f"rm -f {name}.txt")
        c.run(f"echo remove {name}.txt")
      c.run(f"touch {name}.txt")
    c.run("ls -la")