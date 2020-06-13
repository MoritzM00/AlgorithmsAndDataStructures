import os


def find_files(suffix, path):
    """
    Find all files beneath path with file name suffix.

    Args:
      suffix(str): suffix of the file name to be found
      path(str): path of the file system

    Returns:
       a list of paths
    """
    return find_files_worker(suffix, path, [])


def find_files_worker(suffix, path, acc):
    """
    Worker function of find_files
    Searches the given path recursively for the specified file suffix

    :param suffix: the file suffix
    :param path: the path to a dir/file
    :param acc: the accumulator (list), saves all files with the given suffix
    :return: the list with all paths to files with the given suffix
    """
    if os.path.isdir(path):
        items = os.listdir(path)
        for item in items:
            # create the new path with this file/ dir and step down recursively
            new_path = os.path.join(os.sep, path, item)
            find_files_worker(suffix, new_path, acc)

    elif path.endswith(suffix):
        acc.append(path)

    return acc
