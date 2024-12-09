# NBA Lineup Optimization Project - DS785 Capstone

## Description

This project focuses on revolutionizing NBA lineup strategy through the use of advanced plus-minus models and linear programming. By leveraging play-by-play data from NBA games spanning 1998 to 2023, the project aims to optimize lineup combinations to enhance team performance. The core of this project involves developing predictive plus-minus models and integrating them into a linear program to identify optimal lineup strategies for full 48-minute games.

## Key Files

- **pull_pbp_data.ipynb**
  - **Purpose**: Pulls raw NBA play-by-play data from 1996 to 2023.
  - **Functionality**: For every play, identifies the 10 players on the court and records the action, forming the core dataset to power the calculation of plus-minus models for the linear program.

- **import_lineups**
  - **Purpose**: Prepares play-by-play data for analysis.
  - **Functionality**: Reads the play-by-play data and performs data preparation to enable viewing at both the per-player level and the per-lineup level.

- **game_mov_predictions.ipynb**
  - **Purpose**: Calculates various plus-minus model estimations.
  - **Functionality**: Includes multiple versions of plus-minus models:
    - v0: Baseline
    - v1: Raw Plus-Minus
    - v2: Player RAPM
    - v3: Player B-RAPM
    - v4: Player C-RAPM
    - v5: Lineup RAPM
    - v6: Lineup C-RAPM
    - v7: Bayesian combination (incomplete)
  - **Additional Features**: Contains code for generating plots used in the accompanying paper.

- **lineup_optimizer_season.ipynb**
  - **Purpose**: Integrates previous work to run the lineup optimizer over the entire season.
  - **Functionality**: 
    - Reads data and retrieves lineups for all teams.
    - Filters data to a specific team and season.
    - Executes linear programs, including one that disregards lineup order and another performing sequential decision analysis, the project's major outcome.
    - Output optimal lineups for season long data

- **lineup_optimizer_game.ipynb**
  - **Purpose**: Integrates previous work to run the lineup optimizer for a specific game.
  - **Functionality**: 
    - Reads data and retrieves lineups for all teams.
    - Filters data to a specific team, season and game.
    - Executes linear programs, including one that disregards lineup order and another performing sequential decision analysis, the project's major outcome.
    - Output optimal lineups for specific game
---

This README provides an overview of the project's objectives and the key files that contribute to achieving those goals. Each file plays a crucial role in the data processing, model estimation, and optimization processes that form the foundation of this innovative approach to NBA lineup strategy.
