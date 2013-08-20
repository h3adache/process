#!/usr/bin/python
import subprocess

def execute(cmd):
    return subprocess.Popen(cmd, stdout=subprocess.PIPE, shell=True).communicate()[0];

def listRunning(proc, liveOnly=False):
    subtasks = execute("ls /proc/%s/task" % proc)
    for task in subtasks.splitlines():
        stats = execute("cat /proc/%s/task/%s/stat" % (proc, task)).split()
        if stats[2] == 'R':
            print "Subtask", stats[0], "is running on core", stats[len(stats) - 6]
        elif not liveOnly:
            print "Subtask", stats[0], "is last run on core", stats[len(stats) - 6]

proc = raw_input("enter process id: ")
liveOnly = raw_input("live [Y,N] (default N): ")
liveOnly = true if liveOnly == 'Y' else liveOnly == 'y'
print "Subtasks %s of Process %s: " % (liveOnly, proc)
listRunning(proc, liveOnly)
