import random
import os
from datetime import datetime

SITE = "https://chasematthews178.github.io"

TOOLS = [
    {"name": "Jasper AI", "price": "$39/mo", "anchor": "jasper", "badge": "Editor's Pick",
     "hook": "I was most skeptical about Jasper. Now it's the tool I use most.",
     "stat": "Content that took 3 hours now takes 40 minutes.",
     "caveat": "Learning curve is real. Give it a week before judging it.",
     "who": "Anyone publishing more than 4 pieces of content per month."},
    {"name": "Notion AI", "price": "$10/mo", "anchor": "notion", "badge": "Best Value",
     "hook": "The most obvious $10 you'll spend if you already use Notion.",
     "stat": "I save 20 minutes a day just from the Q&A feature alone.",
     "caveat": "Only useful if you actually use Notion.",
     "who": "Anyone drowning in notes, docs, and client information."},
    {"name": "Canva Magic", "price": "Free", "anchor": "canva", "badge": "Free Tier",
     "hook": "I stopped paying a $500/month designer. Canva replaced them.",
     "stat": "Professional graphics in minutes. Zero design experience needed.",
     "caveat": "Less control than Adobe. But 90% of businesses don't need that control.",
     "who": "Any business that needs regular visual content."},
    {"name": "Semrush", "price": "$139/mo", "anchor": "semrush", "badge": "Highest ROI",
     "hook": "I almost cancelled Semrush three times. Then one article earned $400/month.",
     "stat": "That article has been running 8 months. Tool paid for itself 22 times over.",
     "caveat": "Only worth it if SEO is how you get clients.",
     "who": "Businesses where search traffic drives leads."},
    {"name": "Tidio", "price": "Free", "anchor": "tidio", "badge": "E-Commerce",
     "hook": "Set it up expecting 30% automation. It handled 68% in month one.",
     "stat": "Client went from 4 hours of daily support to 45 minutes.",
     "caveat": "Only for businesses with high support volume.",
     "who": "E-commerce stores getting 50+ support tickets per week."},
    {"name": "Zapier", "price": "Free", "anchor": "zapier", "badge": "Automation",
     "hook": "The tool I underestimated longest. It quietly saves 30 minutes every day.",
     "stat": "8 manual steps → zero. Form fills, tasks create, emails send. Automatic.",
     "caveat": "Complex zaps sometimes break. Keep them simple to start.",
     "who": "Anyone doing repetitive tasks between apps — which is everyone."},
    {"name": "Kit", "price": "Free to 1k subs", "anchor": "kit", "badge": "Email Marketing",
     "hook": "Built a 7-email sequence one afternoon. It's run untouched for 14 months.",
     "stat": "Email ROI: $42 back for every $1 spent. Kit is free to start.",
     "caveat": "Pricier than Mailchimp at large list sizes.",
     "who": "Any creator or consultant building an audience."},
]

INSTAGRAM_TEMPLATES = [
    """{hook} 📱

{stat}

{caveat}

Full honest review at the link in my bio 👆

#AItools #SmallBusiness #Productivity #BusinessTools #Entrepreneur #WorkSmart #AIForBusiness #SmallBusinessOwner #BusinessAutomation #SideHustle""",

    """I tested 23 AI tools and spent $2,400. Here's the honest truth about {name} 👇

{stat}

{caveat}

Who should buy it: {who}

Full ranking of all 7 tools I kept — link in bio 🔗

#AItools #SmallBusiness #BusinessTools #Productivity #Entrepreneur #WorkSmart #BusinessGrowth #MarketingTools #AIForBusiness #SmallBusinessOwner""",

    """{name} ({price}) — my honest take after 90 days ✍️

{hook}

{stat}

The caveat nobody mentions: {caveat}

See the full breakdown at the link in my bio 👆

#AItools #SmallBusiness #Entrepreneur #BusinessTools #Productivity #HonestReview #WorkSmart #AIForBusiness #BusinessAutomation #StartupLife""",
]

