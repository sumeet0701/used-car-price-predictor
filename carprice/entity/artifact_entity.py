from dataclasses import dataclass

@dataclass
class DataInjestinArtifact:
    feature_store_file_path: str
    train_file_path : str
    test_file_path : str
    
