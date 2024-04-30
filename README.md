# Funnel Visualization Tool

Updated: 04.30.2024

## Project Overview

The Funnel Visualization Tool is a web application built with Flask that allows users to upload a CSV file containing data about a funnel process. It visualizes the data as a funnel chart, providing insights into the conversion rates at each stage of the funnel and the effectiveness of different acquisition channels.

## Project and Work Product Description

This project aims to simplify the analysis of funnel data by providing an intuitive and interactive visualization. It addresses the need for a straightforward way to understand the performance of different stages in a funnel and the impact of various acquisition channels.

- **Main Goals**: To provide a user-friendly interface for uploading CSV files and visualizing funnel data.
- **Problems Solved**: Facilitates the analysis of funnel data by offering a clear and interactive visualization of conversion rates and acquisition channels.

### Problem and Solution Workflow Diagrams

(TBD flowcharts here to illustrate the "AS-IS" and "TO-BE" states of the funnel process.)

## Description of Solution

The Funnel Visualization Tool is designed to be simple and effective. It uses Plotly for data visualization, ensuring that the funnel chart is both informative and visually appealing.

- **Software Functions**: The application reads a CSV file, filters the data based on a selected time period, and generates a funnel chart visualization.
- **Workflow Diagram**: TBD
- **Minimum Viable Product (MVP) 1.0**: The application can read a CSV file, filter data, and display a funnel chart.
- **Later MVPs**: Future enhancements may include additional filtering options, customizable chart styles, and support for more complex funnel structures.

## Solution Design (High-Level)

The application is built using Flask, a lightweight web framework for Python. It leverages Plotly for data visualization, providing a powerful and flexible way to create interactive charts.

## Solution Code Description (Low-Level Design)

- **Flask**: Used for handling HTTP requests and rendering templates.
- **Pandas**: Used for reading and filtering the CSV data.
- **Plotly**: Used for creating the funnel chart visualization.

## Actual Working Product Code

The core functionality of the application is contained within `Funnel_Visualization.py`. This file handles the file upload, data processing, and chart generation.

## Application Instructions

### Installation and Setup

1. Clone the repository.
2. Install the required Python packages: `flask`, `pandas`, and `plotly`.
3. Run the Flask application: `python Funnel_Visualization.py`.

### Usage

1. Navigate to `http://localhost:5000` in your web browser.
2. Click "Choose File" to select your CSV file.
3. Optionally, select a time period from the dropdown menu.
4. Click "Upload" to generate the funnel chart.

