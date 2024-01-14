import mlflow.keras
import mlflow
from urllib.parse import urlparse
from cnnClassifier.entity.config_entity import EvaluationConfig

from pathlib import Path
import tensorflow as tf

class Evaluation:
    def __init__(self, config: EvaluationConfig):
        self.config = config
        self.model = None

    def _valid_generator(self):
        datagenerator_kwargs = dict(
            rescale=1. / 255,
            validation_split=0.30
        )

        dataflow_kwargs = dict(
            target_size=self.config.params_image_size[:-1],
            batch_size=self.config.params_batch_size,
            interpolation="bilinear"
        )

        valid_datagenerator = tf.keras.preprocessing.image.ImageDataGenerator(
            **datagenerator_kwargs
        )

        self.valid_generator = valid_datagenerator.flow_from_directory(
            directory=self.config.training_data,
            subset="validation",
            shuffle=False,
            **dataflow_kwargs
        )

    @staticmethod
    def load_model(path: Path) -> tf.keras.Model:
        return tf.keras.models.load_model(path)

    def evaluation(self):
        self.model = self.load_model(self.config.path_of_model)
        self._valid_generator()
        self.score = self.model.evaluate(self.valid_generator)
        self.print_score()

    def print_score(self):
        loss, accuracy = self.score[0], self.score[1]
        print(f"Validation Loss: {loss:.4f}")
        print(f"Validation Accuracy: {accuracy * 100:.2f}%")

    def log_into_mlflow(self):
        mlflow.set_registry_uri(self.config.mlflow_uri)
        tracking_url_type_store = urlparse(mlflow.get_tracking_uri()).scheme

        with mlflow.start_run():
            mlflow.log_params(self.config.all_params)
            mlflow.log_metrics({"loss": self.score[0], "accuracy": self.score[1]})

            if tracking_url_type_store != "file":
                mlflow.keras.log_model(self.model, "model", registered_model_name="InceptionV3Model")
            else:
                mlflow.keras.log_model(self.model, "model")
