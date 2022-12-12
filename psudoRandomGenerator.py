from hashlib import blake2s
import codecs

class prg:

    def f(self, inp):

        converted = inp[0:int(len(inp)/4)]+ inp[int(len(inp)/2): int(3*len(inp)/4)] + inp[int(len(inp)/4): int(len(inp)/2)] + inp[int(3*len(inp)/4) :]
        return converted


    def g(self, inp):

        return blake2s(codecs.decode(inp, "hex_codec")).hexdigest()

    

    def __init__(self, seed) -> None:
        self.__seed = blake2s(seed.encode()).hexdigest();
        self.__currentHash = self.g(self.f(self.__seed))

    
    def random(self):
        self.__currentHash = self.g(self.f(self.__currentHash))
        return self.__currentHash


c = prg(seed="")

out = ""

for i in range(100000):
    out = str(bin(int(c.random(), 16)))[2:] + "\n" + out


f = open("ranodm.txt", "w")
f.write(out)