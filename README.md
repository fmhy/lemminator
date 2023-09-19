## lemminator

Note: does not migrate pictures etc yet.

This is a script to transfer your old community posts from `lemmy.fmhy.ml` to `lemmy.dbzer0.com` (or whatever instance you want.)
**This is only for community moderators**, so please don't use it to spam lmao. 

It uses `lemmy.world` (or any other instance) for fetching old posts that were federated before the instance went down. 

This is ratelimited by 10 seconds so you don't get banned and accidentally launch a ddos on the solar system.

## usage
- Lock your community before doing *anything* and don't run it twice.
- `pip install -r requirements.txt`
- rename `config.ini.example` to `config.ini` and fill in details
- `python migrate.py` and tada!!

---

Copyright (c) 2023 taskylizard. Unlicensed.
