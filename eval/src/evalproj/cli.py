"""Command-line entry for evalproj"""
import argparse


def main(argv=None):
    parser = argparse.ArgumentParser(prog="evalproj", description="EvalProj demo CLI")
    parser.add_argument("--name", "-n", default="World", help="Name to greet")
    args = parser.parse_args(argv)
    print(f"Hello, {args.name}!")


if __name__ == "__main__":
    main()
