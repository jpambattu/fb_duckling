from .utils import get_default_locale, get_default_url, get_default_port, get_default_timezone, get_default_reftime


class BaseClass(object):

    default_locale = get_default_locale()  # en_US
    default_url = get_default_url()  # http://0.0.0.0
    default_port = get_default_port()  # 8000
    default_timezone = get_default_timezone() # America/Los_Angeles
    default_reftime = get_default_reftime()   # Unix epoch in milliseconds

    def __init__(self, locale=default_locale, url=default_url, port=default_port, timezone=default_timezone, reftime=default_reftime):

        self.locale = locale or "en_US"
        self.url = url or "http://0.0.0.0"
        self.port = port or 8000
        self.timezone = timezone or "America/Los_Angeles"
        self.reftime = reftime
