import re
class suffixarray(object):
    def __init__(self, instr):
        self.instr = instr
        sfx = []
        for i in range(0, len(instr)):
            sfx.append((self.instr[i:], i))

        self.sarray = sorted(sfx)

    def search(self,what):
        low = 0
        high = len(self.sarray)
        while low < high:
            mid = (high - low)// 2 + low
            mid_val, starts_at = self.sarray[mid]

            if mid_val == what:
                return mid, starts_at
            elif mid_val > what:
                high = mid
            elif mid_val < what:
                low = mid+1

        return -1, -1

    def getallsuffix(self):
        return self.sarray
    def find_shortest(self,match):
        suffixs_i, instr_i = self.search(match)
        return instr_i

    def find_longest(self, match):
        pass

inputstr = "sadhjagsfky"
suffixlist = suffixarray(inputstr)
print(suffixlist.getallsuffix())
print(suffixlist.find_shortest("ky"))

