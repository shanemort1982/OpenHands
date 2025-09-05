Generated: 2025-09-05T10:35:32.791488+00:00

Finish tool contract
- File: openhands/agenthub/codeact_agent/tools/finish.py
- Fields expected when declaring done: parameters.required = ['message']; parameters.properties.message: string (final message to user). (finish.py:23–31)
- Emits summary/artifacts: No explicit summary/artifact fields in tool schema. The FinishTool only accepts 'message'. (finish.py:23–33)
- Handling: In response parsing, a FinishTool call becomes AgentFinishAction(final_thought=arguments.get('message','')). (function_calling.py:147–151)
- AgentFinishAction supports optional outputs: dict, but FinishTool does not populate it. (events/action/agent.py:17–41)
- Controller effect: On AgentFinishAction, controller marks conversation finished; no QA gating logic observed. (controller/agent_controller.py:168–175)

QA gating
- Searched for QA/quality hooks; no hook found that blocks finish based on QA status in the finish path. (no matches)
