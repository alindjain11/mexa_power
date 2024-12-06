# mexa_power

The **mexa_power** project, "EmpowerSelf: Power of Sleep for Mind" is developed for **MEXA hackathon** taken place during Dec 3-5, 2024. This repository contains the following components:

## 1. Dataset Folder

This folder contains:

- Code to generate the **synthetic dataset** used for training.
- The **synthetic dataset** itself.
- Code for converting this data into **JSON files** to be used for fine-tuning purposes.

The dataset is a key part of the project, enabling the training of models and fine-tuning based on synthetic data for better performance in specific tasks.

## 2. LLM Training

The **llm_training** file demonstrates how we use the synthetic data to **fine-tune large language models (LLMs)**, specifically **Gemini**. This file shows how the dataset is used to prompt-feed the model, optimizing its performance for the intended tasks.

## 3. Personal Wellbeing Dashboard (GUI)

A **Graphical User Interface (GUI)** has been developed that allows users to interact with the synthetic data and generate personalized wellbeing insights. This interface is powered by the trained LLM and provides a user-friendly way to view and analyze the data.

- The **dashboard** is designed to display personal wellbeing metrics.
- A **screenshot** of the GUI is provided in this repository to showcase its functionality.

## Project Overview

This repository aims to enable the creation of customized wellbeing dashboards using AI-driven insights. By utilizing synthetic data and a fine-tuned LLM model, we designed an AI-powered solution for users to monitor and track their wellbeing in a personalized manner.

## Project Artifacts

"Psychometrist | Evalyn" library in Google AI Studio:
https://aistudio.google.com/app/prompts?state=%7B%22ids%22:%5B%221zF3XQ3LoUKc3N2KlZ0YG7KMfFJA10zb1%22%5D,%22action%22:%22open%22,%22userId%22:%22117292115876876308818%22,%22resourceKeys%22:%7B%7D%7D&usp=sharing

Below are copies of prompts and outputs found in the library.
1. Prompt 01 - System Instructions.doc
2. Prompt 02 - Other Promps.doc
3. Output 01 - Rubrics.xls
4. Output 02 - Wellbeing Dimension Metrics.doc
5. Others: Synthetic data + User responses that signal early warning signs of burnout and mental illness to a question, "Hi! How is life treating you?"
   
---

Feel free to explore the repository and contribute to the ongoing development of the **mexa_power** project. For any questions or issues, please open an issue or contact us directly.




