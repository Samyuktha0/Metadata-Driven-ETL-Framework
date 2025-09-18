import yaml
from transform import apply_transforms

with open('metadata/pipeline_config.yaml') as f:
    config = yaml.safe_load(f)

apply_transforms(config)
