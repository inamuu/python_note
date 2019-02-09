from invoke import *

@task
def hello(msg):
    msg.run("echo 'hello world'")
