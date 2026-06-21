# Connect4 AI Laboratory

## Vision

This project is not just a Connect 4 game.

The goal is to progressively build increasingly sophisticated AI agents and compare their behavior, performance, and decision-making.

By the end of the project, the same game should support multiple AI opponents ranging from random play to self-learning systems.

This project serves as a practical introduction to:

* Game AI
* Search algorithms
* Adversarial decision making
* Monte Carlo methods
* Neural Networks
* Reinforcement Learning
* AlphaZero-style self-play systems

---

# Long-Term Architecture

```text
connect4/

├── board.py
├── main.py
│
├── agents/
│   ├── HumanPlayer.py
│   ├── RandomAI.py
│   ├── RuleBasedAI.py
│   ├── MinimaxAI.py
│   ├── AlphaBetaAI.py
│   ├── MonteCarloAI.py
│   ├── NeuralNetworkAI.py
│   └── AlphaZeroStyleAI.py
│
├── training/
│   ├── self_play.py
│   ├── dataset_generator.py
│   └── train_network.py
│
├── gui/
│   └── pygame_ui.py
│
├── web/
│   ├── backend/
│   └── frontend/
│
└── README.md
```

---

# AI Roadmap

## HumanPlayer

Purpose:

Baseline player.

Move selection:

* Human input

Concepts learned:

* Game loop
* Board interaction

Status:

✅ Completed

---

## RandomAI

Purpose:

First automated opponent.

Move selection:

* Random valid move

Concepts learned:

* Agent abstraction
* Valid move generation

Status:

✅ Completed

---

## RuleBasedAI

Purpose:

Introduce tactical reasoning.

Move selection:

1. Play winning move if available.
2. Block opponent winning move.
3. Otherwise choose random move.

Concepts learned:

* Board simulation
* Threat detection
* Tactical play

Status:

🔲 Not Started

---

## MinimaxAI

Purpose:

Introduce adversarial search.

Move selection:

* Explore future game states recursively.
* Assume opponent plays optimally.

Concepts learned:

* Game trees
* Recursive search
* Utility functions

Status:

🔲 Not Started

---

## AlphaBetaAI

Purpose:

Optimize Minimax.

Move selection:

* Same decisions as Minimax.
* Fewer nodes searched.

Concepts learned:

* Pruning
* Search optimization

Status:

🔲 Not Started

---

## MonteCarloAI

Purpose:

Evaluate positions through simulation.

Move selection:

* Play thousands of random games.
* Estimate move quality statistically.

Concepts learned:

* Monte Carlo methods
* Rollouts
* Sampling

Status:

🔲 Not Started

---

## NeuralNetworkAI

Purpose:

Learn board evaluation from data.

Move selection:

* Neural network predicts board strength.

Concepts learned:

* Supervised learning
* Position evaluation
* Dataset generation

Status:

🔲 Not Started

---

## AlphaZeroStyleAI

Purpose:

Build a simplified AlphaZero system.

Move selection:

* Self-play
* Neural network guidance
* Monte Carlo Tree Search

Concepts learned:

* Reinforcement learning
* Self-play training
* Modern game AI

Status:

🔲 Not Started

---

# Future Interfaces

## Terminal

Current interface.

Status:

✅ Completed

---

## Pygame GUI

Features:

* Visual board
* Piece animations
* Difficulty selection

Status:

🔲 Planned

---

## Web Application

Features:

* Browser-based gameplay
* AI selection menu
* Match statistics

Status:

🔲 Planned

---

# Current Project Status

Completed:

* Board implementation
* Move validation
* Gravity logic
* Win detection
* Human vs Human
* Human vs Random AI

AI Progress:

* RandomAI
* RuleBasedAI

Additional Features:

* Difficulty Selection
* Git + GitHub

Current architecture:

```text
board.py
ai.py
main.py
```

Current capabilities:

* Horizontal win detection
* Vertical win detection
* Diagonal win detection
* Board cloning
* Valid move generation
* Rule-based move selection
* Board evaluation function

  * Horizontal scoring
  * Vertical scoring
  * Positive diagonal scoring
  * Negative diagonal scoring
  * Center column bonus

Future refactor:

```text
board.py
main.py

agents/
    HumanPlayer.py
    RandomAI.py
    RuleBasedAI.py
    MinimaxAI.py
    ...
```

Refactor only when additional agents exist.

---

# Current Next Task

Implement Minimax AI.

Questions to answer:

1. How does Minimax search future moves?
2. How does recursion explore the game tree?
3. How should maximizing and minimizing turns work?
4. How should terminal states be handled?
5. What search depth should be used?

Goal:

Create a Minimax AI that uses the board evaluation function to choose moves.

Status:

Next

---

# Roadmap

Completed

* RandomAI
* RuleBasedAI
* Board Evaluation Function

Next

* MinimaxAI

Future

* Alpha-Beta Pruning
* Agent Refactor
* Advanced Heuristics
* MCTS / AlphaZero-style experiments

Last Updated:
June 2026

