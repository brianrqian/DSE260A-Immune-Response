2nd CMI-PB Prediction Challenge
*********************************Team Information*********************************
Team Advisor: Barry Grant, Jason Hsiao
Team Members: Peng Cheng, Javier Garcia, Brian Qian, Weikang Guan

*********************************Overview*********************************
The 2nd CMI-PB Prediction Challenge is a systems immunology competition focused on analyzing longitudinal immune response data obtained through multi-omics experiments. The goal is to establish computational models that predict vaccination outcomes based on the baseline state of the vaccines.

*********************************Project Structure*********************************
This project consists of five Jupyter notebooks that handle various aspects of the data processing, model training, prediction, and visualization.

*********************************Notebooks*********************************
00_data_pipeline.py
	Purpose: 
		This script connects to the CMI laboratory database to fetch the latest training dataset and prediction target data.
	Usage: 
		Run the script to update the local dataset with the latest information from the database.
	Functions:
		Connect to the database
		Fetch the latest data
		Save the data locally for further processing
		By running the script using your local python version, you can download all of the data files onto the `data` directory of this project. 
		Every time the script is ran, it will purge any files that exist in that directory.

01_data_Integration.ipynb
	Purpose: 
		This notebook preprocesses and integrates the fetched data, preparing it for model training.
	Usage: 
		Run all cells to clean and integrate the data.
	Steps:
		Load the data
		Clean and preprocess the data
		Integrate different data sources
		Save the cleaned and integrated data

02_modeling.ipynb
	Purpose: 
		This notebook trains machine learning models on the integrated dataset.
	Usage: 
		Run all cells to train the models and select the best one for each prediction task.
	Steps:
		Load the integrated data
		Perform feature selection
		Train multiple models
		Evaluate models and select the best one
		Save the trained models and evaluation metrics

03_Prediction.ipynb
	Purpose: 
		This notebook generates predictions using the trained models on the test dataset.
	Usage: 
		Run all cells to make predictions and prepare the submission files.
	Steps:
		Load the test data
		Preprocess the test data
		Load the trained models
		Make predictions for each task
		Rank the predictions
		Save the prediction results

04_dashboard.ipynb
	Purpose: 
		This notebook reads the training and prediction results and displays them on a dashboard for visualization.
	Usage: 
		Run all cells to visualize the results.
	Steps:
		Load training and prediction results
		Create visualizations (e.g., plots, charts)
		Display the results on the dashboard

*********************************How to Run the Project*********************************
1. Clone the repository

2. Navigate to the project directory

3. Install the required packages: 
	pip install -r requirements.txt

4. Run the notebooks:
	Open each file in your preferred Jupyter environment (e.g., Jupyter Notebook, Google Colab).
	Execute the cells in the following order:
		00_data_pipeline.py
		01_data_Integration.ipynb
		02_modeling.ipynb
		03_Prediction.ipynb
		04_dashboard.ipynb

*********************************Detailed Steps for Running Each Notebook*********************************
00_data_pipeline.py
	Connect to the CMI laboratory database.
	Fetch the latest training data.
	Save the fetched data to a local file.
	if you're working on a file in a different directory, you will need to change ops.path.abspath('../your/intended/path/') to the intended relative path
directory_path = os.path.abspath('../')
	if directory_path not in sys.path:
	sys.path.append(directory_path)
		import api_requests
	Usage： api_requests.create_subdirectory()

01_data_Integration.ipynb
	Load the fetched data from the local file.
	Clean and preprocess the data (e.g., handle missing values, normalize data).
	Integrate different data sources (e.g., combine datasets from different experiments).
	Save the cleaned and integrated data to a local file.

02_modeling.ipynb
	Load the integrated data from the local file.
	Perform feature selection (e.g., select the most relevant features for each task).
	Train multiple machine learning models (e.g., Random Forest, Lasso, SVR).
	Evaluate the models using cross-validation and select the best model for each task.
	Save the trained models and evaluation metrics to local files.

03_Prediction.ipynb
	Load the test data from a local file or a remote source.
	Preprocess the test data (e.g., handle missing values, normalize data).
	Load the trained models from local files.
	Use the trained models to make predictions for each task.
	Rank the predictions and prepare the submission files.
	Save the prediction results to local files.

04_dashboard.ipynb
	Load the training and prediction results from local files.
	Create visualizations (e.g., bar plots, line charts) to display the results.
	Display the visualizations on a dashboard for easy analysis.
	Results and Evaluation
	The results of the prediction tasks will be evaluated by the CMI-PB team. The final submission should include the ranked 	predictions for each task, which will be used to determine the accuracy and performance of the models.

*********************************Acknowledgements*********************************
We thank the CMI-PB team for organizing this challenge and providing the datasets. We also thank our advisors, Barry Grant and Jason Hsiao, for their guidance and support throughout the project.

*********************************Contact*********************************
For any questions or issues, please contact pec016@ucsd.edu; brqian@ucsd.edu; weguan@ucsd.edu; jag043@ucsd.edu.