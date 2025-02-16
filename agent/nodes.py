from langchain_core.messages import HumanMessage
from langchain_core.prompts import PromptTemplate

from agent.llm import llm
from agent.state import State

CLASSIFICATION_NODE_NAME = "classification"
EXTRACTION_NODE_NAME = "extraction"
SUMMARIZATION_NODE_NAME = "summarization"


def classify(state: State):
    """ Классифицируй текст по одной из категорий: Новости, Блог, Исследования или Другое """

    prompt = PromptTemplate(
            input_variables=["text"],
            template="Отнеси следующий текст к одной из категорий: Новости, Блог, Исследования или Другое.\n\Текст:{text}\n\Категория:"
    )
    message = HumanMessage(content=prompt.format(text=state["text"]))
    kind = llm.invoke([message]).content.strip()
    return {"kind": kind}


def extract(state: State):
    """ Извлеки все объекты (Человек, Организация, Местоположение) из текста """

    prompt = PromptTemplate(
            input_variables=["text"],
            template="Извлеки все объекты (Человек, Организация, Местоположение) из следующего текста. Укажи результат в виде списка, разделенного запятыми. Перечисли только сами объекты, не указывай типы, не повторяй объекты\n\Текст:{text}\n\Объекты:"
    )
    message = HumanMessage(content=prompt.format(text=state["text"]))
    entities = llm.invoke([message]).content.strip().split(", ")
    return {"entities": entities}


def summarize(state: State):
    """ Резюме текста в одном коротком предложении """

    prompt = PromptTemplate(
            input_variables=["text"],
            template="Резюмируй следующий текст в одном коротком предложении.\n\Текст:{text}\n\Резюме:"
    )
    message = HumanMessage(content=prompt.format(text=state["text"]))
    summary = llm.invoke([message]).content.strip()
    return {"summary": summary}
