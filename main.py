import argparse
import json
from src.core import ModelLineage

def main():
    parser = argparse.ArgumentParser(description='AI Model Lineage')
    parser.add_argument('--config', help='Configuration file')
    args = parser.parse_args()
    with open(args.config, 'r') as f:
        config = json.load(f)
    model_lineage = ModelLineage(config)
    model_lineage.run()
if __name__ == '__main__':
    main()