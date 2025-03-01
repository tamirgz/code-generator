import streamlit as st
from CodeGeneration import CodeGenerationWorkflow
from typing import Iterator
from agno.agent import RunResponse
from agno.utils.pprint import pprint_run_response

# Streamlit UI
st.title("Code Generation Workflow")

user_input = st.text_area("Enter your request:", value="Generate python code create agents using agno python package that builds a workflow to generate news reports based on articles from a given URL")

if st.button("Run Workflow"):
    if not user_input:
      st.error("Please enter your request for code to be generated.")
    else:
        workflow = CodeGenerationWorkflow()
        with st.spinner("Running..."):
            
            for response in workflow.run_workflow(user_input=user_input):
                st.text_area("Response:", value=pprint_run_response(response), height=300)
                st.write("\n\n")
