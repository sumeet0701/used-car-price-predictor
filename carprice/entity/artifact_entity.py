from dataclasses import dataclass

class DataInjestinArtifact:
    feature_score_file_path = str
    training_file_path = str
    test_file_path : str
    
