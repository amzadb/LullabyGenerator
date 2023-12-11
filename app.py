def main():
    import streamlit as st
    st.set_page_config(
        page_title="Generate Lullaby",
        layout="centered"
    )
    
    st.title("AI driven Lullaby 🎶")

    text_location = st.text_input(label="Location for the story")
    text_character = st.text_input(label="Character name in the story")
    text_translate = st.text_input(label="Translate the story into...")
    
    button_submit = st.button("Submit")
    
    if text_location and text_character and text_translate:
        if button_submit:
            with st.spinner("Generating Lullaby..."):
                import langchain_helper as helper
                response = helper.generate_lullaby(
                    location=text_location, 
                    name=text_character, 
                    language=text_translate
                )

                with st.expander("English Version"):
                    st.write(response['story'])
                
                with st.expander(f"{text_translate} Version"):
                    st.write(response['translated_story'])
                    
            st.success("Lullaby generated successfully...")
            

if __name__ == "__main__":
    main()