TWITTER_TEMPLATES = [
    "{hook}\n\n{stat}\n\nFull honest review: {site}/#{anchor}",
    "Hot take on {name}:\n\n{caveat}\n\nBut also: {stat}\n\nWorth it for the right person: {site}/#{anchor}",
    "I spent $2,400 testing AI tools.\n\nThe honest truth about {name}: {hook}\n\nFull ranking: {site}",
    "{stat}\n\nThat's {name} ({price}).\n\nFull review: {site}/#{anchor}",
]

LINKEDIN_TEMPLATES = [
    """{hook}

Here's the full story.

Over 90 days I tested 23 AI tools with real client work — not demos, not trials. Actual production.

{name} was the one that surprised me most.

{stat}

The honest caveat I always give people: {caveat}

Who it actually makes sense for: {who}

I wrote up the full review with everything that worked, everything that didn't, and exactly who should and shouldn't buy it.

Link in comments 👇

#SmallBusiness #AItools #Productivity #BusinessTools #Entrepreneur #MarketingTools""",

    """The question I get asked most: is {name} actually worth it?

Honest answer: depends entirely on what you do.

{stat}

But here's the thing nobody tells you: {caveat}

If you match this profile — {who} — it's probably worth trying.

If you don't, save your money.

Full breakdown in the link below.

#SmallBusiness #BusinessTools #AItools #Entrepreneur #Productivity #HonestAdvice""",
]

TIKTOK_TEMPLATES = [
    """[HOOK]
"{hook}"

[POINT 1]
"Here's what I mean. {stat}"

[POINT 2]
"The honest part nobody mentions: {caveat}"

[WHO IT'S FOR]
"This is specifically for: {who}"

[CTA]
"Full review at the link in my bio. I ranked all 7 tools I kept after 90 days of testing."
""",
    """[HOOK]
"I tested 23 AI tools. Here's the truth about {name}."

[SETUP]
"{hook}"

[THE RESULT]
"{stat}"

[HONEST TAKE]
"{caveat}"

[CTA]
"Full ranking at the link in my bio — including what annoyed me about every single one."
""",
]

GENERAL_INSTAGRAM = [
    """Spent $2,400 testing AI tools so you don't have to 🧪

Here's what I actually kept after 90 days:

→ Jasper AI ($39/mo) — writes my content drafts
→ Notion AI ($10/mo) — answers questions about my client notes instantly  
→ Canva Magic (free) — replaced my $500/month designer
→ Zapier (free) — kills 30 minutes of daily busywork
→ Kit (free) — email automation that runs while I sleep

The other 16 tools? Cancelled every single one.

Full honest reviews — link in bio 👆

#AItools #SmallBusiness #BusinessTools #Productivity #Entrepreneur #WorkSmart #AIForBusiness #BusinessAutomation #SideHustle #PassiveIncome""",

    """The $0 AI stack that runs a real business 💡

✅ Canva (free) — professional graphics in minutes
✅ Zapier (free) — connects your apps, kills manual tasks  
✅ Kit (free to 1,000 subscribers) — email automation that converts

Total monthly cost: $0

I ran this exact stack for 4 months before I paid for anything.

Full breakdown at link in bio 🔗

#FreeTools #AItools #SmallBusiness #Entrepreneur #BusinessTips #StartupLife #Productivity #OnlineBusiness #PassiveIncome #WorkFromHome""",

    """Quick math that changed how I think about AI tools 🔢

8 hrs/week on content writing
→ AI cuts that by 65% = 5 hours back per week

4 hrs/week on design work  
→ Canva cuts that by 70% = 3 hours back per week

That's 8 hours a week recovered.
At $50/hour = $1,600/month in time value.

Tools to do it cost under $50/month combined.

Free calculator on my site — link in bio 👆

#Productivity #AItools #TimeManagement #SmallBusiness #WorkSmart #BusinessAutomation #ROI #Entrepreneur #BusinessGrowth #WorkLifeBalance""",
]

GENERAL_TWITTER = [
    f"I tested 23 AI tools. Spent $2,400. Cancelled 16.\n\nThe 7 I kept are ranked here with full honest reviews:\n{SITE}",
    f"Hot take: the best AI stack for small businesses costs $0.\n\nCanva + Zapier + Kit = complete marketing and automation system.\n\nFree. Forever:\n{SITE}",
    f"Most AI tools are genuinely embarrassingly bad.\n\nNot 'could be better' bad.\n\n'I can't believe they're charging for this' bad.\n\nThe 7 that aren't:\n{SITE}",
]


