from os import path


class Archive:
    @staticmethod
    def pack_file(path_to_file: str) -> None:
        with open(path_to_file, 'r') as file_txt, open(path.splitext(path.basename(path_to_file))[0] + '.bin',
                                                       'wb') as file_bin:
            file_bin.write(Archive.pack_by_lzw(file_txt.read().encode('utf-8')))

    @staticmethod
    def pack_by_lzw(list_bytes: bytes()) -> bytes():
        codes_list = [item.to_bytes(1, 'big') for item in set(list_bytes)]
        index = 0
        encode_result = bytes(''.join(map(lambda item: item.decode(), codes_list)), encoding='utf-8') + '$'.encode(
            'utf-8')

        while index < len(list_bytes):
            substring = list_bytes[index].to_bytes(1, 'big')
            try:
                while True:
                    print(codes_list)

                    if codes_list.count(substring + list_bytes[index + 1].to_bytes(1, 'big')) == 0:
                        codes_list.append(substring + list_bytes[index + 1].to_bytes(1, 'big'))
                        encode_result += codes_list.index(substring).to_bytes(1, 'big')
                        break

                    index += 1
                    substring += list_bytes[index].to_bytes(1, 'big')

                index += 1
            except IndexError:
                return encode_result + codes_list.index(substring).to_bytes(1, 'big')

    @staticmethod
    def unpack_file(pack_file: str, unpack_file: str) -> None:
        with open(pack_file, 'rb') as file_bin, open(unpack_file, 'a') as file_txt:
            file_txt.write(Archive.unpack_by_lzw(file_bin.read()).decode())

    @staticmethod
    def unpack_by_lzw(file_content: bytes) -> bytes:
        code_list = []
        index = int()

        for byte in enumerate(file_content):

            if byte[1] == 36:
                index = byte[0]
                break

            code_list.append(byte[1])

            decode_result = bytes()
            next_substring = bytes()

        while index + 2 < len(file_content):
            index += 1

            if isinstance(code_list[file_content[index]], int):
                substring = code_list[file_content[index]].to_bytes(1, 'big')
            else:
                substring = code_list[file_content[index]]

            if file_content[index + 1] != len(code_list):

                if isinstance(code_list[file_content[index + 1]], int):
                    next_substring = code_list[file_content[index + 1]].to_bytes(1, 'big')
                else:
                    next_substring = code_list[file_content[index + 1]][0].to_bytes(1, 'big')

            else:
                next_substring = substring

            code_list.append(substring + next_substring)
            decode_result += substring

        return decode_result + next_substring


if __name__ == "__main__":
    Archive.pack_file("File.txt")
    Archive.unpack_file("archFile.bin", "File1.txt")
