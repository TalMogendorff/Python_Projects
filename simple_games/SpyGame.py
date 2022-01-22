def spy_game(nums):
    code = [0,0,7,'x']
    for num in nums:
        if num == code[0]:
            code.pop(0)
    return len(code) == 1