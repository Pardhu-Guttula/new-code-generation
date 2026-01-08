class MaskedPasswordPolicy:
    def __init__(self, show_start: int = 0, show_end: int = 0):
        self.show_start = show_start
        self.show_end = show_end

    def mask_password(self, password: str) -> str:
        if self.show_start >= len(password) or self.show_end >= len(password):
            return '*' * len(password)

        if self.show_start + self.show_end >= len(password):
            return '*' * len(password)

        return password[:self.show_start] + '*' * (len(password) - (self.show_start + self.show_end)) + password[-self.show_end:]