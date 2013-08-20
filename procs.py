#!/usr/bin/python
import subprocess
from datetime import datetime

def execute(cmd):
    return subprocess.Popen(cmd, stdout=subprocess.PIPE, shell=True).communicate()[0];

def listRunning(proc, liveOnly=False):
    subtasks = execute("ls /proc/%s/task" % proc)
    for task in subtasks.splitlines():
        stats = execute("cat /proc/%s/task/%s/stat" % (proc, task)).split()
        if stats[2] == 'R':
            print datetime.now(), "Subtask", stats[1], "pid:", stats[0], "is running on core", stats[len(stats) - 6]
        elif not liveOnly:
            print datetime.now(), "Subtask", stats[1], "pid:", stats[0], "is last run on core", stats[len(stats) - 6]

proc = raw_input("enter process id: ")

liveOnly = raw_input("live only? [Y,N] (default N): ")
liveOnly = True if liveOnly == 'Y' else liveOnly == 'y'

monitor = raw_input("monitor? [Y,N] (default N): ")
monitor = True if monitor == 'Y' else monitor == 'y'

keepGoing = True
while keepGoing:
    listRunning(proc, liveOnly)
    keepGoing = monitor
