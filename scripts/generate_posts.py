"""
generate_posts.py
Generates a full week of social media posts for chasematthews178.github.io
using the Claude API. Saves output to social-posts/YYYY-WW.md
Run via GitHub Actions every Monday, or manually anytime.
"""

import anthropic
import os
import json
from datetime import datetime, timedelta

client = anthropic.Anthropic(api_key=os.environ["ANTHROPIC_API_KEY"])

# ── SITE CONTEXT ────────────────────────────────────────────────────────────────
SITE_URL = "https://chasematthews178.github.io"

TOOLS = [
    {
        "name": "Jasper AI",
        "price": "$39/mo",
        "rating": "4.8/5",
        "badge": "Editor's Pick",
        "best_for": "Marketing copy and content writing",
        "honest_take": "Learning curve is real but it's the single biggest time-saver once fluent",
        "who_should_buy": "Businesses publishing more than 4 pieces of content per month",
        "anchor": "#jasper"
    },
    {
        "name": "Notion AI",
        "price": "$10/mo add-on",
        "rating": "4.6/5",
        "badge": "Best Value",
        "best_for": "Ops, docs, and knowledge management",
        "honest_take": "The only tool I'd recommend to someone who's unsure about AI tools",
        "who_should_buy": "Anyone already using Notion",
        "anchor": "#notion"
    },
    {
        "name": "Canva Magic Suite",
        "price": "Free / $15/mo Pro",
        "rating": "4.7/5",
        "badge": "Free Tier",
        "best_for": "Visual content creation without design experience",
        "honest_take": "I replaced a $500/month part-time designer with this",
        "who_should_buy": "Any business that needs regular visual content",
        "anchor": "#canva"
    },
    {
        "name": "Semrush",
        "price": "from $139/mo",
        "rating": "4.5/5",
        "badge": "Highest ROI",
        "best_for": "SEO and search-driven growth",
        "honest_take": "One article written with Semrush research earns ~$400/mo in referrals",
        "who_should_buy": "Businesses where search traffic drives leads — skip it otherwise",
        "anchor": "#semrush"
    },
    {
        "name": "Tidio",
        "price": "Free / $29/mo Pro",
        "rating": "4.4/5",
        "badge": "E-Commerce",
        "best_for": "Customer support automation for e-commerce",
        "honest_take": "It handled 68% of support tickets automatically in the first month for one client",
        "who_should_buy": "E-commerce businesses getting 50+ support tickets/week",
        "anchor": "#tidio"
    },
    {
        "name": "Zapier",
        "price": "Free / $20/mo Pro",
        "rating": "4.8/5",
        "badge": "Automation",
        "best_for": "Connecting apps and eliminating manual tasks",
        "honest_take": "It quietly eliminates 20-30 minutes of manual tasks every single day",
        "who_should_buy": "Anyone doing repetitive tasks between apps — everyone qualifies",
        "anchor": "#zapier"
    },
    {
        "name": "Kit (ConvertKit)",
        "price": "Free to 1,000 subscribers",
        "rating": "4.5/5",
        "badge": "Email Marketing",
        "best_for": "Email list building and automation",
        "honest_take": "Built a 7-email sequence in one afternoon that's been running untouched for 14 months",
        "who_should_buy": "Any content creator or consultant building an audience",
        "anchor": "#kit"
    }
]

AUTHOR_VOICE = """
Elias Mercer — voice guidelines:
- Direct, honest, occasionally blunt
- Specific numbers and real examples, not vague claims
- Anti-hype: willing to say something isn't worth it
- Conversational but not casual — informative with personality
- First person, personal experience
- Never salesy — the honesty IS the marketing
- Short punchy sentences mixed with longer explanatory ones
- Uses em-dashes and parentheticals naturally
"""

# ── PLATFORM PROMPTS ─────────────────────────────────────────────────────────────
PLATFORMS = {
    "linkedin": {
        "description": "LinkedIn long-form post (150-300 words). Professional but personal. Hook in line 1. Story structure. End with a question or CTA. No hashtags in body — put 3-5 relevant ones at the very end separated by a line break.",
        "count": 2
    },
    "twitter_x": {
        "description": "X/Twitter post. Max 280 characters. Punchy, opinionated, quotable. Can be a standalone take or the opening of a thread (mark with 🧵 if thread). Hooks are everything.",
        "count": 3
    },
    "instagram": {
        "description": "Instagram caption (100-200 words). Hook line 1. Whitespace between paragraphs (use line breaks). Story or insight. End with a CTA to 'link in bio'. 10-15 hashtags after a line break.",
        "count": 2
    },
    "tiktok_script": {
        "description": "TikTok/Reels video script (60-90 seconds spoken). Format: [HOOK], [BODY - 3 quick points], [CTA]. Conversational. Each point 1-2 sentences. Written as it would be spoken aloud.",
        "count": 1
    }
}

