# Observer Hook Points in CodeActAgent
Source: `openhands/agenthub/codeact_agent/codeact_agent.py` (296 lines)
Generated: 2025-09-05T10:23:58.782288+00:00

This note identifies minimally invasive places to POST small JSON events (observer hooks) for runtime introspection.

## (a) Messages are assembled
- Function: `CodeActAgent._get_messages`
- Lines: 243–290
- Least invasive insertion: right before `return messages` near the end of the function

Example patch snippet:
```python
# … inside CodeActAgent._get_messages, right before `return messages`
import os, time
try:
    url = os.getenv('SB_OBSERVER_URL')
    if url:
        payload = {
            'phase': 'messages.assembled',
            'ts': time.time(),
            'count': len(messages),
            'cache_active': bool(self.llm.is_caching_prompt_active()),
        }
        import requests
        requests.post(url, json=payload, timeout=1.0)
except Exception:
    pass
return messages
```

## (b) The LLM is called
- Function: `CodeActAgent.step`
- Lines: 157–221
- Least invasive insertions: pre-call right before line 215, post-call right after it

Example patch snippet:
```python
# … inside CodeActAgent.step, before the LLM call
import os, time
try:
    url = os.getenv('SB_OBSERVER_URL')
    if url:
        payload = {
            'phase': 'llm.before_call',
            'ts': time.time(),
            'model': self.llm.config.model,
            'has_tools': bool(params.get('tools')),
            'messages_len': len(params.get('messages') or []),
        }
        import requests
        requests.post(url, json=payload, timeout=1.0)
except Exception:
    pass
response = self.llm.completion(**params)
try:
    url = os.getenv('SB_OBSERVER_URL')
    if url:
        payload = {
            'phase': 'llm.after_call',
            'ts': time.time(),
            'model': self.llm.config.model,
            'finish_reason': getattr(getattr(response.choices[0], 'finish_reason', None), 'value', None) if getattr(response, 'choices', None) else None,
        }
        import requests
        requests.post(url, json=payload, timeout=1.0)
except Exception:
    pass
```

## (c) Tool calls are dispatched
- Function: `CodeActAgent.step`
- Lines: 217–181
- Least invasive insertion: inside the loop that enqueues actions (emit once per action)

Example patch snippet:
```python
actions = self.response_to_actions(response)
for action in actions:
    try:
        url = os.getenv('SB_OBSERVER_URL')
        if url:
            payload = {
                'phase': 'tool.dispatch',
                'ts': time.time(),
                'tool': getattr(action, 'name', action.__class__.__name__),
                'args': getattr(action, 'arguments', None),
            }
            import requests
            requests.post(url, json=payload, timeout=1.0)
    except Exception:
        pass
    self.pending_actions.append(action)
```

## (d) Results / observations are recorded
- This module does not perform observation recording directly; observations are added by the controller/runtime after executing actions.
- Practical hook in this file: right after condensation and before messages are built, to summarize the condensed history.
- Function: `CodeActAgent.step`
- Lines: 192–None

Example patch snippet:
```python
# … inside CodeActAgent.step, after condensed_history is set
import os, time
try:
    url = os.getenv('SB_OBSERVER_URL')
    if url:
        obs_count = sum(1 for e in condensed_history if getattr(e, 'event_type', '') == 'observation')
        payload = {
            'phase': 'history.condensed',
            'ts': time.time(),
            'events': len(condensed_history),
            'observations': obs_count,
        }
        import requests
        requests.post(url, json=payload, timeout=1.0)
except Exception:
    pass
```

Notes:
- These insertions avoid heavy serialization and keep network IO best-effort (timeouts, exceptions suppressed).
- You can centralize the POST helper to a small utility and gate by env.
- Exact line numbers may shift with upstream changes; anchor near these statements.
