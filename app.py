import streamlit as st
import openai, os
st.title("Text Summarizer")

openai.api_key = os.getenv('OPENAI_KEY')

# initialize state variable 
if "summary" not in st.session_state:
  st.session_state["summary"] = ""

input_text = st.text_area(label='Enter Full text:', value="", height=300)


def summarize(prompt):
    augmented_prompt = f"summarize this text: {prompt}"
    try:
        st.session_state["summary"] = openai.Completion.create(
            model="text-davinci-003",
            prompt=augmented_prompt,
            temperature=.5,
            max_tokens=1000,
        )["choices"][0]["text"]
    except:
        st.write('There was an error')


st.button(
    "Submit",
    on_click=summarize,
    kwargs={"prompt": input_text},
)

# configure text area to populate with current state of summary
output_text = st.text_area(label='Summarized text:', value=st.session_state["summary"], height=300)