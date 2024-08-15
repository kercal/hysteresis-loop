# Hysteresis Loop Model

This project simulates a hysteresis loop using a 10x10 matrix of binary values (0s and 1s). The matrix evolves over several time steps, with each cell's state determined by its neighbors and a specified strength parameter.

## **Features**

- **Random Initialization:** The simulation begins with a randomly generated 10x10 matrix of 0s and 1s.
- **Neighbor Counting:** Each cell's neighbors are counted, and the sum is used to determine the probability of the cell changing state.
- **Hysteresis Simulation:** The `hysterese()` function applies a hysteresis effect, where the probability of a cell switching state is influenced by the state of its neighbors and a strength parameter.
- **Time Steps:** The simulation runs for 5 time steps, displaying the matrix's evolution at each step.

## **Usage**

1. **Matrix Initialization:** The matrix is initialized randomly with binary values.
2. **Strength Parameter:** The user is prompted to input a strength parameter (between 0 and 2). If the strength is greater than 1, the direction of state change is reversed.
3. **Simulation:** The simulation runs for 5 time steps, updating the matrix at each step based on the hysteresis model.
4. **Output:** The initial and final states of the matrix are printed.

## **Example**

```python
Zufällig generiertes Schema:
[[0 1 0 ...]
 [1 0 1 ...]
 ...]

Bitte geben Sie eine Stärke zwischen 0 und 2 ein (>1 ändert die Richtung): 1.5

Ergebnis nach 5 Schritten:
[[1 0 1 ...]
 [0 1 0 ...]
 ...]
