from unittest import TestCase, main
from archiver import Archive


class ArchiveTest(TestCase):
    def pack_by_lsw_into_return_result(self):
        self.assertEqual(Archive.pack_by_lzw(b'Some text\n'), b' e\nmoStx$\x05\x04\x03\x01\x00\x06\x01\x07\x06\x02')

    def unpack_by_lzw_return_result(self):
        self.assertEqual(Archive.unpack_by_lzw(b' e\nmoStx$\x05\x04\x03\x01\x00\x06\x01\x07\x06\x02'), b'Some text\n')


if __name__ == "__main__":
    main()
