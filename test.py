#! /usr/bin/python3

"""Store input in a queue as soon as it arrives, and work on
it as soon as possible. Do something with untreated input if
the user interrupts. Do other stuff if idle waiting for
input."""

import sys
import time
import threading
import queue

timeout = 0.1 # seconds
last_work_time = time.time()

def treat_input(linein):
  global last_work_time
  print('Working on line:', linein, end='')
  time.sleep(1) # working takes time
  print('Done working on line:', linein, end='')
  last_work_time = time.time()

def idle_work():
  global last_work_time
  now = time.time()
  # do some other stuff every 2 seconds of idleness
  if now - last_work_time > 2:
    print('Idle for too long; doing some other stuff.')
    last_work_time = now

def input_cleanup():
  print()
  while not input_queue.empty():
    line = input_queue.get()
    print("Didn't get to work on this line:", line, end='')

# will hold all input read, until the work thread has chance
# to deal with it
input_queue = queue.Queue()

# will signal to the work thread that it should exit when
# it finishes working on the currently available input
no_more_input = threading.Lock()
no_more_input.acquire()

# will signal to the work thread that it should exit even if
# there's still input available
interrupted = threading.Lock()
interrupted.acquire()

# work thread' loop: work on available input until main
# thread exits
def treat_input_loop():
  while not interrupted.acquire(blocking=False):
    try:
      treat_input(input_queue.get(timeout=timeout))
    except queue.Empty:
      # if no more input, exit
      if no_more_input.acquire(blocking=False):
        break
      else:
        idle_work()
  print('Work loop is done.')

work_thread = threading.Thread(target=treat_input_loop)
work_thread.start()

# main loop: stuff input in the queue until there's either
# no more input, or the program gets interrupted
try:
  for line in sys.stdin:
    if line: # optional: skipping empty lines
      input_queue.put(line)

  # inform work loop that there will be no new input and it
  # can exit when done
  no_more_input.release()

  # wait for work thread to finish
  work_thread.join()

except KeyboardInterrupt:
    interrupted.release()
    input_cleanup()

print('Main loop is done.')