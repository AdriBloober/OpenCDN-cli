from open_cdn import Client, File

from open_cdn_cli.parser_helper import required_arguments


def get_key_filename_pair(args, client):
    if args.file_key is not None and args.file_filename is not None:
        key = args.file_key
        filename = args.file_filename
    elif args.ile_link is not None:
        key, filename = client.file_manager.get_key_and_filename_from_link(
            args.file_link
        )
    else:
        raise ValueError(
            "You should choose a downlod key, filename pair or a download link."
        )
    return key, filename


def download(args, parser):
    required_arguments(parser, args, ["download_output_file"])
    client = Client(args.api_url)
    key, filename = get_key_filename_pair(args, client)

    file = client.file_manager.get(key, filename)
    download_file = args.download_output_file.replace("{FILENAME}", file.filename)
    with open(download_file, "wb") as f:
        f.write(file.content)
    print(f"The file {file} has been saved to {download_file}.")
