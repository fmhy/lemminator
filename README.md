## (mali)ciouscompliance

Note: does not migrate pictures etc yet.

This is a script to transfer your old community posts from `lemmy.fmhy.ml` to `lemmy.fmhy.net`.
It's only for community moderators, so please don't use it to spam lmao. You should also lock your community before this and don't run it twice.

It uses `lemmy.world` for fetching old posts though that probably won't do due to how federation works. It's also limited to 50 posts as putting anything higher than whats actually in the community makes Lemmy api not like it, but you can just change the code if thats not what you want.

This is ratelimited by 10 seconds so you don't get banned and accidentally launch a ddos on the solar system.

## usage

`pip install -r requirements.txt`, rename `credentials.py.example` and fill in details, then `python migrate.py` and tada!!

Copyright (c) 2023 taskylizard. All Rights Reserved.
