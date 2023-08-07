import argparse
import configparser
import json
import traceback
import sys
from time import sleep

from pythorhead import Lemmy


def get_config():
    config = configparser.ConfigParser(interpolation=None)
    read = config.read("config.ini")
    if not read:
        print("Could not read config:")
        traceback.print_exc
        sys.exit(1)

    sections = {i: dict(config.items(i)) for i in config.sections()}
    return sections


parser = argparse.ArgumentParser()
parser.add_argument(
    "--profile",
    action="store_true",
    required=False,
    type=bool,
    help="Migrate your old profile, otherwise migrate community posts.",
)
args = parser.parse_args()


def get_old_lemmy() -> Lemmy:
    lemmy = Lemmy("https://lemmy.world")
    return lemmy


def get_lemmy(username: str, password: str) -> Lemmy:
    lemmy = Lemmy("https://lemmy.fmhy.net")
    lemmy.log_in(username, password)
    return lemmy


if __name__ == "__main__":
    config = get_config()
    old = get_old_lemmy()
    new = get_lemmy(config["Current"]["username"], config["Current"]["password"])
    if not args.profile:
        print("Will migrate communities.")
        old_com = old.discover_community(config["Community Migration"]["old"])
        old_posts = old.post.list(
            old_com, limit=int(config["Community Migration"]["limit"])
        )
        community = new.discover_community(config["Community Migration"]["new"])

        for post in old_posts:
            post_name = post["post"]["name"]
            post_body = post["post"].get("body", "")
            post_url = post["post"].get("url", "")

            if post_body:
                try:
                    new.post.create(community, name=post_name, body=post_body)  # type: ignore
                    print(f"Successfully created a post with body for '{post_name}'")
                    sleep(10)
                except Exception as e:
                    print(
                        f"Error while creating post with body for '{post_name}': {str(e)}"
                    )

            elif post_url:
                try:
                    new.post.create(community, name=post_name, url=post_url)  # type: ignore
                    print(f"Successfully created a post with URL for '{post_name}'")
                    sleep(10)
                except Exception as e:
                    print(
                        f"Error while creating post with URL for '{post_name}': {str(e)}"
                    )

    else:
        old_user = old.user.get(username=config["Profile Migration"]["old"])
        if not old_user:
            raise Exception("No valid username found.")
        print(json.dumps(old_user, indent=4))
