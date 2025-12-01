class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        
        if len(s1) > len(s2):
            return False

        C1 = Counter(s1)
        C2 = Counter()

        left = 0

        for right in range(len(s1)):
            C2[s2[right]] += 1

            if C1 == C2:
                return True

        for right in range(len(s1), len(s2)):

            C2[s2[right]] += 1
            C2[s2[left]] -= 1
            left += 1

            if C1 == C2:
                return  True

        return False


