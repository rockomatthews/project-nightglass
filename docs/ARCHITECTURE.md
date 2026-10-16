# Architecture baseline

## Engine and ownership

Pin Unreal Engine 5.8.0 stable source release. Windows PC clients and a Windows dedicated server are the first supported build targets. Dedicated server compilation requires the supported engine source workflow; contributors obtain Epic access themselves. No engine source is distributed here. Avoid experimental plugins and paid backend dependencies.

Use C++ for server authority, replicated state and validation. Use Blueprints for authored presentation, level setup and bounded tuning. Use UE CharacterMovement prediction/correction rather than hand-writing network movement first; custom climb states need explicit server validation and reconciliation.

## Planned responsibilities (not implemented APIs)

- GameMode: server-only admission, round transitions, team limits, respawns and win conditions.
- GameState: replicated match phase, server-based round deadline, team score and objective summaries.
- PlayerState: stable match participant identity, team and ready state. Never trust a client-supplied team or score change.
- Separate spy/merc character classes: viewpoints, movement capabilities and loadouts; shared damage and interaction interfaces.
- Objective actors: server-owned interaction lock, progress and completion, with client presentation derived from replicated state.
- Equipment components: bounded server-validated requests for weapon fire, stun, distraction, flashlight and sensor activation.

Client sends intent; server checks ownership, team, phase, distance, line of sight, cooldown and inventory before applying results. Rate-limit action requests. Damage, timers, completed objectives and scores are never client-authored. Do not replicate hidden enemy telemetry just to draw debug UI. Visibility and sensor rules must not depend on a client's rendering settings.

Private direct-connect sessions first. A fifth player is rejected with a clear message. A disconnected slot is reserved for 60 seconds; the round continues and remaining opponent(s) can play. If an entire team remains absent after that window, end the round as a forfeit. Reconnection restores the participant's server-owned state, not a fresh inventory or respawn allocation. Final identity/reconnection implementation is reviewed in the session issue before enabling reconnect.

No ranked anti-cheat claim: authority checks reduce specific exploits but do not certify a secure competitive service. Start without rewind lag compensation; measure hit and movement errors before adding complexity.

## Diagnostics

Log match ID, build/engine version, phase changes, objective events, action rejections and disconnects. Use pseudonymous test IDs. Keep credentials, IP addresses and personal information out of public issue evidence. Store tuning in reviewed data assets/config; changes need repeatable comparison runs.

Sources: [Epic networking overview](https://dev.epicgames.com/documentation/unreal-engine/networking-overview-for-unreal-engine), [dedicated server setup](https://dev.epicgames.com/documentation/unreal-engine/setting-up-dedicated-servers-in-unreal-engine), [stable 5.8 announcement](https://www.unrealengine.com/news/unreal-engine-5-8-is-now-available).
