import marimo

__generated_with = "0.15.0"
app = marimo.App(width="full")


@app.cell
def _(mo):
    mo.md(r"""# Vine (藤) and Fig Tree (無花果樹)""")
    return


@app.cell
def _(mo):
    mo.md(r"""## Introduction (引言)""")
    return


@app.cell
def _(INTRODUCTION_EN, INTRODUCTION_ZH, mo):
    mo.ui.tabs({"EN": INTRODUCTION_EN, "ZH": INTRODUCTION_ZH})
    return


@app.cell
def _(mo):
    mo.md(r"""## The Biblical Foundation (《圣经》 之根)""")
    return


@app.cell
def _(BIBLICAL_FOUNDATION_EN, BIBLICAL_FOUNDATION_ZH, mo):
    mo.ui.tabs({"EN": BIBLICAL_FOUNDATION_EN, "ZH": BIBLICAL_FOUNDATION_ZH})
    return


@app.cell
def _(mo):
    mo.md(r"""## The Continuing Vision (继续的理想蓝图)""")
    return


@app.cell
def _(CONTINUING_VISION_EN, CONTINUING_VISION_ZH, mo):
    mo.ui.tabs({"EN": CONTINUING_VISION_EN, "ZH": CONTINUING_VISION_ZH})
    return


