class Solution:
    def strongPasswordCheckerII(self, password: str) -> bool:
        return len(password) >= 8 and any(_.isalpha() and _.isupper() for _ in password) and any(
            _.isalpha() and _.islower() for _ in password) and any(_.isdigit() for _ in password) and any(
            _ in '!@#$%^&*()-+' for _ in password) and all(
            password[_] != password[_ + 1] for _ in range(len(password) - 1))
