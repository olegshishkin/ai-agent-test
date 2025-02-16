from langgraph.prebuilt import create_react_agent

from agent.llm import llm
from agent.tools import tools

prompt = "Ты полезный бот для расчета количества слонов в помещении. Один слон занимает площадь 2 квадратных метра."

agent = create_react_agent(model=llm, tools=tools, prompt=prompt)
