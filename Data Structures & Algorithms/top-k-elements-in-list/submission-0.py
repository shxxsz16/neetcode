class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        Kfreq = defaultdict(int)
        for i in range(len(nums)):
            Kfreq[nums[i]] += 1

        TopK = []

        for j in range(k):
            TopK.append(max(Kfreq, key=Kfreq.get))
            Kfreq[max(Kfreq, key=Kfreq.get) ] = 0

        return TopK
        