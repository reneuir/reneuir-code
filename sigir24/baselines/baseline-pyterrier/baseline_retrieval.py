#!/usr/bin/env python3
# Load a patched ir_datasets that loads the injected data inside the TIRA sandbox
from tira.third_party_integrations import ir_datasets, get_output_directory
from pathlib import Path
import pandas as pd

if __name__ == '__main__':
    # In the TIRA sandbox, this is the injected ir_dataset, injected via the environment variable TIRA_INPUT_DIRECTORY
    dataset = ir_datasets.load('workshop-on-open-web-search/document-processing-20231027-training')

    # The expected output directory, injected via the environment variable TIRA_OUTPUT_DIRECTORY
    output_dir = get_output_directory('.')
    
    # Retrieval approaches are expected to produce a TREC-style run.txt file in the output directory.
    output_file = Path(output_dir) / 'run.txt'
    
    # You can pass as many additional arguments to your program, e.g., via argparse, to modify the behaviour of your program.
    
    # Step 1: build an Index. For a real scenario, you should pass the index from the previous stage of the pipeline.

    # Step 2: produce a ranking
    
    # Step 3: persist the ranking
