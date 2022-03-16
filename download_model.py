from mlflow.store.artifact.models_artifact_repo import ModelsArtifactRepository
from mlflow.tracking import MlflowClient

client = MlflowClient()
my_model = client.download_artifacts("00307ff7a4bc40a8b0db66cf8e375eee", path="model")
print(f"Placed model in: {my_model}")
