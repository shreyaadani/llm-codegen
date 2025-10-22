def second_largest(nums):
    unique_nums = sorted(list(set(nums)), reverse=True)
    
    if len(unique_nums) < 2:
        # Or raise an error, but returning None/appropriate value for insufficient elements is common
        return None 
        
    return unique_nums[1]