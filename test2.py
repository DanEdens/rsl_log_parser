# external_pipe_say_my_name.py
import subprocess
import sys

with open("input_pipe", "r") as input_pipe:
    with open("output_pipe", "w") as output_pipe:
        proc = subprocess.Popen(["python", "say_my_name.py"],
            stdin=input_pipe, stdout=output_pipe)

        while proc.returncode is None:
            proc.poll()
