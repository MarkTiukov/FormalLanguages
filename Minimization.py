def minimize(machine, alphabet, final_states):
    number_of_classes = 2
    old_number = 2
    classes = {state: (1 if state in final_states else 0) for state in machine.keys()}  # 1 -- конечное, 0 -- иначе
    has_changed = True
    while has_changed:
        has_changed = False
        for letter in alphabet:
            new_classes = {}
            already_added = []
            new_number = 0
            for state in machine:
                for to, lit in machine[state]:
                    if not lit == letter:
                        continue
                    class_transition = f"{classes[state]}#{classes[to]}"
                    if class_transition not in already_added:
                        already_added.append(class_transition)
                        new_number += 1
                    new_classes[state] = already_added.index(class_transition)
            if not old_number == new_number:
                has_changed = True
                old_number = new_number
            classes = new_classes
    return classes

if __name__ == "__main__":
    from Determination import inputData, determine, makeTotal

    alphabet, machine, final_states = inputData()
    determined, determined_final_states = determine(alphabet, machine, final_states)
    print(f"<MINIMIZED>:\n{minimize(makeTotal(determined, alphabet), alphabet, final_states)}")
    