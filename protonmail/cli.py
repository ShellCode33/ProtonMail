# coding: utf-8

from IPython import embed
import argparse
from protonmail import ProtonMail
from proton import ProtonAPIError

class Color:
    GREEN = "\u001b[32m"
    YELLOW = "\u001b[33m"
    RED = "\u001b[31m"
    RESET = "\u001b[0m"


class Logger:

    @staticmethod
    def info(msg: str):
        print(f"{Color.GREEN}[INFO] {Color.RESET}{msg}")

    @staticmethod
    def warning(msg: str):
        print(f"{Color.YELLOW}[WARNING] {Color.RESET}{msg}")

    @staticmethod
    def error(msg: str):
        print(f"{Color.RED}[ERROR] {Color.RESET}{msg}")


def main() -> None:
    parser = argparse.ArgumentParser(description='Welcome to the ProtonMail utility !')
    parser.add_argument("username", help='The username to log in with')

    parser.add_argument("--filter", help='Returns a list of emails that meet the given filter', required=True)
    parser.add_argument("--summary", action='store_true', help='Prints a summary of filtered emails')
    parser.add_argument("--mark-as", choices=["read", "unread"], help='Set filtered emails state')
    parser.add_argument("--labelize", help='Labelize filtered emails with given label name')

    args = parser.parse_args()

    try:
        client = ProtonMail()
        client.auth(args.username)
        Logger.info(f"You logged in successfully as {args.username}")

    except ProtonAPIError as pae:
        Logger.error(str(pae))
        Logger.error("Something went wrong while trying to use ProtonMail's API")

    except Exception as exc:
        Logger.error(str(exc))

    embed()


if __name__ == "__main__":
    main()
