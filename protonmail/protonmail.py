# coding: utf-8

import ast
import os
import os.path
from getpass import getpass

from typing import List

from proton.api import Session
from protonmail.api import contacts, labels, conversations, users
from protonmail.api.contacts import Contact
from protonmail.api.conversations import Conversation
from protonmail.api.labels import Label
from protonmail.api.users import User

class ProtonMail:

    API_URL = "https://mail.protonmail.com/api"

    def __init__(self, session: Session = None):

        try:
            with open("/tmp/proton/session.json", "r") as session_file:
                dump = ast.literal_eval(session_file.read())

                self.session = session or Session.load(
                    dump=dump,
                    log_dir_path="/tmp/proton",
                    cache_dir_path="/tmp/proton",
                    tls_pinning=False
                )

        except FileNotFoundError:
            self.session = session or Session(
                api_url=ProtonMail.API_URL,
                log_dir_path="/tmp/proton",
                cache_dir_path="/tmp/proton",
                tls_pinning=False
            )

    def auth(self, username: str, password: str = None, stay_connected: bool = False):
        self.session.enable_alternative_routing = ""

        if not os.path.exists("/tmp/proton/session.json"):
            self.session.authenticate(username, password or getpass())

        if stay_connected:
            session_dump = self.session.dump()

            with open("/tmp/proton/session.json", "w") as session_file:
                session_file.write(str(session_dump))

    @property
    def me(self) -> User:
        return users.api_request(self.session)

    @property
    def conversations(self, page: int = 0, items_per_page: int = 50, label: Label = None) -> List[Conversation]:
        return conversations.api_request(self.session, page, items_per_page, label)


    @property
    def contacts(self, page: int = 0, items_per_page: int = 1000) -> List[Contact]:
        return contacts.api_request(self.session, page, items_per_page)

    @property
    def labels(self) -> List[Label]:
        return labels.api_request(self.session)




