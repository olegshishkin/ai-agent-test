from agent.agent import agent

sample_text = """
У меня круглая комната радиусом 3 метра. Сколько в ней поместится слонов?
"""

result = agent.invoke({"messages": sample_text})

print(result)
