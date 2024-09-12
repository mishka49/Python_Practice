from os import path


class Archive:
    @staticmethod
    def pack_file(path_to_file: str, path_to_archived_file: str) -> None:
        if not path_to_archived_file:
            path_to_archived_file = path.splitext(path.basename(path_to_file))[0] + '.bin'

        with open(path_to_file, 'rb') as file_txt, open(path_to_archived_file,
                                                        'wb') as file_bin:
            file_bin.write(Archive.pack_by_lzw(file_txt.read()))

    # The method converts the input string of bytes by encoding according to the Lempel-Ziv-Welch, LZW algorithm
    @staticmethod
    def pack_by_lzw(string_bytes: bytes) -> bytes:
        codes_list = [item.to_bytes(1, 'big') for item in
                      set(string_bytes)]  # list with substrings, the codes for them are the position number in the list
        index = 0
        encode_result = bytes([int.from_bytes(item, 'big') for item in codes_list]) + '$$'.encode(
            'utf-8')  # list of all unique values + delimiter symbols

        while index < len(string_bytes):
            substring = string_bytes[index].to_bytes(1, 'big')
            while index + 1 < len(string_bytes):
                print('pack_index', index)
                next_substring = string_bytes[index + 1].to_bytes(1, 'big')
                if codes_list.count(substring + next_substring) == 0:
                    codes_list.append(substring + next_substring)
                    encode_result += codes_list.index(substring).to_bytes(
                        Archive.set_quantity_of_bytes(len(codes_list)),
                        'big')
                    break

                substring += next_substring
                index += 1

            index += 1

        return encode_result + codes_list.index(substring).to_bytes(Archive.set_quantity_of_bytes(len(codes_list)),
                                                                    'big')

    # determines the number of bytes to write a number
    @staticmethod
    def set_quantity_of_bytes(number: int) -> int:
        quantity_of_bytes = 1

        while number > 255 ** quantity_of_bytes:
            quantity_of_bytes += 1

        return quantity_of_bytes

    @staticmethod
    def unpack_file(path_to_pack_file: str, path_to_unpack_file: str) -> None:
        with open(path_to_pack_file, 'rb') as file_bin, open(path_to_unpack_file, 'ab') as file_txt:
            file_txt.write(Archive.unpack_by_lzw(file_bin.read()))

    #   decodes the input string of bytes using the Lempel-Ziv-Welch algorithm, LZW algorithm
    @staticmethod
    def unpack_by_lzw(file_content: bytes) -> bytes:
        codes_list = []  # list with substrings, the codes for them are the position number in the list
        index = int()

        for file_index, byte in enumerate(file_content):

            if byte == 36 and file_content[file_index + 1] == 36:  # search delimiter symbols
                index = file_index + 1
                break

            codes_list.append(byte)

        decode_result = bytes()
        next_substring = bytes()
        quantity_of_substrings_bytes = 1

        while index + 2 < len(file_content):
            index += quantity_of_substrings_bytes

            quantity_of_substrings_bytes = Archive.set_quantity_of_bytes(len(codes_list) + 1)
            if isinstance(codes_list[int.from_bytes(file_content[index: index + quantity_of_substrings_bytes], 'big')],
                          int):
                substring = codes_list[
                    int.from_bytes(file_content[index: index + quantity_of_substrings_bytes], 'big')].to_bytes(1,
                                                                                                               'big')
            else:
                substring = codes_list[int.from_bytes(file_content[index: index + quantity_of_substrings_bytes], 'big')]

            quantity_of_next_bytes = Archive.set_quantity_of_bytes(len(codes_list) + 2)
            if int.from_bytes(file_content[
                              index + quantity_of_substrings_bytes: index + quantity_of_substrings_bytes + quantity_of_next_bytes],
                              'big') != len(codes_list):

                if isinstance(codes_list[int.from_bytes(file_content[
                                                        index + quantity_of_substrings_bytes: index + quantity_of_substrings_bytes + quantity_of_next_bytes],
                                                        'big')],
                              int):
                    next_substring = codes_list[
                        int.from_bytes(file_content[
                                       index + quantity_of_substrings_bytes: index + quantity_of_substrings_bytes + quantity_of_next_bytes],
                                       'big')].to_bytes(1, 'big')
                else:
                    next_substring = codes_list[
                        int.from_bytes(file_content[
                                       index + quantity_of_substrings_bytes: index + quantity_of_substrings_bytes + quantity_of_next_bytes],
                                       'big')]

            else:
                next_substring = substring

            codes_list.append(substring + next_substring[0].to_bytes(1, 'big'))
            decode_result += substring

        return decode_result + next_substring


if __name__ == "__main__":
    # Archive.pack_file("File.txt", '')
    # Archive.unpack_file("File.bin", "File1.txt")
    Archive.pack_file("archiver.py", '')
    Archive.unpack_file("archiver.bin", 'arhiver1.py')
