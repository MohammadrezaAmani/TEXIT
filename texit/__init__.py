from texit.base import Base, BaseElement, BaseVoidElement


class startex:
    def __init__(self, *data) -> None:
        self.data = data

    def __str__(self) -> str:
        text = ""
        for i in self.data:
            text += str(i) + "\n"

        return text

    def __repr__(self) -> str:
        return self.__str__()

    def render(self) -> str:
        return self.__str__()


__all__ = ["Base", "BaseElement", "BaseVoidElement", "startex"]
