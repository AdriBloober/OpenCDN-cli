import base64
import traceback

from Crypto.PublicKey import RSA
from open_cdn import Client

from open_cdn_cli.parser_helper import required_arguments


def create_authentication(args, client: Client):
    authentication_key_identifier = args.authentication_key_identifier
    with open(args.authentication_key_file, "rb") as file:
        try:
            authentication_key = RSA.import_key(file.read())
        except ValueError as e:
            if "PEM is encrypted, but no passphrase available" in e.__repr__():
                passphrase = input("The key is encrypted: Passphrase to encrypt: ")
                authentication_key = RSA.import_key(file.read(), passphrase)
            else:
                traceback.print_exc()
    return client.authentication_manager.create_authentication_token(
        authentication_key_identifier, authentication_key
    )


def generate_authentication_key(args, parser):
    required_arguments(parser, args, ["generate_authentication_key_output"])
    key = RSA.generate(args.generate_authentication_key_size)
    with open(args.generate_authentication_key_output, "wb") as file:
        file.write(key.export_key("PEM"))
    print(
        f"PublicKey = {base64.b64encode(key.publickey().export_key('PEM')).decode('utf-8')}"
    )
    print(f"PrivateKey saved to {args.generate_authentication_key_output}")


def check_authentication(args, parser):
    client = Client(args.api_url)
    required_arguments(
        parser, args, ["authentication_key_identifier", "authentication_key_file"]
    )
    token = create_authentication(args, client)
    client.authentication_manager.test_authentication(token)
    print("Authentication checking was successful!")

