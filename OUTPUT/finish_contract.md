# FinishTool Contract Summary

- Source: openhands/agenthub/codeact_agent/tools/finish.py
- Required: message
- Emits summary field: Yes
- Emits artifacts (paths/PR URLs): No/Not explicit
- summary references: openhands/agenthub/codeact_agent/tools/finish.py:12
- Hook to block finish when QA is red: Found potential references
  - Files: tests/unit/llm/test_llm_fncall_converter.py, evaluation/benchmarks/gpqa/run_infer.py, evaluation/benchmarks/logic_reasoning/run_infer.py, evaluation/benchmarks/toolqa/run_infer.py, evaluation/benchmarks/toolqa/utils.py

- Parameters schema excerpt (starts at openhands/agenthub/codeact_agent/tools/finish.py:23):

```
parameters={ 'type': 'object', 'required': ['message'], 'properties': { 'message': { 'type': 'string', 'description': 'Final message to send to the user', }, }, },
```
