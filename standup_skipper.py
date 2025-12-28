#!/usr/bin/env python3
"""
Standup Skipper - Because your cat's nap schedule is more important than status updates.
"""

import random
import sys
import time
from datetime import datetime

# Pre-canned excuses that sound more productive than "I was debugging my life"
EXCUSES = [
    "Deep in the rabbit hole of optimization",
    "Battling a particularly stubborn race condition",
    "Refactoring my refactor",
    "In a heated debate with the linter",
    "Documenting why we don't need documentation",
    "Waiting for CI/CD to finish contemplating its existence",
    "Investigating why it works on my machine",
    "Attending a meeting about reducing meetings",
]

# Magical progress percentages that sound specific but mean nothing
PROGRESS = ["70%", "85%", "90%", "95%", "99%", "almost done", "blocked on something trivial"]


def generate_update():
    """Generates a standup update that sounds productive but reveals nothing."""
    yesterday = random.choice([
        f"Worked on {random.choice(['the thing', 'that ticket', 'the backend'])}",
        f"Continued {random.choice(['refactoring', 'optimizing', 'investigating'])} {random.choice(['code', 'performance', 'the issue'])}",
        "Mostly meetings, but also some coding",
    ])
    
    today = random.choice([
        f"Finishing {random.choice(['the rest', 'that last bit', 'the implementation'])}",
        f"{random.choice(['Testing', 'Debugging', 'Polishing'])} {random.choice(['the feature', 'my code', 'everything'])}",
        "More of the same, but with renewed existential dread",
    ])
    
    blockers = random.choice([
        "None, unless you count my will to live",
        f"{random.choice(EXCUSES)}",
        "Waiting on someone who's probably in another standup",
        "",  # Sometimes no blockers is the most believable option
    ])
    
    return {
        "yesterday": yesterday,
        "today": today,
        "blockers": blockers,
        "progress": random.choice(PROGRESS),
    }


def main():
    """The main event - where productivity theater meets copy-paste magic."""
    print("\n🚀 STANDUP SKIPPER - Your Ticket to Pseudo-Productivity\n")
    print(f"Generated at: {datetime.now().strftime('%H:%M')} (standup o'clock)\n")
    
    update = generate_update()
    
    print("📋 YESTERDAY:")
    print(f"  {update['yesterday']}")
    print()
    
    print("🎯 TODAY:")
    print(f"  {update['today']} ({update['progress']})")
    print()
    
    if update['blockers']:
        print("🚧 BLOCKERS:")
        print(f"  {update['blockers']}")
    else:
        print("✅ No blockers (except existential ones)")
    
    print("\n✨ Copy-paste this and get back to actual work!")
    print("   (Or just say 'same as yesterday' - they won't remember)")
    
    # Simulate the time you just saved
    time.sleep(0.5)
    print("\n⏱️  Estimated time saved: 5-15 minutes of your life")
    
    return 0


if __name__ == "__main__":
    sys.exit(main())
