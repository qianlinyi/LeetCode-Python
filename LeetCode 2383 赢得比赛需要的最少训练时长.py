class Solution:
    def minNumberOfHours(self, initialEnergy: int, initialExperience: int, energy: List[int],
                         experience: List[int]) -> int:
        n = len(energy)
        ans = 0
        ene, exp = initialEnergy, initialExperience
        for i in range(n):
            if ene >= energy[i] + 1:
                ene -= energy[i]
            else:
                ans += energy[i] + 1 - ene
                ene = 1
            if exp >= experience[i] + 1:
                exp += experience[i]
            else:
                ans += experience[i] + 1 - exp
                exp = experience[i] + 1 + experience[i]
        return ans
