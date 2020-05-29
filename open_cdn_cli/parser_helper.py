def required_arguments(parser, args, arguments):
    for argument in arguments:
        if not hasattr(args, argument) or getattr(args, argument) is None:
            print(f"You must specifiy the --{argument.replace('_', '-')} argument!")
            parser.print_help()
            exit(1)