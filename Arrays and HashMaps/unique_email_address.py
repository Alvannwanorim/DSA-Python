from typing import List


class Solution:
    def uniqueEmail(self, emails: List[str]) -> int:
        unique = set()

        for email in emails:
            local, domain = email.split("@")
            local = local.split("+")[0]
            local = local.replace(".", "")
            unique.add((local,domain))

        return len(unique)



class Solution2:
    def uniqueEmail(self, emails: List[str]) -> int:
        unique = set()

        for email in emails:
            i, local = 0, ""
            while email[i] not in ["@", "+"]:
                if email[i] != ".":
                    local += email[i]
                i += 1
            
            while email[i] != "@":
                i += 1
            
            domain = email[i + 1:]
            unique.add(local, domain)
        return len(unique)


sol = Solution()
print(sol.uniqueEmail(["test.email+alex@leetcode.com","test.e.mail+bob.cathy@leetcode.com","testemail+david@lee.tcode.com"]))