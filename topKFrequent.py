def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        num_counts = {}

        for num in nums:
            if num in num_counts:
                num_counts[num] += 1
            else:
                num_counts[num] = 1

        sorted_counts = sorted(num_counts.items(), key=lambda item: item[1], reverse=True)

        top_k_frequent = []
        for i in range(min(k, len(sorted_counts))): 
            top_k_frequent.append(sorted_counts[i][0]) 
        
        return top_k_frequent
