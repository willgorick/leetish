from typing import List
class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        emailSet = set()
        for email in emails:
            firstPart, secondPart = email.split("@")
            firstPart = firstPart.replace(".", "")
            firstPart = firstPart.split("+")[0]
            cleanedEmail = firstPart + "@" + secondPart
            if cleanedEmail not in emailSet:
                emailSet.add(cleanedEmail)
        return len(emailSet)

def main():
  sol = Solution()
  print(sol.numUniqueEmails(["a@leetcode.com","b@leetcode.com","c@leetcode.com"]))
  
main()