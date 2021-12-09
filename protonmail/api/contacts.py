# coding: utf-8

from dataclasses import dataclass

from proton.api import Session

ENDPOINT = "/contacts/v4/contacts/emails"


@dataclass(frozen=True)
class ContactInfo:
    name: str
    email: str


@dataclass(frozen=True)
class Contact:
    # TODO : many more fields to support
    id: str
    info: ContactInfo
    last_used_time: int = 0


def api_request(session: Session, page: int = 0, items_per_page: int = 1000):
    resp = session.api_request(endpoint=ENDPOINT, params={
        "Page": page,
        "PageSize": items_per_page
    })

    contacts = []

    for contact in resp["ContactEmails"]:
        contacts.append(
            Contact(
                id=contact["ID"],
                info=ContactInfo(contact["Name"], contact["CanonicalEmail"]),
                last_used_time=contact["LastUsedTime"]
            )
        )

    return contacts
