from collections import deque


# Алгоритм детерминизации недетерминированного
# конечного автомата (НКА)
#
# стартовое состояние должно быть 0 !!!!
def determine(alphabet: list, machine: list, final_states: set):
    new_machine = {}
    queue = deque(["0"])
    while len(queue) > 0:
        current_long_state = queue.popleft()
        for letter in alphabet:
            current_new_node = whereToGoByLit(machine, current_long_state, letter)
            if current_new_node == "":
                continue
            if current_long_state not in new_machine:
                new_machine[current_long_state] = [(current_new_node, letter)]
            else:
                new_machine[current_long_state].append((current_new_node, letter))
            if current_new_node not in queue and current_new_node not in new_machine:
                queue.append(current_new_node)
    new_final_states = set()
    for new_machine_state in new_machine.keys():
        for old_state in new_machine_state:
            if old_state in final_states:
                new_final_states.add(new_machine_state)
    return new_machine, new_final_states


def whereToGoByLit(machine: list, state: str, lit: str):
    result = set()
    for cur_state in state:
        for transition in machine[int(cur_state)]:
            if transition[1] == lit:
                result.add(transition[0])
    result = list(result)
    result.sort()
    string_result = ""
    for lit in result:
        string_result += str(lit)
    return string_result


def printMachine(machine: dict, final_states: set):
    print("Новый ДКА:")
    for start, transitions in machine.items():
        for end, lit in transitions:
            print(f"{start} {end} \"{lit}\"")
    print("Конечные состояния:")
    print(*final_states, sep=", ")


def inputData():
    n = int(input())  # количество состояний
    m = int(input())  # количество переходов
    alphabet = input().split()  # алфавит
    machine = [[] for i in range(n)]
    for i in range(m):
        begin, end, lit = input().split()
        machine[int(begin)].append((int(end), lit))
    final_states = set(input().split())  # конечные состояния
    return alphabet, machine, final_states


if __name__ == '__main__':
    printMachine(*determine(*inputData()))
