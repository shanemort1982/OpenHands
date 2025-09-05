# Finish contract (CCI)

File: /openhands/code/openhands/agenthub/codeact_agent/tools/finish.py

Entities and line ranges:
- ChatCompletionToolParam: L752-753
- ChatCompletionToolParamFunctionChunk: L740-744

Annotated fields (candidates for required inputs):
- ChatCompletionToolParam.type: Union
- ChatCompletionToolParam.function: ChatCompletionToolParamFunctionChunk
- ChatCompletionToolParam.cache_control: ChatCompletionCachedContent
- ChatCompletionToolParamFunctionChunk.name: Required
- ChatCompletionToolParamFunctionChunk.description: str
- ChatCompletionToolParamFunctionChunk.parameters: dict
- ChatCompletionToolParamFunctionChunk.strict: bool

Notes:
- Determine whether finish emits a summary or artifacts by reading its implementation (e.g., whether it creates SuccessObservation with content).
- To block finish on QA failure, add a guard in AgentController or in a pre-finish validation tool that must succeed before the finish tool is allowed to execute.
