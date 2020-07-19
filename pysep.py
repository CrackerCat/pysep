#!/usr/bin/python3
import sys


def sepdump_info(sepdumpid: int, start: int, end: int, applist: list) -> dict:
    img_info = dict()
    img_info['name'] = applist[sepdumpid]
    img_info['start'] = start
    img_info['end'] = end
    img_info['size'] = end - start + 1
    return img_info


def sepsplit(sep, sepinfo: dict):
    sep.seek(sepinfo['start'])
    sepdata = sep.read(sepinfo['size'])
    open("sepdump_" + sepinfo['name'], 'wb').write(sepdata)


def get_macho_names(sep, seplen) -> list:
    # find 'ffff ffff 0000 0000' right after this
    # there is the name of the macho
    name_list = ["boot", "kernel", "SEPOS"]
    char = None
    for offset in range(0, seplen, 8):
        flag = sep.read(8)

        # stop at the first mach-o
        if b'\xcf\xfa\xed\xfe' in flag:
            break

        if flag == b'\xff\xff\xff\xff\x00\x00\x00\x00':
            name = ""
            name_addr = offset + 8
            sep.seek(name_addr)
            char = sep.read(0)
            while char != b'\x20':
                char = sep.read(1)
                name_addr +=1
                name += char.decode('utf-8')
                sep.seek(name_addr)

            name_list.append(name.split(' ')[0])
        offset += 8
        sep.seek(offset)
    return name_list


def usage():
    print("usage : {} <sep-firmware>".format(sys.argv[0]))


def app_list_info(info: dict):
    for i in info:
        if i != "name":
            print("{} : {:<10}".format(i, hex(info[i])), end='   ')
        else:
            print("{} : {:<10}".format(i, info[i]), end='   ')
    print(end='\n')


def main():
    if len(sys.argv) != 2:
        usage()
        return 1

    sep = open(sys.argv[1], mode='rb')
    seplen = len(sep.read())
    sepdumpid, start = 0, 0
    sepdump = dict()

    macho_app_list = get_macho_names(sep, seplen)
    for offset in range(0, seplen, 4):
        sep_data = sep.read(4)

        if sep_data == b'\xcf\xfa\xed\xfe':
            sepdump[sepdumpid] = sepdump_info(sepdumpid, start, offset, macho_app_list)
            sepsplit(sep, sepdump[sepdumpid])
            app_list_info(sepdump[sepdumpid])
            sepdumpid += 1
            start = offset

        offset += 4
        sep.seek(offset)
    sep.close()


if __name__ == '__main__':
    sys.exit(main())
