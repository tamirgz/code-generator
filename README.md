# Code Generation Workflow

## Overview

This project implements a code generation workflow using the `agno` Python package. The workflow is designed to generate, review, and execute Python code based on user input. It leverages agents for different tasks like code generation, code review, and execution. The generated code is intended to build workflows using the `agno` library.

## Key Components

### CodeGenerationWorkflow Class

- **Description**: This class facilitates the entire workflow process. It initializes agents for code generation and review and manages the execution of the generated code.
- **Fields**:
  - `description`: A brief description of the workflow's purpose.
- **Methods**:
  - `create_agents(self)`: Sets up agents for code generation and review.
  - `execute_python_code(self, code: str)`: Executes generated Python code and returns the result or an error message.
  - `update_run_method(self)`: Updates the run method to integrate code generation, review, and execution.
  - `run_workflow(self, user_input: str)`: Main method to execute the workflow using provided user input.

### Agents

- **Code Generator**: Generates Python code based on natural language instructions. It focuses on clarity, efficiency, and correctness.
- **Code Reviewer**: Reviews generated Python code for potential bugs, errors, or inefficiencies. Provides detailed feedback if any issues are found.
- **Code Executor**: Execute the code using Python code execution tool.

## Workflow Execution

1. **Initialization**: The `CodeGenerationWorkflow` class is instantiated, which initializes the workflow storage and agents.
2. **Code Generation**: The `run_workflow` method is called with user input. The code generator agent creates Python code based on the input.
3. **Code Review**: The generated code is reviewed by the code reviewer agent for any issues.
4. **Code Execution**: If no bugs are found, the code is executed, and the results are returned. If bugs are found, the workflow attempts to regenerate the code with feedback.

## Dependencies

- `agno`: Used for managing agents and workflows.
- `SqliteWorkflowStorage`: Utilized for workflow storage.
- `Groq`: A model used by agents for generating and reviewing code.

## Installation

To install the necessary dependencies, run the following command:

```bash
pip install agno
```

## Usage

To use the code generation workflow, create an instance of `CodeGenerationWorkflow` and call the `run_workflow` method with your desired input:

```python
from CodeGeneration import CodeGenerationWorkflow

workflow = CodeGenerationWorkflow()
workflow.run_workflow(user_input="Your input here")
```

This README provides a comprehensive overview of how to use the code generation workflow and its core components. For further details, refer to the code documentation in `CodeGeneration.py`.
