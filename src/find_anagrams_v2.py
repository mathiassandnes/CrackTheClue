from src.shift_letters import ceasar_cipher

with open('data/osrs_words.txt', 'r') as f:
    raws = f.read().splitlines()

with open('data/osrs_words_short.txt', 'r') as f:
    shorts = f.read().splitlines()


def is_anagram(anagram, candidate):
    if len(anagram) == 0 or len(anagram) < len(candidate):
        return
    remainder = anagram
    for letter in candidate:
        if letter in remainder:
            remainder = remainder.replace(letter, '', 1)
        else:
            return False
    return True


def remove_letters(text, letters):
    for letter in letters:
        text = text.replace(letter, '', 1)
    return text


def find_anagrams(text_):
    anagrams = []
    for (raw1, short1) in zip(raws, shorts):
        text = text_
        if is_anagram(text, short1):
            anagrams.append(raw1)
            text = remove_letters(text, short1)
            for (raw2, short2) in zip(raws, shorts):
                if is_anagram(text, short2):
                    text = remove_letters(text, short2)
                    anagrams.append([raw1, raw2])
                    for (raw3, short3) in zip(raws, shorts):
                        if is_anagram(text, short3):
                            text = remove_letters(text, short3)
                            anagrams.append([raw1, raw2, raw3])
                            for (raw4, short4) in zip(raws, shorts):
                                if is_anagram(text, short3):
                                    text = remove_letters(text, short4)
                                    anagrams.append([raw1, raw2, raw3, raw4])
                                    for (raw5, short5) in zip(raws, shorts):
                                        if is_anagram(text, short5):
                                            text = remove_letters(text, short5)
                                            anagrams.append([raw1, raw2, raw3, raw4, raw5])
                                            for (raw6, short6) in zip(raws, shorts):
                                                if is_anagram(text, short6):
                                                    text = remove_letters(text, short6)
                                                    anagrams.append([raw1, raw2, raw3, raw4, raw5, raw6])

    return anagrams


if __name__ == '__main__':

    clue = [
        ['YPWAIETOAENRMHMGEN', 'MIVWDMKDTCBANGBFKW'],
        ['NQLLWQMIRLVFSDROTN', 'VKIIAAKIRLHADHESVG'],
        ['LINVADMCURYBOFEUAI', 'DRULRHTDEESEBREPYE'],
        ['VRBOOHHSDEWEAANANN', 'EERATOLITEJEPEPZFN'],
        ['ANHIITBICPATELTTMH', 'FEKETCHPMSNAFEWNQM'],
        ['SFTOAINWLXARKLANFE', 'NEWEDSANENTEGQLHUA'],
        ['OENIRSRONOFKGVEKAR', 'TLBGONGUWHILPAFNAS'],
        ['EHERESSOVEMDGJTCWS', 'RDMCORRODAPJNLSAWY'],
        ['TASEWNHEVGRANOKNOT', 'SHTOELHTICUTMLHOIO'],
        ['HRFRONLRATTATTIQAT', 'ANEUOASGNHSFALEHND']
    ]

    to_remove_list = ['Pig', 'Engineer']
    for i, row in enumerate(clue):
        for value in row:
            # value = ''.join(row)
            value = value.lower()
            anagrams_ = find_anagrams(value)
            anagrams_ = [anagram for anagram in anagrams_ if not any(word in anagram for word in to_remove_list)]

            print(value, len(anagrams_))
            for anagram in anagrams_:
                print(anagram)
            break
        break
#
# text = '''YPWAIETOAENRMHMGENMIVWDMKDTCBANGBFKWNQLLWQMIRLVFSDROTNVKIIAAKIRLHADHESVGLINVADMCURYBOFEUAIDRULRHTDEESEBREPYEVRBOOHHSDEWEAANANNEERATOLITEJEPEPZFNANHIITBICPATELTTMHFEKETCHPMSNAFEWNQMSFTOAINWLXARKLANFENEWEDSANENTEGQLHUAOENIRSRONOFKGVEKARTLBGONGUWHILPAFNASEHERESSOVEMDGJTCWSRDMCORRODAPJNLSAWYTASEWNHEVGRANOKNOTSHTOELHTICUTMLHOIOHRFRONLRATTATTIQATANEUOASGNHSFALEHND'''
#
#
#

# start = 0
# end = start + 0
#
# # text = 'AAKIRLHADHESVGLINVADMCURYBOFEUAIDRULRHTDEESEBREPYEVRBOOHHSDEWEAANANNEERATOLITEJEPEPZFNANH'
#
# '''
# nuxzddeeel - needle
# '''
#
# hticutmlhoiohrfronlrattattiqataneuoasgnhsfalehnd
# guhdvulminjpgqgspmmqzuszsshpbsbmdtpbthoirgzkfioe
# fvgewvknjmkqfphtqlnpyvryrrgocrclcsqcuipjqhyjgjpf
# ewffxwjokllreoiurkooxwqxqqfndqdkbrrdvjqkpixihkqg
# dxegyxiplkmsdnjvsjpnwxpwppemepejaqsewkrlojwhilrh
# cydhzyhqmjntcmkwtiqmvyovoodlfofizptfxlsmnkvgjmsi
# bzciazgrnioubllxuhrluznunnckgnghyougymtnmlufkntj
# aabjbafsohpvakmyvgsktamtmmbjhmhgxnvhznuolmtelouk
# zbakcbetpgqwzjnzwftjsblsllaiilifwmwiaovpknsdmpvl
# yczldcduqfrxyioaxeuirckrkkzhjkjevlxjbpwqjorcnqwm
# xdymedcvresyxhpbydvhqdjqjjygkjkdukykcqxripqborxn
# wexnfebwsdtzwgqczcwgpeipiixflilctjzldryshqpapsyo
# vfwogfaxtcuavfrdabxfofhohhwemhmbsiamesztgrozqtzp
# ugvphgzyubvbuesebayenggnggvdngnarhbnftaufsnyruaq
# thuqihyzvawctdtfczzdmhfmffucofozqgcogubvetmxsvbr
# sitrjixawzxdscugdyaclieleetbpepypfdphvcwdulwtwcs
# rjsskjwbxyyerbvhexbbkjdkddsaqdqxoeeqiwdxcvkvuxdt
# qkrtlkvcyxzfqawifwcajkcjccrzrcrwndfrjxeybwjuvyeu
# plqumludzwagpzxjgvdzilbibbqysbsvmcgskyfzaxitwzfv
# ompvnmteavbhoyykhueyhmahaapxtatulbhtlzgazyhsxagw
# nnowonsfbucinxzlitfxgnzgzzowuzutkaiumahbyzgrybhx
# monxporgctdjmwamjsgwfoyfyynvvyvsjzjvnbicxafqzciy
# lpmyqpqhdseklvbnkrhvepxexxmuwxwriykwocjdwbepadjz
# kqlzrqpierflkucolqiudqwdwwltxwxqhxlxpdkevcdobeka
# jrkasrojfqgmjtdpmpjtcrvcvvksyvypgwmyqelfudcncflb
# isjbtsnkgphniseqnoksbsubuujrzuzofvnzrfmgtebmdgmc


# text = 'hticutmlhoiohrfronlrattattiqataneuoasgnhsfalehnd'
# text = text.lower()
#
# # text = remove_letters(text, 'Woodenshield al kharid anvil jeed pvp arena body rune fire rune beer glass')
# print('letters left: ', len(text))
#
# text = ''.join(sorted(text))
# anagrams = find_anagrams(text)
#
# print(len(anagrams))
# print(text, anagrams)
