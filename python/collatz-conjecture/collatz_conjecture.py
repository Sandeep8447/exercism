steps = lambda x, s=0 : exec(f'raise ValueError(\'Value \\\'{x}\\\' is not a valid Collatz Sequence starting point.\')') if x < 1 else s if x == 1 else steps(x // 2, s+1) if x % 2 == 0 else steps((3 * x) + 1, s+1)