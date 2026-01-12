import openai
from memory import retrieve, store_memory

def agent(prompt):
    memories = retrieve(prompt)

    context = "\n".join(memories)
    final_prompt = f"""
You are a personalized AI assistant.

Relevant memory:
{context}

User: {prompt}
"""

    res = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[{"role":"user","content":final_prompt}]
    )

    reply = res["choices"][0]["message"]["content"]

    store_memory("User: "+prompt)
    store_memory("Assistant: "+reply)

    return reply
