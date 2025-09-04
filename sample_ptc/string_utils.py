import time

class StringUtils:
    @staticmethod
    def to_upper(s: str) -> str:
        """Convert string to uppercase."""
        return s.upper()

    @staticmethod
    def to_lower(s: str) -> str:
        """Convert string to lowercase."""
        return s.lower()

    @staticmethod
    def is_palindrome(s: str) -> bool:
        """Check if a string is a palindrome."""
        cleaned = ''.join(c.lower() for c in s if c.isalnum())
        return cleaned == cleaned[::-1]

    @staticmethod
    def reverse(s: str) -> str:
        """Reverse the given string."""
        return s[::-1]

    @staticmethod
    def count_vowels(s: str) -> int:
        """Count the number of vowels in a string."""
        return sum(1 for c in s.lower() if c in 'aeiou')
    
    @staticmethod
    def epoch_seconds_as_string(dt) -> str:
        """Return epoch seconds as string from a datetime object."""
        if hasattr(dt, 'timestamp'):
            return str(int(dt.timestamp()))
        else:
            return str(int(time.mktime(dt.timetuple())))

    @staticmethod
    def epoch_millis_as_string(dt) -> str:
        """Return epoch milliseconds as string from a datetime object."""
        if hasattr(dt, 'timestamp'):
            return str(int(dt.timestamp() * 1000))
        else:
            return str(int(time.mktime(dt.timetuple()) * 1000))

    @staticmethod
    def human_readable_datetime(dt) -> str:
        """Return human readable datetime string from a datetime object."""
        return dt.strftime('%Y-%m-%d %H:%M:%S')