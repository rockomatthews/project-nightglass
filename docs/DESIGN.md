# Design brief

## Experience contract

Primary reference: Chaos Theory classic 2v2 Spies vs Mercs. This is an original successor, not a recreation of Ubisoft content. Preserve the decision-making and asymmetry, not copied levels, characters, names, audio, or exact undocumented numeric values.

Two third-person infiltrators (spies) use concealment, traversal, and coordinated distractions to complete objectives. Two first-person defenders (mercenaries) use lethal force, light, information, and patrol routes to stop them. Stealth must be useful without making inactivity optimal; detection should create decisions rather than unavoidable death.

## Reference checklist

These are intended pillars to validate against lawful reference play, not claims that every detail matches the original game. The reference issue must attach observations with mode/platform/version and timestamps before tuning is called faithful.

| Area | Preserve | Improve | Observable test |
| --- | --- | --- | --- |
| Viewpoints | Third-person spy awareness, first-person merc tension | Rebindable input and consistent camera collision | Spy camera cannot pass through walls; merc has no unintended third-person information |
| Movement | Deliberate quiet movement, crouching, climbing and alternate routes | Responsive transitions and clear traversal affordances | Repeated climb/crouch cycles work for remote clients without stuck states |
| Visibility | Darkness, light, and deliberate searching | Consistent exposure cues | The same positions remain readable at supported graphics presets |
| Sound | Movement and action sounds reveal choices | Clear spatial cues and volume controls | Blind listening tests distinguish movement direction and meaningful noise |
| Detection | Complementary tools with tradeoffs | Explain limits and counterplay | Every detection tool has measured range, duration, cooldown and counter-test |
| Gadgets | Distraction, denial, information and counters | Clear feedback and limited initial inventory | Each tool changes a documented decision without replacing stealth |
| Objectives | Attack/defend pressure and coordinated routes | Legible progress and interruption | Progress is server-authoritative; remote cancel/contest outcomes agree |
| Rounds | Short repeatable contests and side switching | Reliable reset and clear results | Two complete matches reset all objective, inventory and team state |

## First playable defaults (provisional tuning)

One original graybox map: **Relay Annex**, an industrial communications facility with three separated terminals, at least two approaches per terminal, spy-only traversal links, and merc-accessible patrol loops. These are original layouts, not remakes of existing maps.

Prototype mode: 2v2, 8-minute rounds; spies must complete any two of three terminals. Each terminal needs 20 uninterrupted seconds of interaction by one spy; interruption resets that attempt. Three shared spy respawns, merc respawn after 10 seconds. Spies win on objective completion; mercs win on timeout or no living spies and no remaining respawns. Swap sides after each round; each team attacks once. One round each is a draw initially. All figures are tuning hypotheses, not claimed Chaos Theory rules.

Start with walk/crouch/run, a small authored climb/vault set, spy distraction emitter, merc flashlight and movement sensor, one merc weapon, and a short spy stun to escape. Stun is not a replacement for shooting. Decide additional gadgets and close-quarters mechanics only after reference and balance tests.

No campaign, progression economy, monetization, licensed content, console target, ranked ladder, or public matchmaking in the first slice. No exact fidelity or release date promised.
