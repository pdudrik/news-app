from datetime import datetime, timezone
from dateutil import parser as dt_parser


_STRPTIME_FORMATS = (
    # RFC 2822 / 822 variants
    "%a, %d %b %Y %H:%M:%S %z",
    "%a, %d %b %Y %H:%M:%S %Z",
    "%a, %d %b %y %H:%M:%S %z",
    "%d %b %Y %H:%M:%S %z",
    # ISO-8601 / RFC 3339 variants
    "%Y-%m-%dT%H:%M:%S%z",
    "%Y-%m-%dT%H:%M:%SZ",
    "%Y-%m-%d %H:%M:%S%z",
    "%Y-%m-%d %H:%M:%S",
    "%Y-%m-%d",
)


def parse_entry_datetime(string_to_parse):
    string = string_to_parse.strip()

    # Parse with dateutil - handles popular formats RFC822, RFC3339,...
    try:
        dt = dt_parser.parse(string)
        if dt.tzinfo is None:
            dt = dt.replace(tzinfo=timezone.utc)
        
        else:
            dt = dt.astimezone(timezone.utc)
        
        return dt
    
    except Exception:
        pass

    # Parse other specified formats
    for format in _STRPTIME_FORMATS:
        try:
            dt = datetime.strptime(string, format)
            if dt.tzinfo is None:
                dt = dt.replace(tzinfo=timezone.utc)
            
            else:
                dt = dt.astimezone(timezone.utc)
            
            return dt

        except Exception:
            pass
    
    # Parsing failed - unknown format
    return None


