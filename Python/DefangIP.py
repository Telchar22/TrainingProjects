#change . to [.]
class Solution:
    def defangIPaddr(self, address: str) -> str:
        ads_list = list(address) 
        ads_list = ["[.]" if (ads_list[i]== ".") else ads_list[i] for i in range(len(ads_list))]
        address = "".join(ads_list)
        return address

ads = "255.255.255.255"
p = Solution()
print(p.defangIPaddr(ads))
