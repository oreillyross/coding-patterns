def isPalindrome(s: str) -> bool:
	l,r = 0, len(s) - 1
	while (l < r):
		if(s[l] != s[r]): return False
		l = l + 1
		r = r - 1
	return True

res = isPalindrome("cacac")

print(res)