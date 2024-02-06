# Underwater Animal Classification Project

This project aims to classify underwater animal images using the ResNet-50 model. The classification model is deployed using Streamlit, and MLflow is used for experiment tracking and model management.

## Project Structure

The project follows a structured approach for managing artifacts and configurations:

### `config.yaml`:

- **Artifacts Root Directory**: Centralized location for storing project artifacts.
  
- **Data Ingestion Configuration**:
  - **Root Directory**: Directory for storing data ingestion artifacts.
  - **Local Data File**: Local file containing the dataset.
  - **Unzip Directory**: Directory for storing the unzipped dataset.
  
- **Prepare Base Model Configuration**:
  - **Root Directory**: Directory for storing artifacts related to preparing the base model.
  - **Base Model Path**: Path to the original base model file.
  - **Updated Base Model Path**: Path to store the updated base model file.
  
- **Training Configuration**:
  - **Root Directory**: Directory for storing artifacts related to model training.
  - **Trained Model Path**: Path to store the trained model file.

### Artifact Structure:

- **Data Ingestion Directory**: Contains scripts or notebooks for data ingestion tasks.
- **Prepare Base Model Directory**: Holds scripts or notebooks for preparing the base model.
- **Training Directory**: Stores scripts or notebooks for training the model.

## How It Helps:

1. **Centralized Configuration**: Easy management of project settings and parameters.
2. **Artifact Organization**: Structured organization of project files and outputs.
3. **Consistency**: Ensures consistency in project organization and execution.
4. **Scalability and Reproducibility**: Facilitates replication of experiments and scaling up the project.

## Usage

To run the project, follow these steps:

1. Clone the repository.
2. Install the required dependencies.
3. Configure the `config.yaml` file with appropriate values.
4. Execute the data ingestion, base model preparation, and training scripts or notebooks.
5. Use Streamlit to deploy the classification model and make predictions.

### Running Streamlit:

To run Streamlit and deploy the classification model, follow these steps:

1. Install Streamlit using `pip install streamlit`.
2. Navigate to the project directory containing the Streamlit app.
3. Run the Streamlit app using the command `streamlit run app.py`.
4. Access the Streamlit app in your web browser at the specified URL.

### Running MLflow:

To use MLflow for experiment tracking and model management, follow these steps:

1. Install MLflow using `pip install mlflow`.
2. Start the MLflow server by running `mlflow server`.
3. Set the MLflow tracking URI to the server's address, e.g., `mlflow.set_tracking_uri("http://localhost:5000")`.
4. Use MLflow APIs to log experiments, parameters, metrics, and models in your code.

## License

This project is licensed under the [MIT License](LICENSE).
