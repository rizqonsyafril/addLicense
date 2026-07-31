# === Stage 25: Добавь обработку некорректных дат и понятные сообщения об ошибках ===
# Project: MilestoneMap
import datetime as dt


def parse_date(date_str):
    """Parse a date string in various formats and return a date object."""
    if not date_str:
        raise ValueError("Date string is empty")
    try:
        return dt.datetime.strptime(str(date_str).strip(), "%Y-%m-%d").date()
    except ValueError:
        pass
    for fmt in ("%m/%d/%Y", "%d.%m.%Y", "%d-%m-%Y"):
        try:
            return dt.datetime.strptime(str(date_str).strip(), fmt).date()
        except ValueError:
            continue
    raise ValueError(
        f"Cannot parse date '{date_str}' in formats: YYYY-MM-DD, MM/DD/YYYY, DD.MM.YYYY, DD-MM-YYYY"
    )


def validate_deadline(start_date, deadline):
    """Validate that a deadline is after or equal to the start date."""
    try:
        start = dt.date.fromisoformat(str(start_date))
    except (ValueError, TypeError):
        raise ValueError(f"Invalid start date: {start_date}")
    if not isinstance(deadline, dt.date) and not isinstance(deadline, str):
        return deadline
    try:
        end = dt.date.fromisoformat(str(deadline).strip())
    except (ValueError, TypeError):
        raise ValueError(f"Invalid deadline date: {deadline}")
    if start > end:
        raise ValueError(
            f"Deadline ({end}) must be on or after the start date ({start})."
        )
    return end


def safe_parse_date(date_str, default=None):
    """Try to parse a date string; return default on failure."""
    if not date_str:
        return default
    try:
        return parse_date(str(date_str).strip())
    except ValueError:
        return default
