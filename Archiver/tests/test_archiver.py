from archiver import Archive
from unittest import TestCase, main
import os


class ArchiveTest(TestCase):
    def pack_file_on_create_file(self):
        Archive.pack_file('File.txt', 'File1.bin')
        self.assertTrue(os.path.isfile('File1.bin'))

    def unpack_file_on_create_file(self):
        Archive.unpack_file('File1.bin', 'File2.txt')
        self.assertTrue(os.path.isfile('File2.txt'))

    def pack_by_lsw_into_return_result(self):
        self.assertEqual(Archive.pack_by_lzw(b'Some text\n'), b' e\nmoStx$\x05\x04\x03\x01\x00\x06\x01\x07\x06\x02')

    def unpack_by_lzw_return_result(self):
        self.assertEqual(Archive.unpack_by_lzw(b' e\nmoStx$\x05\x04\x03\x01\x00\x06\x01\x07\x06\x02'), b'Some text\n')


if __name__ == "__main__":
    main()
