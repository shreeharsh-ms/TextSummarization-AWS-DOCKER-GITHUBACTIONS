import os
from box.exceptions import BoxValueError
import yaml
from textsummarization_aws_docker_githubactions.logging import logger
from ensure import ensure_annotations
from box import Box
from pathlib import Path
from typing import Any
from types import NoneType



@ensure_annotations
def read_yaml_file(file_path: Path) -> Box:
    """
    Reads a YAML file and returns its content as a Box object.
    
    Args:
        file_path (Path): The path to the YAML file.
        
    Returns:
        Box: The content of the YAML file as a Box object.
    """
    try:
        with open(file_path, 'r') as file:
            content = yaml.safe_load(file)
            return Box(content)
    except FileNotFoundError as e:
        logger.error(f"YAML file not found: {file_path}")
        raise e
    except yaml.YAMLError as e:
        logger.error(f"Error reading YAML file: {file_path} - {e}")
        raise BoxValueError(f"Invalid YAML format in {file_path}") from e

@ensure_annotations
def create_directory(directory_path: list, verbose = True) -> NoneType:
    for path in directory_path:
        path = Path(path)
        if not path.exists():
            try:
                path.mkdir(exist_ok=True)
                if verbose:
                    logger.info(f"Directory created: {path}")
            except Exception as e:
                logger.error(f"Error creating directory {path}: {e}")
        else:
            if verbose:
                logger.info(f"Directory already exists: {path}")
    return None

@ensure_annotations
def get_size_of_file(file_path: Path) -> int:
    """
    Returns the size of the file in bytes.
    
    Args:
        file_path (Path): The path to the file.
        
    Returns:
        int: Size of the file in bytes.
    """
    try:
        return file_path.stat().st_size
    except FileNotFoundError as e:
        logger.error(f"File not found: {file_path}")
        raise e
    except Exception as e:
        logger.error(f"Error getting size of file {file_path}: {e}")
        raise e 