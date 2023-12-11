def generate_lullaby(location, name, language):
    import os
    from secret_key import openai_key
    os.environ['OPENAI_API_KEY'] = openai_key

    from langchain.llms import OpenAI
    llm = OpenAI(temperature=0.6)

    story_template = """
    As a comic writer, tell me a short and simple lullaby about 100 words,
    a story based on the {location}
    and the main character is {name}
    STORY:
    """
    from langchain.prompts import PromptTemplate
    story_prompt = PromptTemplate(
        input_variables=["location", "name"],
        template=story_template
    )

    from langchain.chains import LLMChain
    chain_story = LLMChain(
        llm=llm, 
        prompt=story_prompt,
        output_key="story"
    )

    translate_template = """
    Translate the {story} into {language}.
    Make sure the language is simple and fun.
    TRANSLATION:
    """
    from langchain.prompts import PromptTemplate
    translate_prompt = PromptTemplate(
        input_variables=["story", "language"],
        template=translate_template
    )

    chain_translate = LLMChain(
        llm=llm, 
        prompt=translate_prompt, 
        output_key="translated_story"
    )

    from langchain.chains import SequentialChain
    chain_seq = SequentialChain(
        chains=[chain_story, chain_translate],
        input_variables=["location", "name", "language"],
        output_variables=["story", "translated_story"]
    )

    response = chain_seq({
        "location" : location,
        "name" : name,
        "language" : language
    })

    return response

    # print(f"English version ==> {response['story']}\n\n")
    # print(f"Italian version ==> {response['translated_story']}")