# coding: utf-8

from enum import Enum
from dataclasses import dataclass

from typing import List

from proton.api import Session

ENDPOINT = "/v4/labels"

class LabelType(Enum):
    LABEL = 1
    _SOMETHING = 2
    FOLDER = 3


@dataclass(frozen=True)
class Label:
    # TODO : many more fields to support
    id: str
    name: str
    type: LabelType


def api_request(session: Session) -> List[Label]:
    labels = []

    for label_type in range(3):
        resp = session.api_request(endpoint=ENDPOINT, params={
            "Type": label_type + 1
        })

        for label in resp["Labels"]:
            labels.append(
                Label(
                    id=label["ID"],
                    name=label["Name"],
                    type=LabelType(label_type + 1)
                )
            )

    return labels
