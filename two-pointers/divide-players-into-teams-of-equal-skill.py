class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        
        skill.sort()

        left = 0 
        right = len(skill) - 1

        pair = skill[left] + skill[right]
        chemistry = 0

        while left < right:
            if pair != skill[left] + skill[right]:
                return -1

            else:
                chemistry += skill[left] * skill[right]
                left += 1
                right -= 1

        return chemistry

