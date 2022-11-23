"""
If you need to modify the class for different reasons, this means something( an abstraction) is missing and you need to fix this.
The classes could have more than one method as long as they serve the same purpose
The Single Responsibility Principle (SRP) states that a function or a class should have one responsibility.
Following this principle will help keep your functions small and manageable.
Breaking this rule is sometimes justified, but the more you rely on an individual function to do, the more difficult it will be to understand, update, change, debug, or refactor it.
"""

"""
Let’s say that I have a directory with files, and I need to access the data in those files.
Some of them are archived in .zip, .tar, or .gz formats, so I also need to extract those archives first.


"""

import os
import shutil
import re


def prepare_files(directory_path):
    archive_pattern = re.compile('\.(zip|gz|tar)$')

    for filename in os.listdir(directory_path):
        if archive_pattern.search(filename):
            filepath = os.path.join(directory_path, filename)
            shutil.unpack_archive(filepath)

    return


def prepare_files(directory_path):
    for archive_path in get_archive_paths(directory_path):
        shutil.unpack_archive(archive_path)

    return


def get_archive_filepaths(directory_path):
    archive_paths = []
    for filename in os.listdir(directory_path):
        filepath = os.path.join(directory_path, filename)
        if should_extract(filepath):
            archive_paths.append(filepath)

    return archive_paths


def should_extract(filepath):
    archive_pattern = re.compile('\.(zip|gz|tar)$')
    skip_pattern = re.compile('^skip_')

    should_extract_bool = False
    if not skip_pattern.search(filepath) and archive_pattern.search(filename):
        should_extract_bool = True

    return should_extract_bool
