# Operations Research Final Project: Gogoro Site Selection Problem

This repository contains our final project for the Operations Research course. Our project focuses on optimizing the network of GoStations—the battery swapping stations used by Gogoro in Taiwan—by determining which stations can be removed without compromising service coverage and by minimizing the daily battery shipping costs.

## Team Information

- **Team Name:** Team O
- **Members:**
  - Hong-Kai Yang (B11611047)
  - Yi-Ting Chen (B11705051)
  - Chi-Wei Ho (B11702044)
  - Yu-Ting Chou (B11702080)

## Project Overview

The project is divided into two main phases:

1. **Phase 1: GoStation Optimization Strategy**  
   - **Objective:** Maximize the removal of GoStations from Hsinchu City while ensuring that every community’s demand is met by its nearest remaining station.
   - **Approach:**  
     - Develop a mathematical model to decide which stations to remove based on supply–demand balance.
     - Use data extracted from the Gogoro website to estimate real-time battery availability.
     - Pre-process the raw data to underestimate supply and overestimate demand, ensuring a conservative approach to station removal.

2. **Phase 2: Shipping Cost Minimization**  
   - **Objective:** Minimize the daily shipping costs for redistributing batteries among the remaining GoStations while satisfying community demand.
   - **Approach:**  
     - Formulate a mathematical model incorporating shipping, extra battery procurement, and labor costs.
     - Optimize battery dispatch schedules to minimize costs under operational constraints (e.g., inventory continuity and a maximum one-hour inter-processing limit).

## Key Components

- **Introduction & Problem Description:**  
  An overview of the Gogoro battery swapping system, its importance for continuous mobility, and the challenges of high operational costs and site selection.

- **Mathematical Models:**  
  Detailed formulations for both phases, including parameters, decision variables, and constraints to ensure service coverage and cost minimization.

- **Data Processing:**  
  Steps for data acquisition from the Gogoro website, data pre-processing (including supply and demand estimation), and setting up the necessary inputs for the models.

- **Heuristic Algorithm:**  
  A custom-designed heuristic algorithm is implemented to efficiently solve large-scale instances where exact methods may be computationally infeasible. Pseudocode and flowcharts illustrate the algorithm’s key steps.

- **Evaluation:**  
  A comparative evaluation between the heuristic algorithm, a Gurobi-based approach, and a simple heuristic. Metrics such as shipping times, extra battery costs, and assignment times are used to assess performance.

- **Conclusions:**  
  A summary of findings, discussion on challenges (such as demand estimation and data acquisition), and recommendations for future improvements and broader implementation.

For a complete and detailed explanation—including mathematical formulations, algorithm pseudocode, experimental results, and evaluation graphs—please refer to the attached PDF presentation: [TeamO_final_project.pdf](TeamO_final_project_compressed.pdf).
