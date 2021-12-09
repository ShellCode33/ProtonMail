# coding: utf-8

from proton.api import Session
from protonmail.api.contacts import Contact, ContactInfo
from protonmail.api.labels import Label

from dataclasses import dataclass

from typing import List, Dict, Union

ENDPOINT = "/mail/v4/conversations"

@dataclass(frozen=True)
class Message:
    id: str
    subject: str
    sender: ContactInfo
    reply_to: ContactInfo
    is_unread: bool
    is_encrypted: bool
    headers: str
    body: str # TODO : decrypt PGP message
    mime_type: str
    spam_score: int
    attachements_count: int
    time: int # send/receive timestamp

@dataclass(frozen=True)
class Conversation:
    id: str
    subject: str
    senders: List[Contact]
    recipients: List[Contact]
    messages_count: int
    unread_messages_count: int


def api_request(session: Session, page: int = 0, items_per_page: int = 50, label: Label = None) -> List[Conversation]:

    params: Dict[str, Union[str, int]]

    # TODO : loop through pages
    params = {
        "Page": page,
        "PageSize": items_per_page,
        "Desc": 1
    }

    if label:
        params["LabelID"] = label.id

    resp = session.api_request(endpoint=ENDPOINT, params=params)

    conversations = []

    for conversation in resp["Conversations"]:

        senders = []
        recipients = []

        for sender in conversation["Senders"]:
            senders.append(ContactInfo(sender["Name"], sender["Address"]))

        for recipient in conversation["Recipients"]:
            recipients.append(ContactInfo(recipient["Name"], recipient["Address"]))

        conversations.append(
            Conversation(
                id=conversation["ID"],
                subject=conversation["Subject"],
                senders=senders,
                recipients=recipients,
                messages_count=conversation["NumMessages"],
                unread_messages_count=conversation["NumUnread"]
            )
        )

    return conversations
