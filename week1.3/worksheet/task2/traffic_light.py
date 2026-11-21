"""
Portfolio Task - Week 1.3
By submitting this code you are declaring that all work in this file, other than any provided template code, was written and developed by you independently.
Name: Jang Hyuk Lee
"""

states = { "red":4, "red_amber":3, "green":5, "amber":3 }

systime = 0
maxtime = int(input()) # read an integer number of steps (>0)

state = "red"
state_name = list(states)
i = 0
time = 0

print(f"Time {systime:03} State {state}")

while systime < maxtime:
    systime += 1
    time += 1

    if time == states[state]:  # if current time is equal to the time (eg. red = 4) for current state
        i = (i + 1) % len(state_name)   # check the next state and go back to 0 if its the last state
        state = state_name[i]  # update the state to the next state
        time = 0   # reset the time for the new state
    print(f"Time {systime:03} State {state}") 


# Simulate the traffic light system up to time=maxtime in 1-second steps

# At the end of each step you should output the time and state using the statement on line 14