from abc import ABC, abstractmethod


class BaseAgent(ABC):
    SYSTEM_PROMPT = ""

    @abstractmethod
    def respond(self, query: str, context: list = []) -> str:
        pass
