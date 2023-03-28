from typing import List


class Solution:

    def uniqueEmail(self, emails: List[str]) -> List[str]:
        uniqueEmail = set()

        for email in emails:
            local_name, domain = email.split('@')
            local_name = local_name.split('+')[0]
            local_name = local_name.replace('.', '')
            uniqueEmail.add((local_name, domain))

        return len(uniqueEmail)


sol = Solution()
print(
    sol.uniqueEmail([
        "test.email+alex@leetcode.com", "test.e.mail+bob.cathy@leetcode.com",
        "testemail+david@lee.tcode.com"
    ]))
print(sol.uniqueEmail(["a@leetcode.com", "b@leetcode.com", "c@leetcode.com"]))
