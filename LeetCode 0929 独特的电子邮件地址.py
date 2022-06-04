from typing import List


class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        s = set()
        for email in emails:
            local, domain = email[:email.find('@')].replace('.', ''), email[email.find('@') + 1:]
            if local.find('+') != -1:
                local = local[:local.find('+')]
            s.add(local + '@' + domain)
        return len(s)
