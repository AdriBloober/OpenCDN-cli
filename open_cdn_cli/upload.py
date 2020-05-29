from open_cdn_cli.authentication import create_authentication
from open_cdn_cli.parser_helper import required_arguments
from open_cdn import Client


def upload(args, parser):
    required_arguments(parser, args, ["upload_file"])
    client = Client(args.api_url)
    if (
        args.authentication_key_identifier is not None
        and args.authentication_key_file is not None
    ):
        token = create_authentication(args, client)
        file = client.file_manager.post(
            open(args.upload_file, "r"),
            args.upload_file,
            token,
        )
        client.authentication_manager.delete_authentication_token(token)
    else:
        file = client.file_manager.post(open(args.upload_file, "r"), args.upload_file)
    upload_output_type = args.upload_output_type.lower()
    if upload_output_type == "all":
        print(file.__repr__())
    elif upload_output_type == "key":
        print(file.key)
    elif upload_output_type == "link":
        print(client.file_manager.get_link_from_file(file.get_target()))
