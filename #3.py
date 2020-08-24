def swap_case(s):
    netice=""
    for _s in s:
        if _s.upper()==_s:
            netice+=_s.lower()
        else:
            netice+=_s.upper()
    return netice

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)