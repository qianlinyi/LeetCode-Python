from collections import defaultdict


class Solution:
    def mostPopularCreator(self, creators: List[str], ids: List[str], views: List[int]) -> List[List[str]]:
        cnt = defaultdict(int)
        mp = defaultdict(int)
        videos = defaultdict(list)
        n = len(creators)
        mx = -1
        ans = []
        for i in range(n):
            cnt[creators[i]] += views[i]
            mx = max(mx, cnt[creators[i]])
            videos[creators[i]].append(ids[i])
            mp[(creators[i], ids[i])] += views[i]
        for k, v in cnt.items():
            if mx == v:
                num = -1
                id = ''
                for video in videos[k]:
                    if mp[(k, video)] > num:
                        num = mp[(k, video)]
                        id = video
                    elif mp[(k, video)] == num:
                        if video < id:
                            id = video
                ans.append([k, id])
        return ans