def generate_week(week_num):
    tool = TOOLS[week_num % len(TOOLS)]
    gen_tool = TOOLS[(week_num + 3) % len(TOOLS)]

    ig1 = random.choice(INSTAGRAM_TEMPLATES).format(
        name=tool["name"], price=tool["price"], anchor=tool["anchor"],
        hook=tool["hook"], stat=tool["stat"], caveat=tool["caveat"],
        who=tool["who"], site=SITE
    )
    ig2 = random.choice(GENERAL_INSTAGRAM)
    tw1 = random.choice(TWITTER_TEMPLATES).format(
        name=tool["name"], price=tool["price"], anchor=tool["anchor"],
        hook=tool["hook"], stat=tool["stat"], caveat=tool["caveat"],
        who=tool["who"], site=SITE
    )
    tw2 = random.choice(GENERAL_TWITTER)
    tw3 = random.choice(TWITTER_TEMPLATES).format(
        name=gen_tool["name"], price=gen_tool["price"], anchor=gen_tool["anchor"],
        hook=gen_tool["hook"], stat=gen_tool["stat"], caveat=gen_tool["caveat"],
        who=gen_tool["who"], site=SITE
    )
    li = random.choice(LINKEDIN_TEMPLATES).format(
        name=tool["name"], price=tool["price"], anchor=tool["anchor"],
        hook=tool["hook"], stat=tool["stat"], caveat=tool["caveat"],
        who=tool["who"], site=SITE
    )
    tt = random.choice(TIKTOK_TEMPLATES).format(
        name=tool["name"], price=tool["price"], anchor=tool["anchor"],
        hook=tool["hook"], stat=tool["stat"], caveat=tool["caveat"],
        who=tool["who"], site=SITE
    )

    return ig1, ig2, tw1, tw2, tw3, li, tt


def main():
    now = datetime.utcnow()
    week_label = now.strftime("%Y-W%V")
    week_num = int(now.strftime("%V"))

    ig1, ig2, tw1, tw2, tw3, li, tt = generate_week(week_num)

    lines = [
        f"# Social Posts — {week_label}",
        f"*Generated {now.strftime('%Y-%m-%d')} · Site: {SITE}*",
        "", "---", "",
        "## 📸 INSTAGRAM", "",
        "### Post 1 — Schedule: Monday 6pm",
        "```", ig1, "```", "",
        "### Post 2 — Schedule: Thursday 6pm",
        "```", ig2, "```", "",
        "---", "",
        "## 🐦 TWITTER / X", "",
        "### Post 1 — Schedule: Tuesday 10am",
        "```", tw1, "```", "",
        "### Post 2 — Schedule: Wednesday 12pm",
        "```", tw2, "```", "",
        "### Post 3 — Schedule: Friday 10am",
        "```", tw3, "```", "",
        "---", "",
        "## 🔵 LINKEDIN", "",
        "### Post — Schedule: Wednesday 9am",
        "```", li, "```", "",
        "---", "",
        "## 🎵 TIKTOK SCRIPT", "",
        "### Script — Film Wednesday or Thursday",
        "```", tt, "```", "",
        "---", "",
        "## ✅ Checklist",
        "- [ ] Instagram Post 1 — Monday 6pm",
        "- [ ] Twitter Post 1 — Tuesday 10am",
        "- [ ] LinkedIn — Wednesday 9am",
        "- [ ] TikTok — Wednesday or Thursday",
        "- [ ] Twitter Post 2 — Wednesday 12pm",
        "- [ ] Instagram Post 2 — Thursday 6pm",
        "- [ ] Twitter Post 3 — Friday 10am",
        "",
        "*Generated automatically — no API key needed.*"
    ]

    os.makedirs("social-posts", exist_ok=True)
    path = f"social-posts/{week_label}.md"
    with open(path, "w") as f:
        f.write("\n".join(lines))
    print(f"✓ Generated {path}")


if __name__ == "__main__":
    main()
