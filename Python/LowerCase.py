def toLowerCase(a: str) -> str:
    nums = list(a)
    nums = [chr(ord(i)+32) if 65 <= ord(i) <= 90 else i for i in nums]
    return "".join(nums)

a = "AAAaaaAaa&&&&"
print(toLowerCase(a))
