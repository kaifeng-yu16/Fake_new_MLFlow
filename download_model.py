from mlflow.store.artifact.models_artifact_repo import ModelsArtifactRepository
from mlflow.tracking import MlflowClient

client = MlflowClient()
my_model = client.download_artifacts("1a3dacf13bbf49e884fa0895cade96b5", path="model")
print(f"Placed model in: {my_model}")
