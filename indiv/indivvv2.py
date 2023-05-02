import os
import argparse

def build_tree(dir_path, level, show_files, show_dirs_only):
    if not os.path.isdir(dir_path):
        return

    # Prepare the indent string
    indent = ""
    if level > 0:
        indent = "|   " * (level - 1)
        indent += "|-- "

    # Print the current directory name
    print(indent + os.path.basename(dir_path) + "/")

    # Recursively print the contents of subdirectories
    if level >= 0:
        for item in sorted(os.listdir(dir_path)):
            item_path = os.path.join(dir_path, item)
            if os.path.isdir(item_path):
                build_tree(item_path, level + 1, show_files, show_dirs_only)
            elif show_files and not show_dirs_only:
                print(indent + "|   " * level + "|-- " + item)

# Set up command line arguments
parser = argparse.ArgumentParser(description='Print the directory tree')
parser.add_argument('dir_path', metavar='dir_path', type=str, nargs='?',
                    default='.', help='the directory path')
parser.add_argument('-l', '--level', type=int, default=-1,
                    help='the maximum recursion depth')
parser.add_argument('-f', '--show-files', action='store_true',
                    help='show files in addition to directories')
parser.add_argument('-d', '--show-dirs-only', action='store_true',
                    help='show only directories, no files')

# Parse the command line arguments
args = parser.parse_args()

# Build and print the directory tree
build_tree(args.dir_path, 0, args.show_files, args.show_dirs_only)


