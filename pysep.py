#!/usr/bin/python3
import sys

def sepdump_info(sepdumpid: int, start: int, end: int) -> dict:
    img_info = dict()
    img_info['name'] = "sepdump_{:02d}".format(sepdumpid)
    img_info['start'] = start
    img_info['end'] = end
    img_info['size'] = end - start + 1
    return img_info


def sepsplit(sep, sepinfo: dict):
    sep.seek(sepinfo['start'])
    sepdata = sep.read(sepinfo['size'])
    open(sepinfo['name'], 'wb').write(sepdata)


def usage():
    print("usage : {} <sep-firmware>".format(sys.argv[0]))


def main():
    if len(sys.argv) != 2:
        usage()
        return 1

    sep = open(sys.argv[1], mode='rb')
    seplen = len(sep.read())
    sepdumpid, start, end = 0, 0, 0
    sepdump = dict()

    for offset in range(0, seplen, 4):
        sep_data = sep.read(4)

        if sep_data == b'\xcf\xfa\xed\xfe':
            print("found macho @ {}".format(hex(offset)))
            sepdump[sepdumpid] = sepdump_info(sepdumpid, start, offset)
            sepdumpid += 1
            start = offset

        offset += 4
        sep.seek(offset)

    for i in sepdump:
        sepsplit(sep, sepdump[i])
 
    sep.close()
        

if __name__ == '__main__':
    sys.exit(main())
