import random, os
from datetime import datetime

SITE = "https://chasematthews178.github.io"
TOOLS = [
    {"name":"Jasper AI","price":"$39/mo","anchor":"jasper","hook":"I was most skeptical about Jasper. Now it's the tool I use most.","stat":"Content that took 3 hours now takes 40 minutes.","caveat":"Learning curve is real. Give it a week before judging it.","who":"Anyone publishing more than 4 pieces of content per month."},
    {"name":"Notion AI","price":"$10/mo","anchor":"notion","hook":"The most obvious $10 you'll spend if you already use Notion.","stat":"I save 20 minutes a day just from the Q&A feature alone.","caveat":"Only useful if you actually use Notion.","who":"Anyone drowning in notes, docs, and client information."},
    {"name":"Canva Magic","price":"Free","anchor":"canva","hook":"I stopped paying a $500/month designer. Canva replaced them.","stat":"Professional graphics in minutes. Zero design experience needed.","caveat":"Less control than Adobe. But 90% of businesses don't need that control.","who":"Any business that needs regular visual content."},
    {"name":"Semrush","price":"$139/mo","anchor":"semrush","hook":"I almost cancelled Semrush three times. Then one article earned $400/month.","stat":"That article has been running 8 months. Tool paid for itself 22 times over.","caveat":"Only worth it if SEO is how you get clients.","who":"Businesses where search traffic drives leads."},
    {"name":"Tidio","price":"Free","anchor":"tidio","hook":"Set it up expecting 30% automation. It handled 68% in month one.","stat":"Client went from 4 hours of daily support to 45 minutes.","caveat":"Only for businesses with high support volume.","who":"E-commerce stores getting 50+ support tickets per week."},
    {"name":"Zapier","price":"Free","anchor":"zapier","hook":"The tool I underestimated longest. It quietly saves 30 minutes every day.","stat":"8 manual steps — zero. Form fills, tasks create, emails send. Automatic.","caveat":"Complex zaps sometimes break. Keep them simple to start.","who":"Anyone doing repetitive tasks between apps — which is everyone."},
    {"name":"Kit","price":"Free to 1k subs","anchor":"kit","hook":"Built a 7-email sequence one afternoon. It's run untouched for 14 months.","stat":"Email ROI: $42 back for every $1 spent. Kit is free to start.","caveat":"Pricier than Mailchimp at large list sizes.","who":"Any creator or consultant building an audience."},
]
IG = [
    "{hook} 📱\n\n{stat}\n\n{caveat}\n\nFull honest review — link in bio 👆\n\n#AItools #SmallBusiness #Productivity #BusinessTools #Entrepreneur #WorkSmart #AIForBusiness #SmallBusinessOwner #BusinessAutomation #SideHustle",
    "I tested 23 AI tools and spent $2,400. Honest truth about {name} 👇\n\n{stat}\n\n{caveat}\n\nWho should buy it: {who}\n\nFull ranking — link in bio 🔗\n\n#AItools #SmallBusiness #BusinessTools #Productivity #Entrepreneur #WorkSmart #BusinessGrowth #MarketingTools #AIForBusiness #SmallBusinessOwner",
    "{name} ({price}) — my honest take after 90 days ✍️\n\n{hook}\n\n{stat}\n\nThe caveat nobody mentions: {caveat}\n\nLink in bio 👆\n\n#AItools #SmallBusiness #Entrepreneur #BusinessTools #Productivity #HonestReview #WorkSmart #AIForBusiness #BusinessAutomation #StartupLife",
]
IG_GENERAL = [
    "Spent $2,400 testing AI tools so you don't have to 🧪\n\nWhat I kept after 90 days:\n\n→ Jasper AI ($39/mo) — writes my content drafts\n→ Notion AI ($10/mo) — answers questions about my notes instantly\n→ Canva Magic (free) — replaced my $500/month designer\n→ Zapier (free) — kills 30 minutes of daily busywork\n→ Kit (free) — email automation that runs while I sleep\n\nThe other 16 tools? Cancelled every single one.\n\nFull honest reviews — link in bio 👆\n\n#AItools #SmallBusiness #BusinessTools #Productivity #Entrepreneur #WorkSmart #AIForBusiness #BusinessAutomation #SideHustle #PassiveIncome",
    "The $0 AI stack that runs a real business 💡\n\n✅ Canva (free) — professional graphics in minutes\n✅ Zapier (free) — connects your apps, kills manual tasks\n✅ Kit (free to 1,000 subscribers) — email automation that converts\n\nTotal monthly cost: $0\n\nI ran this stack for 4 months before paying for anything.\n\nLink in bio 🔗\n\n#FreeTools #AItools #SmallBusiness #Entrepreneur #BusinessTips #StartupLife #Productivity #OnlineBusiness #PassiveIncome #WorkFromHome",
    "Quick math 🔢\n\n8 hrs/week on content writing → AI cuts 65% = 5 hours back\n4 hrs/week on design → Canva cuts 70% = 3 hours back\n\nThat's 8 hours a week recovered.\nAt $50/hr = $1,600/month in time value.\n\nTools cost under $50/month combined.\n\nFree calculator on my site — link in bio 👆\n\n#Productivity #AItools #TimeManagement #SmallBusiness #WorkSmart #BusinessAutomation #ROI #Entrepreneur #BusinessGrowth #WorkLifeBalance",
]
TW = [
    "{hook}\n\n{stat}\n\nFull honest review: {site}/#{anchor}",
    "Hot take on {name}:\n\n{caveat}\n\nBut also: {stat}\n\nWorth it for: {who}\n\n{site}/#{anchor}",
    "I spent $2,400 testing AI tools.\n\nHonest truth about {name}: {hook}\n\nFull ranking: {site}",
    "{stat}\n\nThat's {name} ({price}).\n\nFull review: {site}/#{anchor}",
]
TW_GENERAL = [
    f"I tested 23 AI tools. Spent $2,400. Cancelled 16.\n\nThe 7 I kept — ranked honestly:\n{SITE}",
    f"Hot take: the best AI stack for small businesses costs $0.\n\nCanva + Zapier + Kit = complete system.\n\nFull breakdown:\n{SITE}",
    f"Most AI tools are embarrassingly bad.\n\nNot 'could be better' bad.\n\n'I can't believe they charge for this' bad.\n\nThe 7 that aren't:\n{SITE}",
]
LI = [
    "{hook}\n\nHere's the full story.\n\nOver 90 days I tested 23 AI tools with real client work — not demos, not trials.\n\n{name} was the one that surprised me most.\n\n{stat}\n\nThe honest caveat: {caveat}\n\nWho it makes sense for: {who}\n\nFull review with everything that worked and didn't — link in comments 👇\n\n#SmallBusiness #AItools #Productivity #BusinessTools #Entrepreneur #MarketingTools",
    "The question I get asked most: is {name} actually worth it?\n\nHonest answer: depends entirely on what you do.\n\n{stat}\n\nBut here's what nobody tells you: {caveat}\n\nIf you match this profile — {who} — it's probably worth trying.\n\nIf you don't, save your money.\n\nFull breakdown in the link below.\n\n#SmallBusiness #BusinessTools #AItools #Entrepreneur #Productivity #HonestAdvice",
]
TT = [
    '[HOOK]\n"{hook}"\n\n[POINT 1]\n"Here\'s what I mean. {stat}"\n\n[POINT 2]\n"The honest part nobody mentions: {caveat}"\n\n[WHO IT\'S FOR]\n"This is specifically for: {who}"\n\n[CTA]\n"Full review at the link in my bio. All 7 tools I kept after 90 days of testing."',
    '[HOOK]\n"I tested 23 AI tools. Here\'s the truth about {name}."\n\n[SETUP]\n"{hook}"\n\n[THE RESULT]\n"{stat}"\n\n[HONEST TAKE]\n"{caveat}"\n\n[CTA]\n"Full ranking at the link in my bio — including what annoyed me about every single one."',
]

