from flask import Flask, render_template, request
import pandas as pd
import json
import plotly.express as px
import plotly.graph_objects as go

# Initialize the Flask application
app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def upload_file():
    # Check if the request method is POST (file upload)
    if request.method == 'POST':
        # Retrieve the uploaded file
        file = request.files['file']
        # Retrieve the selected time period from the form
        time_period = request.form.get('time_period', 'all')
        if file:
            # Read the CSV file into a DataFrame
            df = pd.read_csv(file)
            # Apply filters based on the selected time period
            # Note: Adjust this line based on your actual data structure
            if time_period != 'all':
                df = df[df['time_period'] == time_period]
            # Generate the funnel visualization
            # Include additional variables for multi-dimensional analysis

            # New: Ensure the stages are in the correct order for a descending funnel
            stages_order = ['Awareness', 'Interest', 'Consideration', 'Intent', 'Conversion'] # Modify as per your stages
            df['stage'] = pd.Categorical(df['stage'], categories=stages_order, ordered=True)

            # New: Create a funnel plot with a title and horizontal orientation
            fig = px.funnel(df, x='conversion_rate', y='stage', color='acquisition_channel', 
                            title="Marketing Funnel Visualization",
                            orientation='h') # Horizontal orientation
            
            # Convert the figure to JSON for rendering in the template
            graphJSON = fig.to_json()
            # Render the chart.html template with the plot data
            return render_template('chart.html', plot=graphJSON)
    # If the request method is not POST, render the upload.html template
    return render_template('upload_funnel.html')

if __name__ == '__main__':
    # Run the Flask application
    app.run(debug=True)
