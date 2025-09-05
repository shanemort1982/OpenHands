# Microagent injection status

Prompt dir: /openhands/code/openhands/agenthub/codeact_agent/prompts
Resolved system prompt filename: None

PromptManager microagent references in source (openhands/utils/prompt.py):
- L8: from openhands.events.observation.agent import MicroagentKnowledge
- L66:         self.microagent_info_template: Template = self._load_template(
- L67:             'microagent_info.j2'
- L121:     def build_microagent_info(
- L123:         triggered_agents: list[MicroagentKnowledge],
- L125:         """Renders the microagent info template with the triggered agents.
- L128:             triggered_agents: A list of MicroagentKnowledge objects containing information
- L129:                               about triggered microagents.
- L131:         return self.microagent_info_template.render(

Rendered system prompt contains microagent info? NO

Rendered system prompt length: 13423 chars
Rendered system prompt preview (first 400 chars):
You are OpenHands agent, a helpful AI assistant that can interact with a computer to solve tasks.

<ROLE>
Your primary role is to assist users by executing commands, modifying code, and solving technical problems effectively. You should be thorough, methodical, and prioritize quality over speed.
* If the user asks a question, like "why is X happening", don't try to fix the problem. Just give an an

PromptManager attribute exposing combined microagent info: <none>
