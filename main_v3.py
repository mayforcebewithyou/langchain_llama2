import streamlit as st
from llama_cpp import Llama

def llm_model():
   # Load quantized model
    model_path = "/Users/santu/Desktop/llama2/llama.cpp/models/7B/ggml-model-q4_0.bin"
    model = Llama(model_path = model_path,
                    n_ctx = 1024,            # context window size
                    #n_gpu_layers = 1,        # enable GPU
                    use_mlock = True)        # enable memory lock so not swap
    return model

def main():
    st.set_page_config(page_title="Llama Chat", page_icon=":robot:")
    st.header("Chat with Llama")
    # Streamlit text input 
    question = st.text_input("Ask a question:")

    if question:
        model=llm_model()
        # Get LLama prediction
        response = model(prompt = question, max_tokens=1000, temperature = 0.1, top_p=0.7)
        # Display predicted answer
        st.write(response['choices'][0]['text'])
        # Display explanation
        if "explanation" in response:
            st.write(response["explanation"])

if __name__ == '__main__':
    main()