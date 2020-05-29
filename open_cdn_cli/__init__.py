import argparse

from open_cdn import Client

from open_cdn_cli.authentication import (
    generate_authentication_key,
    check_authentication,
)
from open_cdn_cli.delete import delete
from open_cdn_cli.download import download
from open_cdn_cli.upload import upload

parser = argparse.ArgumentParser(description="OpenCDN Cli")
parser.add_argument(
    "action",
    metavar="ACTION",
    type=str,
    choices=[
        "upload",
        "download",
        "delete",
        "check_authentication",
        "generate_authentication_key",
        "check_version"
    ],
    help="The action, which you would like to execute.",
)
parser.add_argument(
    "-AU", "--api-url", type=str, default="http://localhost", help="The url of the api."
)

# Authentication
parser.add_argument(
    "-aki",
    "--authentication-key-identifier",
    type=str,
    required=False,
    help="The identifier of the authentication key.",
)
parser.add_argument(
    "-akf",
    "--authentication-key-file",
    type=str,
    required=False,
    help="The authentication key file, which contains the private key.",
)

# generate_authentication_key

parser.add_argument(
    "-gaks",
    "--generate-authentication-key-size",
    type=int,
    default=1024,
    help="The keysize of the generating key.",
)
parser.add_argument(
    "-gako",
    "--generate-authentication-key-output",
    type=str,
    required=False,
    help="The path to the private key output file.",
)

# upload
parser.add_argument(
    "-uf",
    "--upload-file",
    type=str,
    required=False,
    help="The file, which you would like to upload.",
)
parser.add_argument(
    "-uot",
    "--upload-output-type",
    type=str,
    choices=["all", "key", "link"],
    default="all",
    help="The output type is the type, how the cli send the output to you.",
)

# download

parser.add_argument(
    "-dof",
    "--download-output-file",
    type=str,
    default="./{FILENAME}",
    help="The output file, where the download file should been saved. Use '{FILENAME}' to set here the filename.",
)
parser.add_argument(
    "-fk",
    "--file-key",
    type=str,
    required=False,
    help="You can use a key, filename pair to target the file.",
)
parser.add_argument(
    "-ff",
    "--file-filename",
    type=str,
    required=False,
    help="You can use a key, filename pair to target the file.",
)
parser.add_argument(
    "-fl",
    "--file-link",
    type=str,
    required=False,
    help="You can use a link to target the file.",
)

# delete
parser.add_argument(
    "-pk",
    "--private-key",
    type=str,
    required=False,
    help="The private key for the file.",
)

args = parser.parse_args()


def run_action():
    action = args.action.lower()
    if action == "upload":
        upload(args, parser)
    elif action == "generate_authentication_key":
        generate_authentication_key(args, parser)
    elif action == "download":
        download(args, parser)
    elif action == "delete":
        delete(args, parser)
    elif action == "check_authentication":
        check_authentication(args, parser)
    elif action == "check_version":
        client = Client(args.api_url)
        client.version_manager.check_version()
        print("Version checking was successful!")


run_action()
