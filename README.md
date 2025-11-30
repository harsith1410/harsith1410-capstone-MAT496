# Overview of MAT496

In this course, we have primarily learned Langgraph. This is helpful tool to build apps which can process unstructured `text`, find information we are looking for, and present the format we choose. Some specific topics we have covered are:

- Prompting
- Structured Output 
- Semantic Search
- Retreaval Augmented Generation (RAG)
- Tool calling LLMs & MCP
- Langgraph: State, Nodes, Graph

We also learned that Langsmith is a nice tool for debugging Langgraph codes.

------
# Capstone Project objective

The first purpose of the capstone project is to give a chance to revise all the major above listed topics. The second purpose of the capstone is to show your creativity. Think about all the problems which you can not have solved earlier, but are not possible to solve with the concepts learned in this course. For example, We can use LLM to analyse all kinds of news: sports news, financial news, political news. Another example, we can use LLMs to build a legal assistant. Pretty much anything which requires lots of reading, can be outsourced to LLMs. Let your imagination run free.

------

## Title: F1 Race Strategy Simulator

## Overview

This project is an F1 race simulator designed to model complex race scenarios. It utilizes Langgraph to simulate strategic decisions, factoring in variables such as tyre degradation, weather conditions, and pit stop timing to predict potential race outcomes.

## Video Summary

Link : https://1drv.ms/v/c/7836e344b21102c4/IQAtItRsom-ySbfirTGuaSpyAWchDUwBPbup8z36fUK24eM?e=w0pNPh


## Reason for picking up this project

I selected this project to merge my deep-seated interest in the  world of Formula 1 strategy with the advanced LLM concepts 
mastered in this course. 
The dynamic nature of an F1 race—where split-second decisions on tyres, pit stops, and defending against rivals can 
determine the outcome—provides a rich, complex environment to challenge my critical thinking and strategic modeling abilities.

Beyond just applying standard techniques, this project aims to push the boundaries of 
how we can model such dynamic systems. It comprehensively employs Langgraph for managing the evolving 
race state, RAG to leverage vast historical data for context-aware simulations, graph parallelization 
to model competing team strategies concurrently, and human-in-the-loop interrupts for those crucial, 
race-defining moments. Tackling this level of complexity makes it a deeply engaging and rewarding endeavor.

## Plan

### Flow of Control

The project is architected using **LangGraph**, dividing the simulation into distinct phases managed by subgraphs and conditional edges. The flow moves from initialization to a cyclic race loop, culminating in a visual celebration.

### 1. Race Preparation Phase (`RacePrep` Subgraph)
Before the race begins, the system initializes the global state through a linear sequence of nodes:
* **Track & Weather:** The user selects a track (Monaco, Great Britain, or Abu Dhabi), loading specific degradation profiles. Weather is generated stochastically (Wet/Dry).
* **Driver Initialization:** A grid of 14 cars is created. The user selects their driver, while the remaining 13 are assigned as AI bots.
* **Pre-Race Strategy:** * **User:** Manually selects starting tyres based on track data.
    * **AI Agents:** An LLM (`GenerateTelemetry` node) analyzes the track and weather to autonomously select the optimal starting compound for every AI car.
* **Grid Formation:** The grid is shuffled, positions are assigned, and the starting order is visualized.

### 2. The Main Race Loop
The core simulation runs in a cycle until the total lap count is reached. This loop utilizes nested graphs to handle complexity.

* **Timing Sheet Generation:** At the start of the loop, the system sorts cars by total race time and displays a live leaderboard with gaps.
* **Event & Physics Simulation (`Events` Subgraph):**
    * **Event Generation:** Probabilistic logic determines if race-altering events occur (Safety Car, VSC, Yellow Flag) or if the weather shifts (Dry ↔ Wet).
    * **Lap Time Calculation:** A hybrid approach is used. An LLM (`LaptimeModel`) generates a base pace based on telemetry, which is then mathematically adjusted for fuel load, tyre degradation percentage, and random variance.
    * **Event Application:** If an event like a Safety Car is active, the system artificially compresses the gaps between cars.
* **Telemetry Updates:** The system mathematically calculates linear tyre wear (based on track abrasiveness), reduces fuel load, and increments tyre age.
* **Strategy & Pit Stops (`PitCall` Node):**
    * **User Decision:** The system pauses for Human-in-the-Loop input, presenting current telemetry and asking the user to "Box" (1) or "Stay out" (0).
    * **AI Decision:** An LLM Agent acts as the Race Engineer for *each* AI car. It evaluates tyre health, weather, and track position to make an autonomous decision on pitting and selecting a new tyre compound.

### 3. Race Conclusion
* **Termination:** A conditional edge (`check_race_over`) monitors the lap count. Once the total laps are completed, the loop breaks.
* **Podium Celebration:** The `podium_celebration` node uses the **Pillow (PIL)** library to dynamically draw and display an image of the top 3 drivers on the podium, including their teams and final time gaps.

## Conclusion

I have successfully achieved the primary objective of building a complex, state-aware F1 strategy simulator. The project demonstrates a robust implementation of **LangGraph** to manage a dynamic global state containing detailed telemetry for multiple agents simultaneously.

I am satisfied with the current implementation because:
1.  **Hybrid Intelligence:** I successfully merged deterministic logic (math-based tyre deg/fuel burn) with non-deterministic LLM agents, creating a simulation that feels organic rather than purely scripted.
2.  **Complex State Management:** The system handles a nested graph structure (`RacePrep` -> `Main Loop` -> `Events Subgraph`) effectively, proving the power of LangGraph for multi-step agentic workflows.
3.  **Strategic Depth:** The inclusion of probabilistic events ensures that no two race simulations are exactly the same.

**Future Roadmap:**
While the core simulation logic is robust, I see several key areas for future development. I had originally planned to integrate a dedicated **User Interface (UI)** (using frameworks like Flask or Django) to replace the current notebook-based interactions. A GUI would make the "Human-in-the-loop" decisions more intuitive and visually immersive.

Other potential enhancements include:
* **Advanced Telemetry Visualization:** Implementing it into a Graphical Interface and making the .
* **Driver Personalities:** Fine-tuning the AI agents to reflect real-world driver traits (e.g., aggressive vs. conservative tyre management).
* **Expanded Race Physics:** Introducing more granular variables like track temperature evolution, dirty air effects, and mechanical failures.
----------

  