def generate_week(week_num):
    t = TOOLS[week_num % len(TOOLS)]
    t2 = TOOLS[(week_num + 3) % len(TOOLS)]
    fmt = lambda tmpl, tool: tmpl.format(name=tool["name"],price=tool["price"],anchor=tool["anchor"],hook=tool["hook"],stat=tool["stat"],caveat=tool["caveat"],who=tool["who"],site=SITE)
    return (fmt(random.choice(IG),t), random.choice(IG_GENERAL), fmt(random.choice(TW),t), random.choice(TW_GENERAL), fmt(random.choice(TW),t2), fmt(random.choice(LI),t), fmt(random.choice(TT),t))

def main():
    now = datetime.utcnow()
    week_label = now.strftime("%Y-W%V")
    ig1,ig2,tw1,tw2,tw3,li,tt = generate_week(int(now.strftime("%V")))
    lines = [f"# Social Posts — {week_label}",f"*Generated {now.strftime('%Y-%m-%d')} · {SITE}*","","---","",
        "## 📸 INSTAGRAM","","### Post 1 — Monday 6pm","```",ig1,"```","",
        "### Post 2 — Thursday 6pm","```",ig2,"```","","---","",
        "## 🐦 TWITTER / X","","### Post 1 — Tuesday 10am","```",tw1,"```","",
        "### Post 2 — Wednesday 12pm","```",tw2,"```","",
        "### Post 3 — Friday 10am","```",tw3,"```","","---","",
        "## 🔵 LINKEDIN","","### Post — Wednesday 9am","```",li,"```","","---","",
        "## 🎵 TIKTOK SCRIPT","","### Script — Film Wednesday or Thursday","```",tt,"```","","---","",
        "## ✅ Checklist",
        "- [ ] Instagram Post 1 — Monday 6pm","- [ ] Twitter Post 1 — Tuesday 10am",
        "- [ ] LinkedIn — Wednesday 9am","- [ ] TikTok — Wednesday or Thursday",
        "- [ ] Twitter Post 2 — Wednesday 12pm","- [ ] Instagram Post 2 — Thursday 6pm",
        "- [ ] Twitter Post 3 — Friday 10am","",
        "*Auto-generated — no API key needed.*"]
    os.makedirs("social-posts",exist_ok=True)
    path = f"social-posts/{week_label}.md"
    with open(path,"w") as f: f.write("\n".join(lines))
    print(f"✓ Generated {path}")

if __name__ == "__main__":
    main()
