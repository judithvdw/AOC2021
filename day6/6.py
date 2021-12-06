def populate_states(initial_states):
    states = {i : 0 for i in range(9)}
    for state in initial_states:
        states[state] +=1
    return states

def pass_day(states):
    new_states = {i : 0 for i in range(9)}
    for timer, n_fish in states.items():
        if timer == 0:
            new_states[8] += states[0]
            new_states[6] += states[0]
        else:
            new_states[timer-1] += states[timer]
    return new_states

def total_anglerfish(days, states):
    for i in range(days):
        states = pass_day(states)
    return sum(states.values())

if __name__ == '__main__':
    initial_state = [1,3,4,1,5,2,1,1,1,1,5,1,5,1,1,1,1,3,1,1,1,1,1,1,1,2,1,5,1,1,1,1,1,4,4,1,1,4,1,1,2,3,1,5,1,4,1,2,4,1,1,1,1,1,1,1,1,2,5,3,3,5,1,1,1,1,4,1,1,3,1,1,1,2,3,4,1,1,5,1,1,1,1,1,2,1,3,1,3,1,2,5,1,1,1,1,5,1,5,5,1,1,1,1,3,4,4,4,1,5,1,1,4,4,1,1,1,1,3,1,1,1,1,1,1,3,2,1,4,1,1,4,1,5,5,1,2,2,1,5,4,2,1,1,5,1,5,1,3,1,1,1,1,1,4,1,2,1,1,5,1,1,4,1,4,5,3,5,5,1,2,1,1,1,1,1,3,5,1,2,1,2,1,3,1,1,1,1,1,4,5,4,1,3,3,1,1,1,1,1,1,1,1,1,5,1,1,1,5,1,1,4,1,5,2,4,1,1,1,2,1,1,4,4,1,2,1,1,1,1,5,3,1,1,1,1,4,1,4,1,1,1,1,1,1,3,1,1,2,1,1,1,1,1,2,1,1,1,1,1,1,1,2,1,1,1,1,1,1,4,1,1,1,1,1,1,1,1,1,1,1,1,1,1,2,1,1,2,5,1,2,1,1,1,1,1,1,1,1,1]
    states = populate_states(initial_state)

    print(f"Part 1:{total_anglerfish(80, states)}")
    print(f"Part 2:{total_anglerfish(256, states)}")
