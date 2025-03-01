from CodeGeneration import CodeGenerationWorkflow
from typing import Iterator
from agno.agent import RunResponse
from agno.utils.pprint import pprint_run_response

workflow: Iterator[RunResponse] = CodeGenerationWorkflow().run_workflow(user_input="Generate python code create agents using agno python package that builds a workflow to generate news reports based on articles from a given URL")

# Print the report
pprint_run_response(workflow, markdown=True, show_time=True)
