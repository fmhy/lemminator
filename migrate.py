from pythorhead import Lemmy
import credentials
from time import sleep


def get_old_lemmy():
    lemmy = Lemmy("https://lemmy.world")
    return lemmy


def get_lemmy():
    lemmy = Lemmy("https://lemmy.fmhy.net")
    lemmy.log_in(credentials.username, credentials.password)
    return lemmy


if __name__ == "__main__":
    old = get_old_lemmy()
    new = get_lemmy()
    old_com = old.discover_community(credentials.old_community)
    old_posts = old.post.list(old_com, limit=50)
    community = new.discover_community(credentials.new_community)

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
                print(f"Error while creating post with URL for '{post_name}': {str(e)}")
