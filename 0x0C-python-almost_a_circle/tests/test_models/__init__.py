class Counts:
    base_count = 0
    rect_count = 0
    square_count = 0

    @classmethod
    def print_counts(cls):
        s = f"Counts: Base = {cls.base_count}, Rectangle = {cls.rect_count}, "
        s += f"Square = {cls.square_count}"
        print(s)

    @classmethod
    def init_rect_count(cls):
        """Sync the Rectangle objects count"""
        if not cls.rect_count and cls.base_count:
            cls.rect_count = cls.base_count
        pass

    @classmethod
    def init_square_count(cls):
        """Sync the Square objects count"""
        if not cls.square_count and cls.rect_count:
            cls.square_count = cls.rect_count
        pass
