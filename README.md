# IoT-DA_LR_CRISP-DM_HW1: Linear Regression Streamlit Application

This project demonstrates a simple linear regression model implemented as an interactive Streamlit application. It allows users to generate synthetic housing data, visualize the regression line, identify outliers, and predict prices based on user-defined parameters.

## Project Evolution

The project started with a basic Python script (`app.py`) containing Chinese comments and a fixed dataset. Through several iterations, it has evolved into a dynamic Streamlit application with enhanced features and a user-friendly interface.

### 1. Initial Setup and Translation

Initially, the `app.py` script contained a linear regression model with hardcoded parameters and comments in Chinese.

*   **Action:** The script was translated from Chinese to English to improve readability and maintainability.
*   **Challenge & Resolution:** A `UnicodeEncodeError` was encountered due to the `R²` character in a print statement. This was resolved by replacing `R²` with `R^2`.

### 2. Plotting Refinement

The original script generated two plots, which was redundant.

*   **Action:** The code was modified to display only the final, more informative plot showing the regression line.

### 3. Streamlit Conversion and Interactivity

The core `app.py` script was converted into a Streamlit application to provide an interactive user experience.

*   **Interactive Parameters:**
    *   **Number of Data Points (n):** A slider was added to control the number of data points generated, ranging from 100 to 5000.
    *   **Coefficient (a):** A slider was introduced to adjust the coefficient used in the price generation formula, ranging from -10.0 to 10.0.
    *   **Noise Variance (var):** A slider was added to control the variance of the noise in the price data, ranging from 0 to 1000.
*   **Layout:** The application layout was restructured to include a left-side control bar for all input parameters and a right-side main area for displaying data and plots.

### 4. Outlier Detection and Visualization

To enhance data analysis, outlier detection was implemented and integrated into the visualization.

*   **Methodology:** Outliers are identified using the Interquartile Range (IQR) method. Data points falling below `Q1 - 1.5 * IQR` or above `Q3 + 1.5 * IQR` are flagged as outliers.
*   **Visualization:** Outliers are now distinctly plotted in red on the scatter plot, making them easily identifiable.

### 5. Git Integration

The project was initialized as a Git repository and pushed to GitHub for version control and collaboration.

*   **Repository:** `https://github.com/YiKai07/IoT-DA_LR_CRISP-DM_HW1.git`
*   **Commit Message:** "Initial commit: Streamlit app with sidebar and outlier detection"

## How to Run the Streamlit Application

1.  **Ensure Python and Streamlit are installed:**
    ```bash
    pip install streamlit numpy pandas matplotlib scikit-learn
    ```
2.  **Navigate to the project directory:**
    ```bash
    cd D:\01_學校資料\114_1_上課資料\物聯網應用與資料分析\HW1
    ```
3.  **Run the Streamlit application:**
    ```bash
    streamlit run app.py
    ```
    This command will open the application in your default web browser, usually at `http://localhost:8501`.

## Files in this Project

*   `app.py`: The main Streamlit application script.
*   `GEMINI.md`: Provides instructional context for future interactions with the Gemini CLI.
*   `log.md`: A detailed log of all interactions and actions performed by the Gemini CLI agent during the project development.

## Future Enhancements

*   Add more advanced regression models (e.g., Polynomial Regression, Ridge, Lasso).
*   Implement more sophisticated outlier detection methods.
*   Allow users to upload their own datasets.
*   Add more evaluation metrics and visualizations.
