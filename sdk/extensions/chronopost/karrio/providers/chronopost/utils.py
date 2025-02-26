"""Karrio Chronopost client settings."""

from chronopost_lib.shippingservice import headerValue
from karrio.core.settings import Settings as BaseSettings


class Settings(BaseSettings):
    """Chronopost connection settings."""

    account_number: str
    password: str
    id_emit: str = "CHRFR"
    language: str = "en_GB"

    account_country_code: str = "FR"
    metadata: dict = {}

    @property
    def carrier_name(self):
        return "chronopost"

    @property
    def server_url(self):
        return "https://ws.chronopost.fr"

    @property
    def tracking_url(self):
        return "https://www.chronopost.fr/tracking-no-cms/suivi-page?listeNumerosLT={}"

    @property
    def header_value(self):
        return headerValue(accountNumber=self.account_number, idEmit=self.id_emit)
