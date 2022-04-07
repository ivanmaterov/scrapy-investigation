# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

from dataclasses import dataclass, field
from typing import Optional
from itemloaders.processors import TakeFirst, MapCompose


def cut_last_two_symbols(value: str) -> str:
    """Cut two symbols.

    Data from mirasmart contains two strage symbols in the end of string

    Args:
        value(str): string with two extra symbols

    Returns:
        string without two last symbols

    """
    return value[:-2]


@dataclass
class DetailItem:
    """Item for storing data."""
    session_name: Optional[str] = field(
        default=None,
        metadata=dict(
            input_processor=MapCompose(cut_last_two_symbols),
            output_processor=TakeFirst(),
        )
    )
    topic: Optional[str] = field(
        default=None,
        metadata=dict(
            input_processor=MapCompose(cut_last_two_symbols),
            output_processor=TakeFirst(),
        )
    )
    program_number: Optional[str] = field(
        default=None,
        metadata=dict(
            input_processor=MapCompose(cut_last_two_symbols),
            output_processor=TakeFirst(),
        )
    )
    abstract: Optional[str] = field(
        default=None,
        metadata=dict(
            input_processor=MapCompose(cut_last_two_symbols),
            output_processor=TakeFirst(),
        )
    )