# ── GENERATE ────────────────────────────────────────────────────────────────────
def generate_week_of_posts():
    now = datetime.utcnow()
    week_num = now.strftime("%Y-W%V")

    system_prompt = f"""You are a social media content writer for Elias Mercer, who runs {SITE_URL} — an honest AI tools review site for small businesses.

VOICE:
{AUTHOR_VOICE}

ALWAYS INCLUDE: A link or reference to {SITE_URL} in every post (either the full URL or "link in bio" for Instagram).

NEVER DO:
- Fake urgency ("Act now!", "Limited time!")
- Empty superlatives ("amazing", "incredible", "game-changing")
- Start posts with "I" (LinkedIn algorithm penalty)
- Generic advice — always tie to specific tools or numbers
- Sound like a press release

OUTPUT FORMAT: Return valid JSON only. No markdown, no preamble. Structure:
{{
  "week": "{week_num}",
  "posts": [
    {{
      "platform": "linkedin|twitter_x|instagram|tiktok_script",
      "tool_focus": "tool name or 'general'",
      "content": "the post content",
      "notes": "brief note on strategy/timing"
    }}
  ]
}}"""

    # Build the tools summary for context
    tools_summary = json.dumps([{
        "name": t["name"], "price": t["price"], "best_for": t["best_for"],
        "honest_take": t["honest_take"], "url": f"{SITE_URL}/{t['anchor']}"
    } for t in TOOLS], indent=2)

    user_prompt = f"""Generate a full week of social media posts promoting the AI tools review site.

TOOLS ON THE SITE:
{tools_summary}

WHAT TO GENERATE:
- 2 LinkedIn posts (different tools, different angles)
- 3 X/Twitter posts (mix of standalone takes and thread openers)
- 2 Instagram captions
- 1 TikTok/Reels script

ANGLES TO USE THIS WEEK (rotate through these across posts):
1. "I tested 23 AI tools and cancelled 16" — the editorial credibility angle
2. Specific ROI story from a tool (use real numbers from reviews)
3. "The free stack" — Canva + Zapier + Kit = $0
4. Counterintuitive take — e.g. "The cheapest tool saved me the most time"
5. Direct comparison or elimination: "Here's who should NOT buy [tool]"
6. The calculator angle — "15 hours saved = $X/month at your rate"

Make each post feel like a distinct piece of content, not variations of the same message."""

    print(f"Generating posts for {week_num}...")

    response = client.messages.create(
        model="claude-sonnet-4-20250514",
        max_tokens=4000,
        system=system_prompt,
        messages=[{"role": "user", "content": user_prompt}]
    )

    raw = response.content[0].text.strip()

    # Parse JSON
    try:
        data = json.loads(raw)
    except json.JSONDecodeError:
        # Strip any accidental markdown fences
        raw = raw.replace("```json", "").replace("```", "").strip()
        data = json.loads(raw)

    return data, week_num


def save_posts(data, week_num):
    os.makedirs("social-posts", exist_ok=True)
    filepath = f"social-posts/{week_num}.md"

    lines = [
        f"# Social Posts — {week_num}",
        f"*Generated {datetime.utcnow().strftime('%Y-%m-%d %H:%M UTC')}*",
        f"*Site: {SITE_URL}*",
        "",
        "---",
        ""
    ]

    platform_order = ["linkedin", "twitter_x", "instagram", "tiktok_script"]
    platform_labels = {
        "linkedin": "## 🔵 LinkedIn",
        "twitter_x": "## 🐦 X / Twitter",
        "instagram": "## 📸 Instagram",
        "tiktok_script": "## 🎵 TikTok / Reels Script"
    }

    posts_by_platform = {p: [] for p in platform_order}
    for post in data.get("posts", []):
        p = post.get("platform", "linkedin")
        if p in posts_by_platform:
            posts_by_platform[p].append(post)

    for platform in platform_order:
        posts = posts_by_platform[platform]
        if not posts:
            continue
        lines.append(platform_labels.get(platform, f"## {platform}"))
        lines.append("")
        for i, post in enumerate(posts, 1):
            tool = post.get("tool_focus", "general")
            notes = post.get("notes", "")
            content = post.get("content", "")
            lines.append(f"### Post {i} — Focus: {tool}")
            if notes:
                lines.append(f"*Strategy: {notes}*")
            lines.append("")
            lines.append("```")
            lines.append(content)
            lines.append("```")
            lines.append("")
        lines.append("---")
        lines.append("")

    lines += [
        "## ✅ Publishing Checklist",
        "",
        "- [ ] LinkedIn Post 1 — schedule Mon 9am",
        "- [ ] LinkedIn Post 2 — schedule Wed 12pm",
        "- [ ] X Post 1 — schedule Mon 10am",
        "- [ ] X Post 2 — schedule Tue 2pm",
        "- [ ] X Post 3 — schedule Thu 11am",
        "- [ ] Instagram Post 1 — schedule Tue 6pm",
        "- [ ] Instagram Post 2 — schedule Fri 5pm",
        "- [ ] TikTok Script — film & post Wed or Thu",
        "",
        "---",
        "*Posts auto-generated by GitHub Actions. Review before publishing.*"
    ]

    with open(filepath, "w") as f:
        f.write("\n".join(lines))

    print(f"✓ Saved {len(data.get('posts', []))} posts to {filepath}")
    return filepath


if __name__ == "__main__":
    data, week_num = generate_week_of_posts()
    filepath = save_posts(data, week_num)
    print(f"✓ Done. Open {filepath} to review and schedule your posts.")