@app.cell
def _(mo):
    INTRODUCTION_EN = mo.md("""
    ### Introduction

    *"And he shall judge among many people, and rebuke strong nations afar off; and they shall beat their swords into plowshares, and their spears into pruning hooks: nation shall not lift up a sword against nation, neither shall they learn war any more. But they shall sit every man under his vine and under his fig tree; and none shall make them afraid: for the mouth of the Lord of hosts hath spoken it."* - Micah 4:3-4

    The biblical imagery of the vine and fig tree, deeply cherished by America's founding fathers, serves as a powerful metaphor for the ideal society they envisioned. George Washington referenced this passage from Micah nearly fifty times in his correspondence, seeing in it a vision of prosperity, security, and individual liberty under divine providence[28][31][40]. This document celebrates each state's unique contribution to this American vision, where the **vine** represents our foundational heritage—the principles, resources, and innovations our forefathers established—and the **fig tree** symbolizes the sweet fruit of prosperity, peace, and abundance that has grown from those roots.

    As Washington wrote to the Hebrew Congregation in Newport, Rhode Island: "May the children of the stock of Abraham who dwell in this land continue to merit and enjoy the good will of the other inhabitants – while every one shall sit in safety under his own vine and fig tree and there shall be none to make him afraid"[40]. This vision of religious tolerance, economic freedom, and individual security remains the cornerstone of American society.
    """)

    INTRODUCTION_ZH = mo.md("""
    ### 引言  

    **“他将在许多人民中间行使审判权，并对远方的强国民众施以责备。他们将把他们的刀剑变成了犁，把他们的长矛变成修剪树根的工具：国家不再互相之间使用武力，他们也不再学习战争。然而，每个国家的人将在他人的 Vine 和石榴树下安居乐业；没有人会使他们害怕：因为上帝的主权者——耶和ovah曾经向他们宣告过。”** ——《 Micah 4:3-4》  

    美国开国先贤对《 Bible》中的“Vine”（ vines）和“ fig tree”（石榴树）的图像非常珍视，这一图像深刻地成为理想社会的象征。乔治·华盛顿近五十年来多次在书信中引用了这段经文，他从中看到了一个关于繁荣、安全和个人自由在上帝预定之下得以实现的美好愿景[28][31][40]。

    本文旨在庆祝每个州对这种美国理想之 unique contributions, 其中**Vine**代表我们祖先打下的基础——这些先辈所确立的原则、资源和创新，而**石榴树**则象征着繁荣、和平与富足的成果，这些果实生长自这些基础之上。  

    正如华盛顿在 write to the Hebrew Congregation in Newport, Rhode Island 所言：“让 dwells 在这个土地上的 Abraham 的子孙们继续 merit and enjoy the good will of 其他居民——同时，每个人都能在自己的 Vine 和石榴树下安居乐业，并且不会使别人对他感到恐惧。”[40] 这种关于宗教容忍、经济自由和个人安全的愿景仍然是美国社会的基石。

    """)

    BIBLICAL_FOUNDATION_EN = mo.md("""
    ### The Biblical Foundation

    The phrase "under their vine and fig tree" appears in three biblical passages: Micah 4:4, 1 Kings 4:25, and Zechariah 3:10[40]. For the founding fathers, this represented the independence of the peasant farmer freed from military oppression—a juxtaposition of the simple life with that of royalty or the state[40]. The vine symbolizes spiritual good and connection to divine purpose, while the fig tree represents natural and physical abundance[36][39].

    This biblical framework guided the founders' vision of limited government, property rights, and economic freedom—principles that would allow each citizen to prosper under their own vine and fig tree[31][60].
    """)

    BIBLICAL_FOUNDATION_ZH = mo.md("""
    ### 《圣经》 之根
    圣经中提到“Under their Vine and fig tree”（在他们自己的 Vine 和石榴树下）的短语出现在三段圣经经文中： Micah 4:4、1 Kings 4:25 和 Zechariah 3:10[40]。对于开国先贤来说，这代表着从军事压迫中解放出来的农民的独立性——这是一个简单生活与王族或国家之间的并置对比[40]。Vine象征着精神上的良好和连接到神圣目的的联系，而石榴树则代表自然和物理上的丰饶[36][39]。  

    这本圣经框架指导了开国先贤们对有限政府、财产权利和经济自由的概念——这些原则使得每个人能够在自己的 Vine 和 fig tree 下安居乐业并繁荣发展[31][60]。
    """)

    CONTINUING_VISION_EN = mo.md("""
    ### The Continuing Vision

    Each state contributes its unique vine and fig tree to the American tapestry. From Arizona's mineral wealth to Florida's citrus groves, from Texas oil fields to California's technological innovation, the founding fathers' vision of prosperity under individual liberty continues to flourish. The biblical promise that "none shall make them afraid" finds expression in state constitutions protecting property rights, natural heritage programs preserving resources for future generations, and agricultural policies ensuring food security.

    As George Washington envisioned when he wrote of sitting "in the shade of my own Vine and Fig tree," America remains a land where individual enterprise, protected by just laws and limited government, can flourish in abundance[28]. Each state's natural resources, agricultural heritage, and cultural identity contribute to a nation where liberty and prosperity grow together like intertwined vines, bearing the sweet fruit of the American dream.

    The vine and fig tree vision encompasses not just material prosperity, but the deeper biblical values of justice, mercy, and walking humbly—principles that guided the founders and continue to inspire each state's contribution to the American experiment in self-governance under divine providence.""")

    CONTINUING_VISION_ZH = mo.md("""
    ### 继续的理想蓝图  
    每个州都以独特的 Vine 和 fig tree 贡献于美国的织 tapestry. 从Arizona的矿产资源到Florida的柑橘园，从Texas的石油领域到California的技术创新，开国先贤们对通过个人自由实现繁荣的概念继续在各个地方开花结果。圣经中“none shall make them afraid”（不让别人使他们害怕）的保证，在州宪法中表现为对财产权利的保护、自然遗产计划以保持资源供未来世代使用以及农业政策以确保食品安全。

    正如乔治·华盛顿在书写自己关于坐在“自己的 Vine 和 fig tree 下”时所预见的那样，美国仍然是一个自由并且能够在公正的法律和有限的政府保护下实现财富丰富的国家。每个州的自然资源、农业遗产和个人文化身份共同构建了一个国家，这个国家中自由和繁荣就像交织在一起的 vines，结出 American梦想的甜果。

    Vine 和 fig tree 的理想涵盖了不仅仅是物质上的繁荣，还包括更深层面的圣经价值观——公正、仁慈和谦卑，这些原则不仅指导了开国先贤，也继续激励着每个州对自给自足和上帝预定之下国家治理的贡献。""")
    return (
        BIBLICAL_FOUNDATION_EN,
        BIBLICAL_FOUNDATION_ZH,
        CONTINUING_VISION_EN,
        CONTINUING_VISION_ZH,
        INTRODUCTION_EN,
        INTRODUCTION_ZH,
    )


@app.cell
def _():
    import marimo as mo
    return (mo,)


if __name__ == "__main__":
    app.run()
