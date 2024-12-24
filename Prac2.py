def validate_string_fa(states, symbols, start_state, accepting_states, transitions, input_string):
    """
    Validate a string based on the given finite automaton rules.

    :param states: List of states in the automaton.
    :param symbols: List of valid input symbols.
    :param start_state: The initial state of the automaton.
    :param accepting_states: List of accepting states.
    :param transitions: Dictionary representing the transition table.
    :param input_string: String to validate.
    :return: True if the string is valid, False otherwise.
    """
    current_state = start_state

    for symbol in input_string:
        if symbol not in symbols:
            return False  # Invalid symbol in input string
        if current_state not in transitions or symbol not in transitions[current_state]:
            return False  # No valid transition
        current_state = transitions[current_state][symbol]

    return current_state in accepting_states


def main():
    # Input number of symbols
    num_symbols = int(input("Number of input symbols: "))
    symbols = input("Input symbols (space-separated): ").split()

    # Input number of states
    num_states = int(input("Enter number of states: "))
    states = [str(i) for i in range(1, num_states + 1)]

    # Input initial state
    start_state = input("Initial state: ")

    # Input number of accepting states
    num_accepting = int(input("Number of accepting states: "))
    accepting_states = input("Accepting states (space-separated): ").split()

    # Input transition table
    transitions = {}
    print("Enter transitions (format: current_state input_symbol next_state):")
    for _ in range(num_states * num_symbols):
        transition = input().split()
        current_state, input_symbol, next_state = transition
        if current_state not in transitions:
            transitions[current_state] = {}
        transitions[current_state][input_symbol] = next_state

    # Input string to validate
    input_string = input("Input string: ")


    if validate_string_fa(states, symbols, start_state, accepting_states, transitions, input_string):
        print("Valid string")
    else:
        print("Invalid string")


if __name__ == "__main__":
    main()
