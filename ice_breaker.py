from langchain.prompts import PromptTemplate

# from langchain.chat_models import ChatOpenAI
from langchain_community.chat_models import ChatOpenAI
from langchain.chains import LLMChain
from third_parties.linkedin import scrape_linkedin_profile
from agents.linkedin_lookup_agent import lookup as linkedin_lookup_agent

information = """
Juhi Chawla (born 13 November 1967) is an Indian actress and beauty pageant titleholder. She established herself as one of the leading actresses of Hindi cinema from the late 1980s through the early 2000s.[1] Recognised for her comic timing and vivacious on-screen persona, she is the recipient of several accolades, including two Filmfare Awards.[2]

After winning the 1984 Miss India beauty pageant, Chawla made her acting debut with a brief appearance in the film Sultanat (1986), and had her breakthrough role in the tragic romance film Qayamat Se Qayamat Tak (1988), which earned her the Filmfare Award for Best Female Debut. The year 1993 was key in her career, as she gained recognition for her starring roles in Lootere, Aaina, Darr, and Hum Hain Rahi Pyar Ke, winning the Filmfare Award for Best Actress for the lattermost.[2] Further success came in 1997 with Deewana Mastana, Yes Boss, and Ishq.[2][3]

In the following decade, Chawla began playing against type in art-house projects, garnering critical acclaim for her performances in Jhankaar Beats (2003), 3 Deewarein (2003), My Brother Nikhil (2005), I Am (2011) and Gulaab Gang (2014). She also starred in several Punjabi films, including the biopics Shaheed Udham Singh (2000), Des Hoyaa Pardes (2004), Waris Shah: Ishq Daa Waaris (2006) and Sukhmani – Hope for Life (2010). Among her television work, she was a talent judge on the third season of the dance reality show Jhalak Dikhhla Jaa (2009) and had supporting roles in the streaming series Hush Hush (2022) and The Railway Men (2023).

Chawla has been married to industrialist Jay Mehta since 1995, with whom she has two children. Along with her husband and Shah Rukh Khan, she is the co-owner of the Indian Premier League cricket team Kolkata Knight Riders. Along with Khan, she co-founded the production company Dreamz Unlimited, which produced three films, beginning with their self-starring Phir Bhi Dil Hai Hindustani (2000).
"""


if __name__ == "__main__":
    print("Hello LangChain")

    linkedin_profile_url = linkedin_lookup_agent(name="Eden Marco Udemy")

    summary_template = """
        given the LinkedIn information {information} about a person from I want you to create:
        1. a short summary
        2. two interesting facts about them
    """

    summary_prompt_template = PromptTemplate(
        input_variables=["information"], template=summary_template
    )

    llm = ChatOpenAI(temperature=0, model_name="gpt-3.5-turbo")

    chain = LLMChain(llm=llm, prompt=summary_prompt_template)

    linkedin_data = scrape_linkedin_profile(linkedin_profile_url=linkedin_profile_url)
    # print(linkedin_data)
    print(chain.run(information=linkedin_data))
