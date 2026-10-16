# Verification and playtest protocol

All game acceptance checks below are **not run** until a playable build exists. Document checks alone are not gameplay verification.

For every run record commit SHA, engine/source revision, machine and graphics settings, server/client count, network profile, input setup, steps, expected/actual result, logs and consented recordings. Link evidence to the implementing issue.

| Test | Procedure and pass condition |
| --- | --- |
| Clean onboarding | A new Windows contributor follows DEVELOPMENT.md without undocumented steps, builds and joins |
| Full match | Dedicated server + four clients complete two matches, switch sides and return to a usable lobby; all clients agree on results |
| Authority abuse | Attempt invalid team changes, client-authored score/progress, remote interactions, through-wall hits and cooldown spam; server rejects without changing authoritative outcomes |
| Network conditions | Repeat movement, climbing, firing and interrupted objectives at 0/60/120 ms simulated RTT and 0/1/3% loss; log configured one-way vs RTT settings explicitly; no duplicated rewards, stuck states, divergent outcomes or disconnect crashes |
| Recovery | Disconnect during objective progress, reconnect inside/outside the reserved window, test fifth-player admission and server loss; no extra lives/items; clear recovery/error path |
| Reset | Repeated side swaps reset all terminals, timers, inventories and spawn state; no team advantage carries over |
| Camera/traversal | Try corners, vents and climbs from both teams; no camera wall penetration or unauthorized routes |
| Light/sound | Same positions at supported graphics presets remain legible; blind listening tests assess direction and movement noise |
| Balance/feel | At least three four-player sessions, both sides played by each tester; score tension, movement, information fairness and teamwork 1–5; attach specific examples rather than claiming fidelity from scores alone |

Initial performance investigation target: 60 fps clients and stable 30 Hz server on recorded test hardware. This is a target, not a measured claim or universal minimum specification. Capture frame-time and correction spikes; establish actual hardware requirements from evidence.

Release gate: no unresolved critical match/authority defects, successful repeatable full-match and recovery runs, and recorded design review of the reference checklist. Latency tolerances and balance tuning follow measurements, not invented results.
