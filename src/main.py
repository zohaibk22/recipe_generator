from dotenv import load_dotenv
import os
import streamlit as st
from langchain_openai import OpenAI
from langchain_core.prompts import PromptTemplate
# from langchain.chains import LLMChainv


API_KEY = os.environ.get("OPENAI_API_KEY")
def main():

    llm = OpenAI(openai_api_key=API_KEY, temperature=0.9)

    # Define prompt template
    prompt_template = PromptTemplate(
        template= "Give me am example of a meal that could be made using the following ingredients: {ingredients}",
        input_variables=["ingredients"]
    )

    gangster_template = """Re-Write the meials given below in the style of a 1920s New York Mafia gangster.
    
    Meals: {meals} 
    """

    gangster_template_prompt = PromptTemplate(template = gangster_template, 
                                              input_variables=["meals"])

    # Test the prompt template
    # template = prompt_template.format(ingredients="chicken, rice, broccoli")

    # print(template)

    # Create LLM Chain
    # meal_chain = LLMChain(llm=llm, prompt=prompt_template, verbose=True)


    # Create sequential chain using pipe operator
    # First chain: ingredients -> meal
    meal_chain = prompt_template | llm
    
    # Second chain: meal -> gangster style
    # Use a lambda to transform the output to the expected input format
    sequential_chain = (
        prompt_template 
        | llm 
        | (lambda output: {"meals": output})
        | gangster_template_prompt 
        | llm
    )

    st.title("Recipe Generator")
    user_prompt = st.text_input("Enter ingredients (comma separated):")

    if st.button("Generate Recipe") and user_prompt:
        with st.spinner("Generating recipe..."):
            # First chain generates meal, second chain transforms it to gangster style
            output = sequential_chain.invoke({"ingredients": user_prompt})
            st.write(output)

if __name__ == "__main__":
    load_dotenv()
    main()