# Observer hook points (S2)

File: /openhands/code/openhands/agenthub/codeact_agent/codeact_agent.py

a) Messages assembled around:
- L204:         messages = self._get_messages(condensed_history, initial_user_message)
- L206:             'messages': messages,
- L242:     def _get_messages(
- L248:         and formatting them into messages that the LLM can understand. It handles both regular
- L253:         2. Processes events (Actions and Observations) into messages, including SystemMessageAction
- L260:             events: The list of events to convert to messages
- L263:             list[Message]: A list of formatted messages ready for LLM consumption, including:
- L265:                 - Action messages (from both user and assistant)
- L266:                 - Observation messages (including tool responses)
- L272:             - Messages from the same role are combined to prevent consecutive same-role messages

b) LLM called around:
- L214:         response = self.llm.completion(**params)

c) Tool calls dispatched by constructing Action instances around:
- L165:         - CmdRunAction(command) - bash command to run
- L166:         - IPythonRunCellAction(code) - IPython code to run
- L167:         - AgentDelegateAction(agent, inputs) - delegate action for (sub)task
- L168:         - MessageAction(content) - Message action to run (e.g. ask for clarification)
- L169:         - AgentFinishAction() - end the interaction
- L170:         - CondensationAction(...) - condense conversation history by forgetting specified events and optionally providing a summary
- L171:         - FileReadAction(path, ...) - read file content from specified path
- L172:         - FileEditAction(path, ...) - edit file using LLM-based (deprecated) or ACI-based editing
- L173:         - AgentThinkAction(thought) - log agent's thought/reasoning process
- L174:         - CondensationRequestAction() - request condensation of conversation history
- L175:         - BrowseInteractiveAction(browser_actions) - interact with browser using specified actions
- L176:         - MCPAction(name, arguments) - interact with MCP server tools
- L185:             return AgentFinishAction()
- L165:         - CmdRunAction(command) - bash command to run
- L21: from openhands.agenthub.codeact_agent.tools.llm_based_edit import LLMBasedFileEditTool

d) Observations recorded around:

## Minimal POST example to $SB_OBSERVER_URL
```bash
curl -sS -X POST "$SB_OBSERVER_URL/observe" \
  -H "Content-Type: application/json" \
  -d "{"event":"llm_call","agent":"CodeActAgent","file":"codeact_agent.py","line":123,"meta":{"note":"hook example"}}"
```
