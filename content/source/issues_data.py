"""
Single source of truth for all 16 issues of Anonymous Heroes.

Edit THIS file to change story content, then run:
    python scripts/export_issue_yaml.py
to regenerate content/issues/issue-NN.yaml for the art/build pipeline.

Structure:
ISSUES = [ { act, number, slug, title, music_cue, pages: [ { page, panels: [ {...} ] } ] } ]

Panel fields:
  id            - panel number within the page
  shot          - shot type / framing note for the artist or AI prompt
  description   - visual description of the panel
  narration     - optional narration caption (str or None)
  dialogue      - optional list of {speaker, line}
  image_prompt  - prompt sent to the AI art backend (falls back to description)
"""

ISSUES = [
    # ---------------------------------------------------------------- ACT 1
    {
        "act": 1, "number": 1, "slug": "ghost-protocol", "title": "Ghost Protocol",
        "music_cue": "Low ambient synth; Anonymous's solo motif introduced.",
        "pages": [
            {"page": 1, "panels": [
                {"id": 1, "shot": "Wide establishing shot",
                 "description": "Rain-slicked cyberpunk city, neon signage reflected in puddles.",
                 "narration": "Before there was a team, there was one man convinced the world was already lost.",
                 "dialogue": [],
                 "image_prompt": "Acubi aesthetic, wide establishing shot, futuristic city at night, rain, neon reflections, muted earth-tone palette with cyan accent lighting."},
                {"id": 2, "shot": "Close-up",
                 "description": "Anonymous's hands typing across multiple monitors, code cascading.",
                 "narration": "Six years ago.", "dialogue": [], "image_prompt": None},
            ]},
            {"page": 2, "panels": [
                {"id": 3, "shot": "Medium, cramped interior",
                 "description": "Anonymous (unmasked, younger) in a cramped apartment, exhausted, takeout containers and hardware everywhere.",
                 "narration": None,
                 "dialogue": [{"speaker": "Anonymous", "line": "One more layer. One more wall between them and the truth."}],
                 "image_prompt": None},
                {"id": 4, "shot": "Flashback insert, desaturated",
                 "description": "A shadowy mentor figure (MSmaster, younger, not yet villainous) teaching him at a terminal.",
                 "narration": None,
                 "dialogue": [{"speaker": "MSmaster", "line": "The mask isn't to hide from them. It's to hide from yourself."}],
                 "image_prompt": None},
            ]},
            {"page": 3, "panels": [
                {"id": 5, "shot": "Action, tense",
                 "description": "Present day. Anonymous, now masked, breaks into a low-level corporate server — sloppy, not yet the polished hacker he'll become. Alarms trigger.",
                 "narration": None, "dialogue": [], "image_prompt": None},
                {"id": 6, "shot": "Alley, handheld feel",
                 "description": "He barely escapes, hiding in an alley, breathing hard.",
                 "narration": None,
                 "dialogue": [{"speaker": "Anonymous", "line": "Too close. I need people who don't need me to be perfect."}],
                 "image_prompt": None},
            ]},
            {"page": 4, "panels": [
                {"id": 7, "shot": "Close on screen",
                 "description": "A data packet arrives on his terminal — untraceable, encrypted, signed only with a hat icon.",
                 "narration": "The first thread. He didn't know yet it would become a rope.",
                 "dialogue": [{"speaker": "Screen text", "line": "You're being watched. Not by them. By me. — H"}],
                 "image_prompt": None},
            ]},
        ],
    },
    {
        "act": 1, "number": 2, "slug": "static", "title": "Static",
        "music_cue": "Two motifs: Rusty (industrial/mechanical), Zero (fast/glitchy).",
        "pages": [
            {"page": 1, "panels": [
                {"id": 1, "shot": "Industrial interior",
                 "description": "An off-grid server farm. Rusty, a contractor, discovers his company selling backdoor access to a hostile buyer.",
                 "narration": None,
                 "dialogue": [{"speaker": "Rusty", "line": "This isn't a bug. Somebody built this on purpose."}],
                 "image_prompt": None},
                {"id": 2, "shot": "Tense two-shot",
                 "description": "Rusty is caught reviewing the logs by his supervisor.",
                 "narration": None,
                 "dialogue": [{"speaker": "Supervisor", "line": "Walk away, Rusty. Some doors you don't knock on twice."}],
                 "image_prompt": None},
            ]},
            {"page": 2, "panels": [
                {"id": 3, "shot": "Quiet, resolute",
                 "description": "Rusty walks away — but pockets a drive first. No music sting, just resolve.",
                 "narration": None, "dialogue": [], "image_prompt": None},
            ]},
            {"page": 3, "panels": [
                {"id": 4, "shot": "Neon-lit stealth op",
                 "description": "Zero, in his stealth suit, mid-op with the scammer-payback crew, exposing a phone-scam call center live to camera.",
                 "narration": None,
                 "dialogue": [{"speaker": "Blue-Haired Leader", "line": "Get the footage and get out, Zero. We're not the story."}],
                 "image_prompt": None},
                {"id": 5, "shot": "Chase, dynamic angle",
                 "description": "Zero hesitates too long, gets made by a security guard. Chase begins, cut off mid-chase.",
                 "narration": None, "dialogue": [], "image_prompt": None},
            ]},
            {"page": 4, "panels": [
                {"id": 6, "shot": "Split panel",
                 "description": "Split panel: Rusty staring at the stolen drive / Zero cornered in a stairwell.",
                 "narration": "Two men. Two doors closing. Neither knew the other existed yet.",
                 "dialogue": [], "image_prompt": None},
            ]},
        ],
    },
    {
        "act": 1, "number": 3, "slug": "first-blood-first-failure", "title": "First Blood, First Failure",
        "music_cue": "Tension strings, no resolution chord at issue end.",
        "pages": [
            {"page": 1, "panels": [
                {"id": 1, "shot": "Silhouette meeting",
                 "description": "Anonymous, having tracked 'H' (The Hat) through the encrypted signature, meets him in person — silhouette only, voice modulated.",
                 "narration": None,
                 "dialogue": [{"speaker": "The Hat", "line": "You're not ready. But you're close. Close enough to be useful — or close enough to be dead."}],
                 "image_prompt": None},
            ]},
            {"page": 2, "panels": [
                {"id": 2, "shot": "Briefing",
                 "description": "The Hat sets up the team's first real job: intercepting a data shipment before a corrupt official can bury evidence.",
                 "narration": None, "dialogue": [], "image_prompt": None},
                {"id": 3, "shot": "Introductions, separate",
                 "description": "Rusty and Zero are recruited separately by The Hat, each reluctant, each with something to prove.",
                 "narration": None, "dialogue": [], "image_prompt": None},
            ]},
            {"page": 3, "panels": [
                {"id": 4, "shot": "Chaotic action",
                 "description": "The uncoordinated team meets for the first time on-site and botches the timing; security response is faster than expected.",
                 "narration": None, "dialogue": [], "image_prompt": None},
                {"id": 5, "shot": "Frantic close-ups",
                 "description": "Rusty improvises a hardware fix under fire; Zero freezes; Anonymous has to abandon part of the plan.",
                 "narration": None,
                 "dialogue": [{"speaker": "Anonymous", "line": "We're not a team. We're three guys who happened to show up."}],
                 "image_prompt": None},
            ]},
            {"page": 4, "panels": [
                {"id": 6, "shot": "Retreat, low light",
                 "description": "They escape, barely, empty-handed on the primary objective — only a partial data fragment recovered.",
                 "narration": "Failure has a way of introducing people faster than success ever could.",
                 "dialogue": [], "image_prompt": None},
            ]},
        ],
    },
    {
        "act": 1, "number": 4, "slug": "the-playground", "title": "The Playground",
        "music_cue": "Main team theme introduced, full instrumentation.",
        "pages": [
            {"page": 1, "panels": [
                {"id": 1, "shot": "Debrief, unemotional",
                 "description": "Aftermath meeting, tense. The Hat lays out what went wrong, precise and unemotional.",
                 "narration": None,
                 "dialogue": [{"speaker": "The Hat", "line": "You don't need to like each other. You need to trust the work."}],
                 "image_prompt": None},
            ]},
            {"page": 2, "panels": [
                {"id": 2, "shot": "Corporate meeting, guarded",
                 "description": "Mister MC (Jared Derival) is approached separately — a corporate insider offering resources for information.",
                 "narration": None, "dialogue": [], "image_prompt": None},
                {"id": 3, "shot": "Duo introduction",
                 "description": "The Santos twins (Joas & Iris) are brought in as support, established as an inseparable package deal.",
                 "narration": None, "dialogue": [], "image_prompt": None},
            ]},
            {"page": 3, "panels": [
                {"id": 4, "shot": "Distant, observational",
                 "description": "TrebleSmak and The Suit (Ron Sharon) shown operating independently at a distance — seeds for later issues.",
                 "narration": None, "dialogue": [], "image_prompt": None},
                {"id": 5, "shot": "Warm, small-scale",
                 "description": "First genuine team moment: Rusty fixes Zero's suit calibration; small, human, unforced camaraderie.",
                 "narration": None, "dialogue": [], "image_prompt": None},
            ]},
            {"page": 4, "panels": [
                {"id": 6, "shot": "Clean, satisfying action",
                 "description": "The team takes a smaller, controlled job and succeeds — coordinated, after three issues of stumbling.",
                 "narration": "It wasn't a playground. Not yet. But it was starting to feel like one.",
                 "dialogue": [], "image_prompt": None},
                {"id": 7, "shot": "Rooftop silhouette",
                 "description": "A masked figure watches from a rooftop — Blu Corbel, unidentified to the reader yet.",
                 "narration": None, "dialogue": [], "image_prompt": None},
            ]},
        ],
    },

    # ---------------------------------------------------------------- ACT 2
    {
        "act": 2, "number": 5, "slug": "noise-in-the-signal", "title": "Noise in the Signal",
        "music_cue": "Unease motif; low drone under dialogue.",
        "pages": [
            {"page": 1, "panels": [
                {"id": 1, "shot": "Post-mission confusion",
                 "description": "A job goes wrong in a way that doesn't make sense — the target was tipped off before the plan was finalized.",
                 "narration": None,
                 "dialogue": [{"speaker": "Rusty", "line": "Nobody outside this room knew the target. Nobody."}],
                 "image_prompt": None},
            ]},
            {"page": 2, "panels": [
                {"id": 2, "shot": "Isolated, quiet",
                 "description": "The Hat grows uncharacteristically quiet, running his own investigation.",
                 "narration": None, "dialogue": [], "image_prompt": None},
                {"id": 3, "shot": "Cryptic approach",
                 "description": "Blu Corbel approaches Anonymous directly, cryptic, clearly knowing more than he should.",
                 "narration": None,
                 "dialogue": [{"speaker": "Blu Corbel", "line": "I'm not your enemy. I'm also not your friend. Figure out which one you need more."}],
                 "image_prompt": None},
            ]},
            {"page": 3, "panels": [
                {"id": 4, "shot": "Villain thread, cold",
                 "description": "MSmaster, embittered, is shown for the first time since Issue 1, working with unknown backers.",
                 "narration": None,
                 "dialogue": [{"speaker": "MSmaster", "line": "My student thinks he outgrew me. Let's remind him what he learned first."}],
                 "image_prompt": None},
            ]},
            {"page": 4, "panels": [
                {"id": 5, "shot": "Ending beat, grim",
                 "description": "A second job also leaks. Pattern confirmed — someone close to the team is compromised or watched.",
                 "narration": None, "dialogue": [], "image_prompt": None},
            ]},
        ],
    },
    {
        "act": 2, "number": 6, "slug": "teachers-pet", "title": "Teacher's Pet",
        "music_cue": "Flashback motif, distorted version of Anonymous's theme.",
        "pages": [
            {"page": 1, "panels": [
                {"id": 1, "shot": "Flashback, desaturated",
                 "description": "MSmaster's fall from grace — fired, disgraced, blaming Anonymous's success for his ruin.",
                 "narration": None, "dialogue": [], "image_prompt": None},
                {"id": 2, "shot": "Shadowed recruitment",
                 "description": "MSmaster recruited by an unseen backer (voice/shadow only) — first hint of Shadow/The Syndicate, unnamed.",
                 "narration": None, "dialogue": [], "image_prompt": None},
            ]},
            {"page": 2, "panels": [
                {"id": 3, "shot": "Present day, probing",
                 "description": "MSmaster begins probing the team's network from outside, testing defenses, not attacking yet.",
                 "narration": None, "dialogue": [], "image_prompt": None},
                {"id": 4, "shot": "Recognition, close-up",
                 "description": "Anonymous notices the intrusion pattern and feels a chill of recognition — the technique is familiar.",
                 "narration": None,
                 "dialogue": [{"speaker": "Anonymous", "line": "I know this signature. I learned it from someone."}],
                 "image_prompt": None},
            ]},
            {"page": 3, "panels": [
                {"id": 5, "shot": "Team meeting, guarded",
                 "description": "Team meeting: Anonymous doesn't share his suspicion yet — first crack of internal secrecy.",
                 "narration": None, "dialogue": [], "image_prompt": None},
            ]},
            {"page": 4, "panels": [
                {"id": 6, "shot": "Villain resolve, cliffhanger",
                 "description": "MSmaster, alone, finalizes a plan to strike at the team through someone vulnerable — targeting Zero.",
                 "narration": None, "dialogue": [], "image_prompt": None},
            ]},
        ],
    },
    {
        "act": 2, "number": 7, "slug": "taken", "title": "Taken",
        "music_cue": "Sparse percussion, no melody until final panel.",
        "pages": [
            {"page": 1, "panels": [
                {"id": 1, "shot": "Ambush, professional",
                 "description": "Zero, off-mission doing solo scammer-payback work out of old habit, is ambushed professionally, not randomly.",
                 "narration": None, "dialogue": [], "image_prompt": None},
                {"id": 2, "shot": "Struggle, sudden",
                 "description": "Struggle; Zero is subdued and taken. No dramatic rescue attempt — he simply vanishes.",
                 "narration": None, "dialogue": [], "image_prompt": None},
            ]},
            {"page": 2, "panels": [
                {"id": 3, "shot": "Panic, blame",
                 "description": "Team discovers Zero missing hours later. Panic, blame, first real fracture.",
                 "narration": None,
                 "dialogue": [{"speaker": "Rusty", "line": "You've known something for two issues. Talk."}],
                 "image_prompt": None},
            ]},
            {"page": 3, "panels": [
                {"id": 4, "shot": "Confession, tense",
                 "description": "Anonymous admits his suspicion about MSmaster. The team is furious he sat on it.",
                 "narration": None, "dialogue": [], "image_prompt": None},
                {"id": 5, "shot": "Fragile truce",
                 "description": "The Hat intervenes, forces a fragile truce: find Zero first, sort trust later.",
                 "narration": None, "dialogue": [], "image_prompt": None},
            ]},
            {"page": 4, "panels": [
                {"id": 6, "shot": "Methodical, quiet",
                 "description": "Investigation begins — no action beat yet, just tense, methodical tracing of Zero's last signal.",
                 "narration": "Some rescues start with silence, not sirens.",
                 "dialogue": [], "image_prompt": None},
            ]},
        ],
    },
    {
        "act": 2, "number": 8, "slug": "the-mole", "title": "The Mole",
        "music_cue": "Discordant strings under team argument.",
        "pages": [
            {"page": 1, "panels": [
                {"id": 1, "shot": "Impossible trace",
                 "description": "The trace on Zero leads somewhere impossible — a signal originating inside the team's own secure channel.",
                 "narration": None, "dialogue": [], "image_prompt": None},
                {"id": 2, "shot": "Argument, close quarters",
                 "description": "Accusations fly. Rusty suspects Blu Corbel. Anonymous defends him, which makes things worse.",
                 "narration": None, "dialogue": [], "image_prompt": None},
            ]},
            {"page": 2, "panels": [
                {"id": 3, "shot": "Suspicion, corporate",
                 "description": "Mister MC, still a semi-outsider, is quietly suspected too — his corporate ties make him an easy target.",
                 "narration": None, "dialogue": [], "image_prompt": None},
                {"id": 4, "shot": "Stabilizing presence",
                 "description": "The Santos twins refuse to pick a side, insisting on evidence over instinct.",
                 "narration": None, "dialogue": [], "image_prompt": None},
            ]},
            {"page": 3, "panels": [
                {"id": 5, "shot": "Dramatic irony, reveal to reader only",
                 "description": "Reveal to the reader only: the leak isn't a person — it's a compromised piece of hardware Rusty salvaged back in Issue 2.",
                 "narration": "The traitor had no face. It had a serial number.",
                 "dialogue": [], "image_prompt": None},
            ]},
            {"page": 4, "panels": [
                {"id": 6, "shot": "Urgent, unresolved",
                 "description": "Still fractured and suspicious of each other, the team gets a location ping on Zero — forced to move before resolving trust.",
                 "narration": None, "dialogue": [], "image_prompt": None},
            ]},
        ],
    },
    {
        "act": 2, "number": 9, "slug": "shadow-revealed", "title": "Shadow Revealed",
        "music_cue": "Full villain theme introduced for Shadow.",
        "pages": [
            {"page": 1, "panels": [
                {"id": 1, "shot": "Stealth infiltration",
                 "description": "Team infiltrates the facility holding Zero — tense, quiet, no full firefight yet.",
                 "narration": None, "dialogue": [], "image_prompt": None},
                {"id": 2, "shot": "Discovery, unsettling",
                 "description": "They find Zero alive but shaken, being interrogated not for information but as bait.",
                 "narration": None, "dialogue": [], "image_prompt": None},
            ]},
            {"page": 2, "panels": [
                {"id": 3, "shot": "Confrontation, close",
                 "description": "MSmaster confronts Anonymous face-to-face for the first time since the timeskip.",
                 "narration": None,
                 "dialogue": [{"speaker": "MSmaster", "line": "You wear the mask I gave you. Take it off and see what's actually underneath."}],
                 "image_prompt": None},
            ]},
            {"page": 3, "panels": [
                {"id": 4, "shot": "Grand reveal, distorted",
                 "description": "The true reveal: MSmaster is a lieutenant, not the leader. Shadow steps into view — voice distorted, face still unseen by design, but now an active on-page presence.",
                 "narration": None,
                 "dialogue": [{"speaker": "Shadow", "line": "Every hero needs an origin story. I'm simply the one who gets to write yours."}],
                 "image_prompt": None},
            ]},
            {"page": 4, "panels": [
                {"id": 5, "shot": "Extraction, chaotic",
                 "description": "Team extracts Zero but Shadow escapes clean. MSmaster is captured (writer's choice flagged, see production note).",
                 "narration": None, "dialogue": [], "image_prompt": None},
                {"id": 6, "shot": "Quiet, bitter",
                 "description": "Rusty finds the compromised hardware, realizes the mole was never a person.",
                 "narration": None, "dialogue": [], "image_prompt": None},
            ]},
        ],
    },

    # ---------------------------------------------------------------- ACT 3
    {
        "act": 3, "number": 10, "slug": "rules-of-engagement", "title": "Rules of Engagement",
        "music_cue": "Establishing theme for The Grid — abstract, geometric motif.",
        "pages": [
            {"page": 1, "panels": [
                {"id": 1, "shot": "Corporate introduction",
                 "description": "The Suit (Ron Sharon) is formally introduced into the main plot via his corporate cybersecurity role.",
                 "narration": None, "dialogue": [], "image_prompt": None},
                {"id": 2, "shot": "Countermeasure framing",
                 "description": "TrebleSmak folded in properly — his sound-based ability framed as a countermeasure against Shadow's tactics.",
                 "narration": None, "dialogue": [], "image_prompt": None},
            ]},
            {"page": 2, "panels": [
                {"id": 3, "shot": "Briefing, wide",
                 "description": "The team is briefed on 'The Grid' — part server-farm, part simulated reality, where the final confrontation will happen.",
                 "narration": None, "dialogue": [], "image_prompt": None},
                {"id": 4, "shot": "Stakes, serious",
                 "description": "Explain the stakes: dying in The Grid has real-world neurological consequences.",
                 "narration": None, "dialogue": [], "image_prompt": None},
            ]},
            {"page": 3, "panels": [
                {"id": 5, "shot": "Squad introduction",
                 "description": "Red Squad introduced properly — Captain H.A., Tib3rius, Alex Olsen — a parallel force, not yet allied.",
                 "narration": None, "dialogue": [], "image_prompt": None},
                {"id": 6, "shot": "Enemy display of force",
                 "description": "The Hadess Banshees dismantle a Red Squad probe effortlessly.",
                 "narration": None, "dialogue": [], "image_prompt": None},
            ]},
            {"page": 4, "panels": [
                {"id": 7, "shot": "Realization, resolve",
                 "description": "The team realizes they can't win alone — they need Red Squad, Mister MC's full team, and the Santos twins fully committed.",
                 "narration": None, "dialogue": [], "image_prompt": None},
            ]},
        ],
    },
    {
        "act": 3, "number": 11, "slug": "two-fronts", "title": "Two Fronts",
        "music_cue": "Parallel motifs for physical vs digital fronts, intercut.",
        "pages": [
            {"page": 1, "panels": [
                {"id": 1, "shot": "Physical-front prep",
                 "description": "Rusty and Red Squad prepare to assault The Syndicate's physical server facility.",
                 "narration": None, "dialogue": [], "image_prompt": None},
                {"id": 2, "shot": "Digital-front prep, abstract",
                 "description": "Anonymous, The Suit, and TrebleSmak prepare to enter The Grid directly.",
                 "narration": None, "dialogue": [], "image_prompt": None},
            ]},
            {"page": 2, "panels": [
                {"id": 3, "shot": "Quiet character beat",
                 "description": "Zero, still recovering from his capture, insists on joining despite the team's concerns.",
                 "narration": None, "dialogue": [], "image_prompt": None},
                {"id": 4, "shot": "Ambiguous commitment",
                 "description": "Blu Corbel makes his position semi-clear — he'll help, but only on his own terms.",
                 "narration": None,
                 "dialogue": [{"speaker": "Blu Corbel", "line": "I'm not here to be your hero. I'm here because Shadow owes me a debt older than any of you."}],
                 "image_prompt": None},
            ]},
            {"page": 3, "panels": [
                {"id": 5, "shot": "Assault begins",
                 "description": "Physical assault begins — Rusty and Red Squad breach the facility, met by hard resistance from the Hadess Banshees.",
                 "narration": None, "dialogue": [], "image_prompt": None},
                {"id": 6, "shot": "Style shift, geometric/abstract",
                 "description": "Digital entry begins — Anonymous and company enter The Grid, visual style shifting to abstract geometry.",
                 "narration": None, "dialogue": [], "image_prompt": None},
            ]},
            {"page": 4, "panels": [
                {"id": 7, "shot": "Cliffhanger, overwatch",
                 "description": "Mister MC and the Santos twins, providing overwatch, spot a second Syndicate strike team moving on an unguarded flank.",
                 "narration": None, "dialogue": [], "image_prompt": None},
            ]},
        ],
    },
    {
        "act": 3, "number": 12, "slug": "false-victory", "title": "False Victory",
        "music_cue": "Triumphant swell that curdles into dread by issue's end.",
        "pages": [
            {"page": 1, "panels": [
                {"id": 1, "shot": "Apparent win, physical",
                 "description": "Physical front looks won — Rusty's team clears the facility floor, Captain H.A. calls it early.",
                 "narration": None, "dialogue": [], "image_prompt": None},
                {"id": 2, "shot": "Apparent win, digital",
                 "description": "Digital front looks won — Anonymous corners what appears to be Shadow's core node in The Grid.",
                 "narration": None, "dialogue": [], "image_prompt": None},
            ]},
            {"page": 2, "panels": [
                {"id": 3, "shot": "Twist reveal",
                 "description": "It's a decoy — both wins were traps designed to pin the team down while a second strike team hits the real-world base.",
                 "narration": None, "dialogue": [], "image_prompt": None},
                {"id": 4, "shot": "Outnumbered stand",
                 "description": "Mister MC and the Santos twins engage the strike team alone, outnumbered, no backup available.",
                 "narration": None, "dialogue": [], "image_prompt": None},
            ]},
            {"page": 3, "panels": [
                {"id": 5, "shot": "Brutal, costly",
                 "description": "Iris Santos is badly injured protecting Joas; Mister MC is pushed to the edge of his Magna Cyber abilities.",
                 "narration": None, "dialogue": [], "image_prompt": None},
                {"id": 6, "shot": "Scramble",
                 "description": "The rest of the team realizes the trap too late and scrambles to redeploy.",
                 "narration": None, "dialogue": [], "image_prompt": None},
            ]},
            {"page": 4, "panels": [
                {"id": 7, "shot": "Grim aftermath",
                 "description": "The base holds, barely, but the cost is visible.",
                 "narration": "They had called it a victory. Shadow had simply let them believe it.",
                 "dialogue": [], "image_prompt": None},
            ]},
        ],
    },
    {
        "act": 3, "number": 13, "slug": "the-ultimate-showdown", "title": "The Ultimate Showdown",
        "music_cue": "Full ensemble theme, physical and digital motifs merge.",
        "pages": [
            {"page": 1, "panels": [
                {"id": 1, "shot": "Regrouping, resolve",
                 "description": "Regrouped and reeling, the team learns Shadow's actual location from Blu Corbel, who finally commits fully to the fight.",
                 "narration": None, "dialogue": [], "image_prompt": None},
                {"id": 2, "shot": "Full team assembled, wide",
                 "description": "Full team assembled for the first time — every named hero present, Iris wounded but standing.",
                 "narration": None, "dialogue": [], "image_prompt": None},
            ]},
            {"page": 2, "panels": [
                {"id": 3, "shot": "Intercut, rapid",
                 "description": "The real confrontation begins — split across physical and digital fronts simultaneously, cutting rapidly.",
                 "narration": None, "dialogue": [], "image_prompt": None},
                {"id": 4, "shot": "Reveal, mid-battle",
                 "description": "Shadow finally unmasked mid-battle — a betrayed former ally of The Hat's, with personal history not yet shown to the reader.",
                 "narration": None, "dialogue": [], "image_prompt": None},
            ]},
            {"page": 3, "panels": [
                {"id": 5, "shot": "Digital decisive blow",
                 "description": "TrebleSmak's Death-Note attack disables The Grid's core systems; The Suit's quarantine cannon seals Shadow's digital escape routes.",
                 "narration": None, "dialogue": [], "image_prompt": None},
                {"id": 6, "shot": "Physical decisive blow",
                 "description": "Rusty and Red Squad hold off the Hadess Banshees long enough for Mister MC to land the decisive blow.",
                 "narration": None, "dialogue": [], "image_prompt": None},
            ]},
            {"page": 4, "panels": [
                {"id": 7, "shot": "Defeat, not death",
                 "description": "Shadow defeated — not killed, but broken and captured, echoing MSmaster's earlier fate.",
                 "narration": None, "dialogue": [], "image_prompt": None},
                {"id": 8, "shot": "Quiet unity, final",
                 "description": "The team, battered, stands together for the first time as something more than allies.",
                 "narration": "It was not the ending of a war. It was the beginning of trust.",
                 "dialogue": [], "image_prompt": None},
            ]},
        ],
    },

    # ---------------------------------------------------------------- ACT 4
    {
        "act": 4, "number": 14, "slug": "the-cost", "title": "The Cost",
        "music_cue": "Sparse, reflective piano over ambient synth bed.",
        "pages": [
            {"page": 1, "panels": [
                {"id": 1, "shot": "Recovery, honest",
                 "description": "Aftermath — recovery scenes. Iris Santos's injury has lasting consequences, addressed honestly.",
                 "narration": None, "dialogue": [], "image_prompt": None},
                {"id": 2, "shot": "Prison, ambiguous",
                 "description": "MSmaster, still imprisoned, given a small redemptive or tragic beat (writer's choice).",
                 "narration": None, "dialogue": [], "image_prompt": None},
            ]},
            {"page": 2, "panels": [
                {"id": 3, "shot": "Reflective two-shot",
                 "description": "Blu Corbel's ambiguous status addressed directly — neither fully joining nor disappearing.",
                 "narration": None,
                 "dialogue": [{"speaker": "The Hat", "line": "Some doors you leave open. Not because you trust what's on the other side. Because closing it costs more."}],
                 "image_prompt": None},
            ]},
            {"page": 3, "panels": [
                {"id": 4, "shot": "Quiet scattering",
                 "description": "The team disbands temporarily to heal — a quiet, human scattering, not a triumph montage.",
                 "narration": None, "dialogue": [], "image_prompt": None},
            ]},
            {"page": 4, "panels": [
                {"id": 5, "shot": "Visual callback to Issue 1",
                 "description": "Anonymous, alone again as in Issue 1, reflects on how much has changed.",
                 "narration": None, "dialogue": [], "image_prompt": None},
            ]},
        ],
    },
    {
        "act": 4, "number": 15, "slug": "new-tide", "title": "New Tide",
        "music_cue": "New villain motif for ComShark — fluid, aquatic-digital texture.",
        "pages": [
            {"page": 1, "panels": [
                {"id": 1, "shot": "Concrete inciting incident",
                 "description": "Introduce Gabrielle/ComShark via a specific breach at a facility connected to The Suit's corporate world.",
                 "narration": None, "dialogue": [], "image_prompt": None},
                {"id": 2, "shot": "Power showcase",
                 "description": "Establish ComShark's power set visually — digital-physical hybrid, 'swimming' through networked infrastructure.",
                 "narration": None, "dialogue": [], "image_prompt": None},
            ]},
            {"page": 2, "panels": [
                {"id": 3, "shot": "Reconnection",
                 "description": "The Suit notices the pattern and flags it to Anonymous, tentatively reforming contact between separated team members.",
                 "narration": None, "dialogue": [], "image_prompt": None},
                {"id": 4, "shot": "Motive tease",
                 "description": "ComShark's motive teased but not resolved — personal, not purely villainous.",
                 "narration": None, "dialogue": [], "image_prompt": None},
            ]},
            {"page": 3, "panels": [
                {"id": 5, "shot": "Organic regathering",
                 "description": "Small team elements begin reconvening organically, drawn back by the new threat rather than forced.",
                 "narration": None, "dialogue": [], "image_prompt": None},
            ]},
            {"page": 4, "panels": [
                {"id": 6, "shot": "Cliffhanger, ominous",
                 "description": "ComShark makes contact with someone from The Syndicate's remnants — implying the threats aren't fully separate.",
                 "narration": None, "dialogue": [], "image_prompt": None},
            ]},
        ],
    },
    {
        "act": 4, "number": 16, "slug": "a-better-tomorrow", "title": "A Better Tomorrow",
        "music_cue": "Full team theme reprise layered with Anonymous's Issue-1 motif — bookend.",
        "pages": [
            {"page": 1, "panels": [
                {"id": 1, "shot": "Formalization, wide",
                 "description": "Full team reconvenes, scars and all, formalizing what they've been informally — TMHP's playground named in-story for the first time.",
                 "narration": None, "dialogue": [], "image_prompt": None},
                {"id": 2, "shot": "Changed but unbroken",
                 "description": "Iris Santos returns changed but unbroken — a new role within the team reflecting her injury.",
                 "narration": None, "dialogue": [], "image_prompt": None},
            ]},
            {"page": 2, "panels": [
                {"id": 3, "shot": "Mirrored exchange",
                 "description": "Blu Corbel's final scene — still unaligned, but a moment of mutual respect with Anonymous, mirroring Issue 5.",
                 "narration": None, "dialogue": [], "image_prompt": None},
                {"id": 4, "shot": "Resolution, flexible",
                 "description": "MSmaster's fate resolved (redemption, escape, or ruin — final call left to writer's room).",
                 "narration": None, "dialogue": [], "image_prompt": None},
            ]},
            {"page": 3, "panels": [
                {"id": 5, "shot": "Sequel hook",
                 "description": "The team formally takes on the ComShark case as their next mission.",
                 "narration": None, "dialogue": [], "image_prompt": None},
            ]},
            {"page": 4, "panels": [
                {"id": 6, "shot": "Mirrored wide shot, final",
                 "description": "Closing wide shot mirroring Issue 1's opening alley — same location, transformed, team walking into the light.",
                 "narration": "They were never meant to be heroes. They simply refused to be nothing.",
                 "dialogue": [], "image_prompt": None},
                {"id": 7, "shot": "End card",
                 "description": "End card.",
                 "narration": None,
                 "dialogue": [{"speaker": "Text", "line": "ANONYMOUS HEROES will return."}],
                 "image_prompt": None},
            ]},
        ],
    },
]
