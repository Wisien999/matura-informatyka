with open("dane.txt") as f:
    darkest = 256
    brightest = 0
    for line in f.readlines():
        nums = list(map(int, line.split()))
        d_candidates = nums.copy()
        b_candidates = nums.copy()
        d_candidates.append(darkest)
        b_candidates.append(brightest)
        darkest = min(d_candidates)
        brightest = max(b_candidates)

print("Najjaśniejszy:", brightest)
print("Najciemniejszy:", darkest)
        
