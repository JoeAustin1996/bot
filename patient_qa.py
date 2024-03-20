import streamlit as st
import openai

# Assuming you've set your API key in your environment variables
# Otherwise, you can set it here with openai.api_key = 'your_api_key_here'
openai.api_key = "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"

def get_gpt_response(context, query):
    """Generate a response from GPT-3.5 Turbo given the context and user query, assuming the user is a doctor."""
    prompt = f"{context}\nQ: {query}\nA:"
    response_sql = openai.ChatCompletion.create(
            model="gpt-4",  # Ensure this matches your GPT model version
            messages=[
                {"role": "system", "content": f"{context} You are a doctor with expertise in medications."},
                {"role": "user", "content": query}
            ]
        )
    return response_sql.choices[0].message['content']

# Streamlit app layout
st.title('Medical Inquiry Assistant')
context = "As a medical professional, you often need to provide advice on various health conditions, treatments, and medications."  # Example context
st.write("Context for this session:", context)

# User input
user_query = st.text_input("Ask a question based on the context:")

if st.button('Generate Response'):
    if user_query:
        # Generate and display response
        response = get_gpt_response(context, user_query)
        st.write(f"Response: {response}")
    else:
        st.write("Please enter a question.")
