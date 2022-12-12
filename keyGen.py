from hashlib import blake2s
import codecs

def init(inp):
    return blake2s(inp.encode()).hexdigest();


def f(inp):

    converted = [inp[0:int(len(inp)/4)]+ inp[int(len(inp)/2): int(3*len(inp)/4)], inp[int(len(inp)/4): int(len(inp)/2)]+ inp[int(3*len(inp)/4) : ]]
    
    return converted


def g(inp):

    return [blake2s(codecs.decode(inp[0] + inp[1], "hex_codec")).hexdigest(), blake2s(codecs.decode(inp[1], "hex_codec")).hexdigest()]


def keyGen(seed):
    initialise = init(seed)

    r1 = g(f(initialise))

    r2_0 = g(f(r1[0]))
    r2_1 = g(f(r1[1]))

    r2 = [r2_0[0], r2_0[1], r2_1[0], r2_1[1]]


    r3_0 = g(f(r2[0]))
    r3_1 = g(f(r2[1]))
    r3_2 = g(f(r2[2]))
    r3_3 = g(f(r2[3]))

    r3 = [r3_0[0], r3_0[1], r3_1[0], r3_1[1], r3_2[0], r3_2[1], r3_3[0], r3_3[1]]
    

    r4_0 = g(f(r3[0]))
    r4_1 = g(f(r3[1]))
    r4_2 = g(f(r3[2]))
    r4_3 = g(f(r3[3]))
    r4_4 = g(f(r3[4]))
    r4_5 = g(f(r3[5]))
    r4_6 = g(f(r3[6]))
    r4_7 = g(f(r3[7]))

    r4 = [r4_0[0], r4_0[1], r4_1[0], r4_1[1], r4_2[0], r4_2[1], r4_3[0], r4_3[1], r4_4[0], r4_4[1], r4_5[0], r4_5[1], r4_6[0], r4_6[1], r4_7[0], r4_7[1]]
    output = "".join(r4)
    r4_5 = g(f(r3[5]))
    r4_6 = g(f(r3[6]))
    r4_7 = g(f(r3[7]))

    r4 = [r4_0[0], r4_0[1], r4_1[0], r4_1[1], r4_2[0], r4_2[1], r4_3[0], r4_3[1], r4_4[0], r4_4[1], r4_5[0], r4_5[1], r4_6[0], r4_6[1], r4_7[0], r4_7[1]]
    output = "".join(r4)
    return output

