from CodeGeneration import CodeGenerationWorkflow
from typing import Iterator
from agno.agent import RunResponse
from agno.utils.pprint import pprint_run_response

# Create workflow
workflow = CodeGenerationWorkflow()

# Run workflow
for response in workflow.run_workflow(user_input="Generate python code create agents using agno python package that builds a workflow to generate news reports based on articles from a given URL"):
    pprint_run_response(response, markdown=True, show_time=True)