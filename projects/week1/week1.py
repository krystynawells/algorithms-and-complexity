import marimo

__generated_with = "0.17.6"
app = marimo.App(layout_file="layouts/week1.grid.json", css_file="style3.css")


@app.cell
def _():
    import marimo as mo
    return (mo,)


@app.cell
def _(mo):
    mo.md("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Fredoka:wght@400;600&display=swap');
    </style>
    """)
    return


@app.cell
def _(mo):
    # -----------------------------
    # Headshot
    # -----------------------------

    photo2 = "https://raw.githubusercontent.com/krystynawells/profile-assets/main/Screenshot%202026-01-20%20at%2001.25.21.png"

    mo.hstack(
        [

            mo.image(
                src=photo2,
                width="250imagepx",
                height="250imagepx",
                rounded=True,
                style={"object-fit": "cover"},
            ),
        ],
        gap="xl",
        align="center",
        justify="center",
    )
    return


@app.cell
def _(mo):
    mo.md("""
    <div style="
      max-width: 520px;
      margin: px auto;
      padding: 2px 28px;
      text-align: center;
      font-family: 'Fredoka', sans-serif;
    ">

      <div style="
        font-size: 24px;
        font-weight: 600;
        color: #30343F;
        margin-bottom: 0px;
      ">
        Krystyna Wells
      </div>

      <div style="
        font-size: 16px;
        color: #555;
      ">
        2nd Year BSc Computer Science Student at UAL
      </div>

    </div>
    """)
    return


@app.cell
def _(mo):
    # -----------------------------
    # Links + Buttons 
    # -----------------------------

    # Screenshot of button images
    github_logo = "https://raw.githubusercontent.com/krystynawells/profile-assets/main/Screenshot%202026-01-20%20at%2001.59.54.png"
    linkedin_logo = "https://raw.githubusercontent.com/krystynawells/profile-assets/main/Screenshot%202026-01-20%20at%2001.55.58.png"
    blog_logo = "https://raw.githubusercontent.com/krystynawells/profile-assets/main/Screenshot%202026-01-20%20at%2002.03.21.png"

    # Links
    github_link = "https://github.com/krystynawells"
    linkedin_link = "https://www.linkedin.com/in/krystyna-wells-323531382/"
    blog_link = "https://techtrailblazers.substack.com/"

    # Button Function 
    def link_button(img, url, label):
        return mo.md(f"""
        <a href="{url}" target="_blank" style="text-decoration:none;">
          <img 
            src="{img}" 
            alt="{label}"
            style="
              width:40px;
              height:40px;
              cursor:pointer;
              transition: transform 0.2s ease, filter 0.2s ease;
            "
            onmouseover="this.style.transform='scale(1.12)'; this.style.filter='drop-shadow(0 4px 8px rgba(255,105,180,0.4))';"
            onmouseout="this.style.transform='scale(1)'; this.style.filter='none';"
          />
        </a>
        """)

    # Formatting 
    mo.hstack(
        [
            link_button(github_logo, github_link, "GitHub"),
            link_button(linkedin_logo, linkedin_link, "LinkedIn"),
            link_button(blog_logo, blog_link, "Blog"),
        ],
        gap="xl",
        justify="center",
        align="center",
    )

    return


@app.cell
def _(mo):
    mo.md("""
    ---
    """)
    return


@app.cell
def _(mo):
    # -----------------------------
    # About Me
    # -----------------------------
    mo.md("""
    <div style="
        border: 2px solid #89023E;
        border-radius: 12px;
        padding: 16px;
        background-color: #ffebee;
        font-family: 'Fredoka', sans-serif;
        box-shadow: 2px 2px 6px rgba(255, 182, 193, 0.2);
    ">
        <h3 style="margin-top:0;">About Me</h3>
        <p>
            Hi! I'm <strong>Krystyna Wells</strong>, a second-year Computer Science student
            at the <strong>University of the Arts London</strong>.
            I’m passionate about combining creativity, technology and communication,
            from building IoT systems to exploring AI for design and interaction.
            Currently, I’m the <strong>Treasurer of the FinTech Society</strong> and              author of the blog Tech Trailblazers, I love collaborating on hands-on tech projects.
        </p>
    </div>
    """)
    return


@app.cell
def _(mo):
    # -----------------------------
    # Projects dropdown + card
    # -----------------------------
    projects = [
        {
            "name": "IoT Desk Health Helper",
            "tags": ["IoT", "ESP8266", "MQTT", "Python"],
            "link": "https://github.com/krystynawells/IoT-Desk-Assisstant",
            "summary": "An IoT-based desk health assistant that promotes healthier study/work habits: hydration reminders, screen distance monitoring, and comfort checks.",
        },
        {
            "name": "Text Classifier Tool",
            "tags": ["Python", "TF-IDF"],
            "link": "https://github.com/krystynawells/text-classifier-tool",
            "summary": "An interactive web app that classifies articles or short text into one of 20 news topics using machine learning.",
        },
        {
            "name": "Tech Trailblazers Blog",
            "tags": ["Journalism", "Writing"],
            "link": "https://techtrailblazers.substack.com/",
            "summary": "A blog where I interview women in tech and write accessible pieces about technology and career paths.",
        },
    ]

    names = [p["name"] for p in projects]
    select = mo.ui.dropdown(options=names, value=names[0], label="Choose a project")

    mo.md("""
    <div style="
        border: 2px solid #ffb6c1; border-radius: 12px; padding: 16px;
        background-color: #fff5f8; box-shadow: 2px 2px 6px rgba(255,182,193,0.2);
        margin-top: 12px;
    ">
        <h3 style="margin:0 0 8px 0;">📁 Projects</h3>
    </div>
    """)

    select
    return projects, select


@app.cell
def _(mo, projects, select):
    chosen = next(p for p in projects if p["name"] == select.value)

    mo.md(f"""
    <div style="border:1px solid #ffd6e2; border-radius:12px; padding:14px; background:#fff; margin-top:10px;">
        <div style="font-size:18px; font-weight:600; margin-bottom:4px;">
            {chosen['name']}
        </div>
        <div style="color:#666; margin-bottom:8px;">
            {', '.join(chosen['tags'])}
        </div>
        <div style="margin-bottom:10px;">{chosen['summary']}</div>
        <a href="{chosen['link']}" target="_blank" style="
            display:inline-block; padding:8px 12px; border-radius:10px;
            border:1px solid #ffb6c1; text-decoration:none;
        ">🔗 View</a>
    </div>
    """)
    return


@app.cell
def _(mo):
    # -----------------------------
    # Leadership & Involvement
    # -----------------------------
    mo.md("""
    <div style="border:2px solid #ffb6c1; border-radius:12px; padding:16px; background:#fff5f8;">
      <h3 style="margin:0 0 8px 0;"> Leadership & Involvement</h3>
      <details open>
        <summary><strong>FinTech Society, UAL — Treasurer & Acting Vice President (2024 – Present)</strong></summary>
        <ul style="margin-top:8px;">
          <li>Oversee society finances, budgeting, and event planning for a growing student-led FinTech community</li>
          <li>Spearhead engagement initiatives and first-year outreach</li>
          <li>Organize speaker events exploring blockchain, digital banking, and AI in finance</li>
        </ul>
      </details>
      <details>
        <summary><strong> Tech Trailblazers Blog — Founder & Writer (2024 – Present)</strong></summary>
        <ul style="margin-top:8px;">
          <li>Founded a blog championing women in technology through interviews, insights, and stories from the field</li>
          <li>Conduct interviews with researchers and professionals</li>
          <li>Write articles on AI, IoT, and gender diversity in tech</li>
        </ul>
      </details>
    </div>
    """)
    return


@app.cell
def _(mo):
    mo.md(r"""
    ##                           ✮⋆˙ My Experience ✮⋆˙
                          ★ Use the slider to see my timeline ★
    """)
    return


@app.cell
def _(mo):
    year_slider = mo.ui.slider(start=2022, stop=2025, step=1, value=2025, label="Select Year")

    timeline = {
        2022: {"title": "2022 - Travelling 🇺🇸+🇨🇦", "desc": "Travelled around the United States and Canada. Experienced my first Thanksgiving Turkey 🦃."},
        2023: {"title": "2023 - Worked in Spain + Started Coding 🇪🇸+💻", "desc": "While working in Spain, I began teaching myself to code and realised I wanted to pursue Computer Science."},
        2024: {"title": "2024 - Started my Computer Science degree 🇬🇧", "desc": "Enrolled in my Computer Science programme at UAL, learning core programming concepts and building projects."},
        2025: {"title": "2025 - Internship Applications + Starting my blog 🎯", "desc": "Focused on internship applications, continued part-time work at Wickes, and launched my Tech Trailblazers blog."},
    }
    return timeline, year_slider


@app.cell
def _(mo, timeline, year_slider):
    selected = year_slider.value
    mo.vstack(
        [
            year_slider,
            mo.md(f"### {timeline[selected]['title']}<br>{timeline[selected]['desc']}"),
        ]
    )
    return


@app.cell
def _(mo, year_slider):
    import numpy as np
    import matplotlib.pyplot as plt

    skills = {
        "Python": min(100, 30 + (year_slider.value - 2022) * 20),
        "IoT / Hardware": min(100, 10 + (year_slider.value - 2022) * 18),
        "Writing": min(100, 40 + (year_slider.value - 2022) * 15),
        "Problem Solving": min(100, 35 + (year_slider.value - 2022) * 15),
        "Leadership": min(100, 20 + (year_slider.value - 2022) * 25),
        "Creative Tech": min(100, 25 + (year_slider.value - 2022) * 20),
    }

    labels = list(skills.keys())
    values = list(skills.values())

    angles = np.linspace(0, 2 * np.pi, len(labels), endpoint=False).tolist()
    values += values[:1]
    angles += angles[:1]

    fig, ax = plt.subplots(figsize=(5, 5), subplot_kw=dict(polar=True))

    # pink line
    ax.plot(
        angles,
        values,
        linewidth=2,
        color="#ff69b4"  # hot pink line
    )

    # soft pink fill
    ax.fill(
        angles,
        values,
        alpha=0.3,
        color="#ffb6c1"  # light pink fill
    )

    ax.set_xticks(angles[:-1])
    ax.set_xticklabels(labels, fontsize=9)
    ax.set_yticks([20, 40, 60, 80, 100])
    ax.set_ylim(0, 100)

    ax.set_title(
        f"Skills Overview — {year_slider.value}",
        pad=18,
        color="#d63384"  # darker pink title
    )

    fig.tight_layout()

    mo.as_html(fig)


    mo.as_html(fig)
    return


if __name__ == "__main__":
    app.run()
