import sys
import unicodedata
from array import array

ALPHA = 1 << 0
DIGIT = 1 << 1
DECIMAL = 1 << 2
NUMERIC = 1 << 3
LETTER = 1 << 4
UPPER = 1 << 5
LOWER = 1 << 6


class UnicodeRecord:
    __slots__ = ("flags",)

    def __init__(self, flags=0):
        self.flags = flags

    @property
    def alpha(self):
        return bool(self.flags & ALPHA)

    @property
    def digit(self):
        return bool(self.flags & DIGIT)

class UnicodeDatabase:

    BLOCK_BITS = 8
    BLOCK_SIZE = 1 << BLOCK_BITS
    BLOCK_MASK = BLOCK_SIZE - 1

    MAX_UNICODE = 0x10FFFF

    def __init__(self):
        self.blocks = {}
        self._build()

    @staticmethod
    def _property_flags(ch):

        flags = 0

        category = unicodedata.category(ch)

        if category.startswith("L"):
            flags |= LETTER
            flags |= ALPHA

        if category == "Lu":
            flags |= UPPER

        if category == "Ll":
            flags |= LOWER

        try:
            unicodedata.digit(ch)
            flags |= DIGIT
        except (TypeError, ValueError):
            pass

        try:
            unicodedata.decimal(ch)
            flags |= DECIMAL
        except (TypeError, ValueError):
            pass

        try:
            unicodedata.numeric(ch)
            flags |= NUMERIC
        except (TypeError, ValueError):
            pass

        return flags

    def _build_block(self, block):

        start = block << self.BLOCK_BITS
        end = min(
            start + self.BLOCK_SIZE,
            self.MAX_UNICODE + 1
        )

        table = array("B", [0]) * (end - start)

        for codepoint in range(start, end):

            try:
                ch = chr(codepoint)
            except ValueError:
                continue

            flags = self._property_flags(ch)

            table[codepoint - start] = flags

        return table

    def _build(self):

        max_block = self.MAX_UNICODE >> self.BLOCK_BITS

        for block in range(max_block + 1):

            table = self._build_block(block)

            if any(table):
                self.blocks[block] = table

    def get_flags(self, codepoint):

        if not 0 <= codepoint <= self.MAX_UNICODE:
            raise ValueError("Invalid Unicode code point")

        block = codepoint >> self.BLOCK_BITS
        offset = codepoint & self.BLOCK_MASK

        table = self.blocks.get(block)

        if table is None:
            return 0

        return table[offset]


class UnicodeCharacter:

    __slots__ = ("database",)

    def __init__(self, database):
        self.database = database

    def flags(self, ch):

        if len(ch) != 1:
            raise ValueError("Expected one Unicode character")

        return self.database.get_flags(ord(ch))

    def is_alpha(self, ch):

        return bool(
            self.flags(ch) & ALPHA
        )

    def is_digit(self, ch):

        return bool(
            self.flags(ch) & DIGIT
        )


class UnicodeString:

    __slots__ = ("checker",)

    def __init__(self, checker):
        self.checker = checker

    def isalpha(self, s):

        if not s:
            return False

        for ch in s:

            if not self.checker.is_alpha(ch):
                return False

        return True

    def isdigit(self, s):

        if not s:
            return False

        for ch in s:

            if not self.checker.is_digit(ch):
                return False

        return True

    def password(self, s):

        if len(s) < 8:
            return False

        has_alpha = False
        has_digit = False

        for ch in s:

            flags = self.checker.flags(ch)

            if flags & ALPHA:
                has_alpha = True

            elif flags & DIGIT:
                has_digit = True

            else:
                return False

            if has_alpha and has_digit:
                pass

        return has_alpha and has_digit


database = UnicodeDatabase()

checker = UnicodeCharacter(database)

unicode_string = UnicodeString(checker)


p = input()

print(
    len(p) >= 8
    and unicode_string.password(p)
)