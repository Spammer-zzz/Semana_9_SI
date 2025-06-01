import asyncio
from agent.agent import root_agent

async def main():
    question = "Double check this: Earth is further away from the Sun than Mars."
    response = await root_agent.run(question)
    print("\n🧠 RESPUESTA DEL AGENTE:\n")
    print(response)

if __name__ == "__main__":
    asyncio.run(main())
