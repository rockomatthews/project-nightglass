# Implementation plan

Milestones are dependency gates, not calendar promises. Hooded maintains scope and reviews evidence; contributors opt in individually. No contributor is assigned by this document.

## M0 — Reference and setup

Deliver the reference observations, acceptance checklist, original asset policy, pinned engine instructions, and a buildable minimal C++ Unreal project with Game, Editor and Server targets. Capture exact engine revision and compiler/toolchain from a successful Windows build. Gate: a fresh checkout builds; an empty dedicated server and two clients connect. The current repository contains planning documents only; this gate has not passed.

## M1 — Authoritative match loop

Implement four-player 2v2 admission, ready states, team selection, lobby/round/results state, server clock, three terminal actors, scoring, respawn budgets, side swap and full reset. Gate: four separate clients complete two matches without contradictory scores, team overflow or stuck phase transitions. Depends on M0.

## M2 — Asymmetric interaction

Implement spy third-person movement/camera and authored traversal; merc first-person movement/weapon/flashlight; spatial sound and exposure cues; distraction, stun and motion sensing with counters. Gate: server validates actions and inventories; recorded tests show readable feedback and no through-wall interaction. Depends on M1; tune with M3.

## M3 — Relay Annex graybox

Build an original three-terminal map, patrol loops and spy alternate routes. Add deliberate light/dark spaces and surface sound variation. Gate: all objectives reachable by intended routes, no spawn traps or invalid geometry escapes, route timings documented from both perspectives. Depends on M1; iterate with M2.

## M4 — Reliable vertical slice

Add rebinding, basic tutorial, private IP joining, useful error messages, disconnect policy, match restart and logs. Test packet loss and latency, abuse validation, graphics consistency and repeated matches. Gate: docs/TESTING.md evidence complete, critical defects closed, new tester can join without developer intervention. Depends on M2 and M3.

## After the gate

Use evidence to choose the next improvement: more maps/gadgets, accessibility, polish, or matchmaking. Do not expand scope to compensate for a weak stealth loop. Paid services/assets and contractor commitments require separate operator approval.

## Tracking

GitHub issues carry dependency, deliverable and acceptance criteria. Statuses: proposed, opted-in, in-progress, review, verified. Only mark verified with linked test evidence. The project goal issue hosts the public goal and this implementation plan; Musebook's Studio board links to it.
