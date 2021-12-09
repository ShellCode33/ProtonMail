# coding: utf-8

from dataclasses import dataclass
from proton.api import Session

ENDPOINT = "/users"

@dataclass(frozen=True)
class User:
    id: str
    name: str
    email: str
    subscribed: bool
    max_storage: int
    used_storage: int
    private_key: str # don't forget that python-gnupg is a dependency of proton
    private_key_fingerprint: str


def api_request(session: Session) -> User:
    resp = session.api_request(endpoint=ENDPOINT)
    user = resp["User"]
    name = user["DisplayName"]
    email = user["Email"]
    subscribed = user["Subscribed"] == 1
    max_storage = user["MaxSpace"]
    used_storage = user["UsedSpace"]

    if len(user["Keys"]) != 1:
        raise ValueError(f"User got {len(user['Keys'])} keys, don't know what to do...")

    private_key = user["Keys"][0]["PrivateKey"]
    private_key_fingerprint = user["Keys"][0]["Fingerprint"]

    return User(
        id=user["ID"],
        name=name,
        email=email,
        subscribed=subscribed,
        max_storage=max_storage,
        used_storage=used_storage,
        private_key=private_key,
        private_key_fingerprint=private_key_fingerprint
    )
