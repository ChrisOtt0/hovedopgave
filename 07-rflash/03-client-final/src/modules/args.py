import argparse
import os
import sys

parser = argparse.ArgumentParser(
    prog="Remote flash client",
    description="Sends flash configuration and binary to remote flash server.",
    epilog="Use -h to print help information"
)

parser.add_argument(
    "-c",
    "--config-path",
    dest="configpath",
    required=True,
    help="Path to config TOML file."
)

parser.add_argument(
    "-b",
    "--binary-path",
    dest="binarypath",
    required=True,
    help="Path to flashable binary."
)

parser.add_argument(
    "-k",
    "--key-dir",
    dest="keydir",
    required=True,
    help="Path to key directory, where keys for signing are stored."
)

parser.add_argument(
    "-r",
    "--retries",
    dest="retries",
    required=False,
    type=int,
    default=3,
    help="Amount of retries if server fails. Defaults to 3."
)


def get_args():
    """
    Get arguments for the program.
    """
    args = parser.parse_args()

    # Create absolute paths, if relative supplied
    if not os.path.isabs(args.configpath):
        args.configpath = os.path.abspath(args.configpath)

    if not os.path.isabs(args.binarypath):
        args.binarypath = os.path.abspath(args.binarypath)

    if not os.path.isabs(args.keydir):
        args.keydir = os.path.abspath(args.keydir)

    # Ensure paths are valid
    if not os.path.isfile(args.configpath):
        print("Supplied configpath is not a valid file.")
        sys.exit(1)

    if not os.path.isfile(args.binarypath):
        print("Supplied binarypath is not a valid file.")
        sys.exit(1)

    if not os.path.isdir(args.keydir):
        print("Supplied keypath is not a valid directory.")
        sys.exit(1)
    
    # Ensure keys exist
    symkey = os.path.join(args.keydir, "agsymkey")
    if not os.path.exists(symkey) and not os.path.isfile(symkey):
        print("Supplied key directory does not contain the symmetric key.")
        sys.exit(1)

    privkey = os.path.join(args.keydir, "agprivkey")
    if not os.path.exists(privkey) and not os.path.isfile(privkey):
        print("Supplied key directory does not contain the private key.")
        sys.exit(1)

    # Return args
    return args