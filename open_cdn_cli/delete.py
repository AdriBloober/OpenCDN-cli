from open_cdn import Client, FileTarget

from open_cdn_cli.download import get_key_filename_pair
from open_cdn_cli.parser_helper import required_arguments


def delete(args, parser):
    required_arguments(parser, args, ["private_key"])
    client = Client(args.api_url)
    key, filename = get_key_filename_pair(args, client)
    client.file_manager.delete(FileTarget(key, filename), args.private_key)
    print("The file has been successfully deleted!")
