from agent import agent

print("Agent started. Type 'exit' to quit.")

while True:
    q = input("> ")
    if q=="exit":
        break
    print(agent(q))
