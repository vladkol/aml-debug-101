"""
Basic step to do a task on a compute
"""
import logging
import argparse
import debugpy
from azureml.core import Run
from amldebugutils import start_remote_debugging_from_args

def main():
    """Step main function
    """
    # can use Python logging
    logging.basicConfig(level=logging.INFO)
    log: logging.Logger = logging.getLogger(__name__)
    log.info("Basic step")

    # Retrieve current step's AML Run object
    aml_run = Run.get_context()

    # parse step arguments
    parser = argparse.ArgumentParser()
    # FileDataset argument
    parser.add_argument("--dataset", type=str, required=True)
    # debugging argument
    parser.add_argument('--is-debug', type=str, required=True)

    args, _ = parser.parse_known_args()

    # FileDataset is passed as a directory path
    dataset_directory_path = args.dataset

    if args.is_debug.lower() == 'true':
        print("Let's start debugging")
        if start_remote_debugging_from_args():
            debugpy.breakpoint()
            print("We are debugging!")
        else:
            print("Could not connect to a debugger!")

    # print to console output log (70_driver_log.txt)
    print(f"#### Dataset directory: {dataset_directory_path}")

    # log metrics in the current run
    aml_run.log(name="my string metric", value="magic value")
    aml_run.log(name="my numeric metric", value=42)


if __name__ == "__main__":
    main()
