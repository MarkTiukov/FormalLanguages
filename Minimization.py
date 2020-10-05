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


# 4
# 6
# a b c
# 0 1 c
# 1 1 b
# 0 2 a
# 2 1 c
# 2 3 c
# 3 3 c
# 1 3


if __name__ == "__main__":
    from Determination import inputData, determine, printMachine

    alphabet, machine, final_states = inputData()
    # dka, new_finals = determine(alphabet, machine, final_states)
    # total_dka = makeTotal(dka, alphabet)
    # printMachine(total_dka, new_finals)
    determined = determine(alphabet, machine, final_states)[0]
    printMachine(determined, final_states)
    print(f"<MINIMIZED>:\n{minimize(determined, alphabet, final_states)}")

# 8
# 16
# a b
# 0 1 a
# 1 2 a
# 2 2 a
# 0 5 b
# 1 3 b
# 2 7 b
# 5 5 a
# 5 5 b
# 3 1 a
# 7 2 a
# 3 4 b
# 7 6 b
# 4 3 a
# 6 7 a
# 6 4 b
# 4 5 b
# 3 4 5 6
