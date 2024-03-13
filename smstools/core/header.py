
class Header:

    def __init__(self, rom_data):
        self._rom_data = rom_data

    def get_field(self, offset, length):
        value = self._rom_data[offset:offset + length]

        return value

    def get_ptr_field(self, offset):
        field = []

        for byte in self._rom_data[offset:]:
            if not byte:
                break

            field.append(chr(byte))

        return ''.join(field)