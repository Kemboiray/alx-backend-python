#!/usr/bin/env python3
'''
Test file for printing the correct output of the task_wait_n coroutine
'''
import asyncio

task_wait_n = __import__("4-tasks").task_wait_n

print(asyncio.run(task_wait_n(5, 5)))
print(asyncio.run(task_wait_n(10, 7)))
print(asyncio.run(task_wait_n(10, 0)))
