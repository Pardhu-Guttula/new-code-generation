class MaskedPasswordPolicy:
    def __init__(self, show_start: int = 1, show_end: int = 1):
        self.show_start = show_start
        self.show_end = show_end

    def mask_password(self, password: str) -> str:
        if len(password) <= self.show_start + self.show_end:
            return '*' * len(password)
        
        return (
            password[:self.show_start] + 
            '*' * (len(password) - self.show_start - self.show_end) + 
            password[-self.show_end:]
        )