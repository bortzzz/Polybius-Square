def solution(text):
    dicts = {
        #! Letters
        "a": "11",
        "b": "12",
        "c": "13",
        "d": "14",
        "e": "15",
        "f": "21",
        "g": "22",
        "h": "23",
        "i": "24",
        "j": "24",
        "k": "25",
        "l": "31",
        "m": "32",
        "n": "33",
        "o": "34",
        "p": "35",
        "q": "41",
        "r": "42",
        "s": "43",
        "t": "44",
        "u": "45",
        "v": "51",
        "w": "52",
        "x": "53",
        "y": "54",
        "z": "55",
        #! Numbers
        11: "a",
        12: "b",
        13: "c",
        14: "d",
        15: "e",
        21: "f",
        22: "g",
        23: "h",
        24: "i",
        24: "j",
        25: "k",
        31: "l",
        32: "m",
        33: "n",
        34: "o",
        35: "p",
        41: "q",
        42: "r",
        43: "s",
        44: "t",
        45: "u",
        51: "v",
        52: "w",
        53: "x",
        54: "y",
        55: "z",
        #! Space
        99: " ",
        " ": " ",
    }
    word = ""
    a = 2
    space = " "
    for x in text:
        if x.isdigit():
            if space in text:
                stripTXT = text.replace(" ", "99")
                list1 = [stripTXT[i : i + a] for i in range(0, len(stripTXT), a)]
                int_list = [int(i) for i in list1]
                strs_list = [dicts[w] for w in int_list]
                completed_str = word.join(strs_list)
                return completed_str
            if len(text) >= 3:
                list1 = [text[i : i + a] for i in range(0, len(text), a)]
                int_list = [int(i) for i in list1]
                strs_list = [dicts[w] for w in int_list]
                completed_str = word.join(strs_list)
                return completed_str
            else:
                textint = int(text)
                word += dicts[textint]
                return word
        else:
            word += dicts[x.lower()]
    return word


print(solution("Hello World"))
print(solution("2315313134 5234423114"))
