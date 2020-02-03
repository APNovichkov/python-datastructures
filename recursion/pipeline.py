#!/usr/bin/env python3

import json
import sys
import logger
import importlib
import time
import os
from datetime import datetime
import s3_tools


def process_manifest(filename):
    with open(filename, "r") as mf:
        data = json.load(mf)
        logger.log("Successfully loaded data for pipeline: {}".format(data['params']['name']))
        run_pipeline(data)

def run_pipeline(data):
    is_single_sample = data['params']['single_sample']
    s3_bucket_name = data['params']['s3_bucket_name']
    s3_project_name = data['params']['s3_project_name']

    if is_single_sample == "true":
        logger.log("Running single sample pipeline")
        sample_name = data['params']['sample_name']
        run_ss_pipeline(data['configuration'], sample_name, s3_bucket_name, s3_project_name)
    else:
        logger.log("Running full project pipeline")

        sample_list = []

        with open(data['params']['sample_list_filepath'], 'r') as f:
            for line in f:
                sample_list.append(line.strip())

        run_fp_pipeline(data['configuration'], sample_list, s3_bucket_name, s3_project_name)


def run_ss_pipeline(configuration, sample_name, s3_bucket, s3_project):
    logger.log("Running pipeline for sample: {}".format(sample_name))

    steps = configuration['steps']

    logger.log("Going to run steps in this order")
    for step in steps:
        logger.log("-{} (version: {})".format(step['name'], step['version']))

    print("============================================================")

    for step in steps:
        app_name = step['name']
        logger.log("Running {} (version: {})".format(app_name, step['version']))

        start = time.time()

        app_executible = importlib.import_module(step['script_name'])
        app_executible.run_app(step['arguments'], step['input_data_source'], step['resource_path'], sample_name, s3_bucket, s3_project)

        end = time.time()
        step_time = (end - start)  # In seconds

        # Write metadata.txt file
        write_step_metadata(step, step_time, s3_bucket, s3_project, sample_name)

        logger.log("Finished running {} (version: {})".format(app_name, step['version']))

        print("============================================================")

def run_fp_pipeline(configuration, sample_list, s3_bucket, s3_project):
    for sample_name in sample_list:
        logger.log("Running pipeline for sample: {}".format(sample_name))

        steps = configuration['steps']

        logger.log("Going to run steps in this order")
        for step in steps:
            logger.log("-{} (version: {})".format(step['name'], step['version']))

        print("============================================================")

        for step in steps:

            app_name = step['name']
            logger.log("Running {} (version: {})".format(app_name, step['version']))

            start = time.time()

            app_executible = importlib.import_module(step['script_name'])
            app_executible.run_app(step['arguments'], step['input_data_source'], step['resource_path'], sample_name, s3_bucket, s3_project)

            end = time.time()
            step_time = (end - start)  # In seconds

            write_step_metadata(step, step_time, s3_bucket, s3_project, sample_name)

            logger.log("Finished running {} (version: {})".format(app_name, step['version']))

            print("============================================================")


def write_step_metadata(step_config, step_time, s3_bucket, s3_project, sample_name):
    meta_filename = "metadata.txt"
    pipeline_tmp = "pipeline-tmp"
    meta_filepath = os.path.join(pipeline_tmp, meta_filename)

    if not os.path.exists(pipeline_tmp):
        os.mkdir(pipeline_tmp)

    if os.path.exists(meta_filepath):
        os.remove(meta_filepath)

    logger.log("Creating metadata file for run of app: {}...".format(step_config['name']))

    with open(meta_filepath, "w") as f:
        f.write("Time and Date ran: {}\n".format(datetime.now()))
        f.write("---------------------------------------------\n")
        f.write("App Name: {}\n".format(step_config['name']))
        f.write("App Version: {}\n".format(step_config['version']))
        f.write("Input Data Source: {}\n".format(step_config['input_data_source']))
        f.write("Arguments (key,value):\n")

        for key, value in step_config['arguments'].items():
            f.write("-{} -> {}\n".format(key, value))

        f.write("\nTime took to run {}: {} seconds".format(step_config['name'], step_time))
        f.close()

    s3_meta_filepath = os.path.join(s3_project, sample_name, step_config['name'], meta_filename)
    s3_tools.upload_file(meta_filepath, s3_bucket, s3_meta_filepath)

    logger.log("Saved metadata file for run of app: {}".format(step_config['name']))

    if os.path.exists(meta_filepath):
        os.remove(meta_filepath)


def time_it(func):
    """Time the runtime of a function that it is wrapping."""

    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()

        print("{} took {} ms to complete".format(func.__name__, (end - start) * 1000))

        return result

    return wrapper


if __name__ == "__main__":
    mf_filename = sys.argv[1]

    process_manifest(mf_filename)
