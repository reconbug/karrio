
"""Karrio Post NL client settings."""

import attr
import karrio.providers.post_nl.utils as provider_utils


@attr.s(auto_attribs=True)
class Settings(provider_utils.Settings):
    """Post NL connection settings."""

    # required carrier specific properties

    # generic properties
    id: str = None
    test_mode: bool = False
    carrier_id: str = "post_nl"
    account_country_code: str = None
    metadata: dict = {}
