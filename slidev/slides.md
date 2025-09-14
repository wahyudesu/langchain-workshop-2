---
theme: neversink
addons:
  - slidev-addon-python-runner
  - slidev-addon-rabbit
rabbit:
  slideNum: true

title: Building AI Agent using Langchain & Langgraph
author: Wahyu Ikbal Maulana
info: |
  ## Slidev Starter Template
  Presentation slides for developers.

  Learn more at [Sli.dev](https://sli.dev)
keyword: langgraph, ai, agent, langchain
download: true
exportFilename: building-ai-agent-with-langgraph
export:
  format: pdf
  timeout: 30000
  dark: false
  withClicks: false
  withToc: false

transition: slide-left

mdc: true
# open graph
seoMeta:
  # By default, Slidev will use ./og-image.png if it exists,
  # or generate one from the first slide if not found.
  ogImage: auto
  # ogImage: https://cover.sli.dev

color: navy
---

# AI Workshop

<div class="text-3xl">

**Building `AI Agent` using Langchain & Langgraph**

</div>

**Wahyu Ikbal Maulana** <a href="https://www.linkedin.com/in/wahyuikbalmaulana/" class="ns-c-iconlink"><mdi-open-in-new /></a>  
_AI Engineer at 80& Company_

:: note ::

©Dentechcorp

---
layout: two-cols-title
columns: is-7
color: navy
---

:: title :: 

# Rising Demand, `AI Engineers`

:: left ::

<div class="flex justify-center items-center">
  <img src="/ai-engineer.png" class="w-fit h-fit" />
</div>

<div v-click>- Global AI market $279B (2024)</div>
<div v-click>- 78% of organizations use AI (2024)</div>
<div v-click>- AI job postings +25% (US, Q1 2025 vs Q1 2024)</div>
<div v-click>- AI/ML Engineer roles +41.8% YoY (US)</div>
<div v-click>- Generative AI jobs +700% (2022–24)</div>
<div v-click>- AI-skilled workers earn +56% premium</div>
<div v-click>- Fastest-growing role in Indonesia: AI Engineer</div>
<div v-click>- Digital talent gap in Indonesia +4M</div>

:: right ::

<div v-click>- US #1 fastest-growing job</div>
<div v-click>- AI job postings +59% (2024)</div>
<div v-click>- AI listings +94% YoY (2025)</div>
<div v-click>- 1 in 4 tech roles seek AI skill</div>
<div v-click>- ML Engineer $162k avg sal</div>
<div v-click>- AI Engr ~ $175k median</div>
<div v-click>- Research Sci up to $440k</div>
<div v-click>- Entry AI grads &gt; $190–260k</div>
<div v-click>- Meta offered $200M+ deals</div>
<div v-click>- AI skills = top recruiter pick</div>
<div v-click>- AI is the main focus for the vice president</div>
<div v-click>- AI Engineer openings in Indonesia &gt;1K (+5x vs 2022)</div>
<div v-click>- ML Engineer salary in Jakarta ≥Rp10M/month</div>

---
columns: is-8
color: navy
---

<div class="flex flex-col justify-center items-center mt-8">

<div class="mb-2">

# ey ay enginer 

</div>
<img src="/api-ai.png" class="w-fit h-100" />

</div>


---
layout: two-cols-title
columns: is-8
color: navy
---

:: title :: 

<div class="flex flex-col justify-center items-center mt-8">

# In reality - What's AI Applications look like

</div>

:: left ::

<div class="flex justify-center items-center">
  <img src="/llm-architecture.png" class="w-fit h-100" />
</div>

:: right ::

<div v-click>
- Failure rate so high >70 %
</div>
<div v-click>
- Framework too early
</div>
<div v-click>
- Memory bottleneck
</div>
<div v-click>
- In Production 
</div>

---
layout: top-title-two-cols
columns: is-8
align: l-lt-lt
color: dark
---

:: title ::

# Introduce Me👋

:: left ::

<div class="ns-c-tight">

## **My Experience**

- 💻 **AI Engineer** - Perfect10
- 💻 **AI Engineer** - 80& Company
- 🧑‍💼 **Tech Lead Researcher** - Techfusion
- 🤖 **ML Engineer** - Gastronomi research
- 🤖 **ML Engineer** - Bambubot project
- 📊 **Data Analyst** - KANOTARIA
- 🎓 **AI Student Mentorship** - KORIKA

## Certificate

- **Data Scientist Associate** - Datacamp
- **AI Engineer for Data Scientist Associate** - Datacamp

</div>

:: right ::

<div class="flex absolute bottom-12 right-6 flex-col items-end text-sm">
  <img src="/wahyu-profile.jpg" class="w-36 h-36 rounded-full shadow-lg object-cover mb8" />
  <a href="https://medium.com/@wahyuikbal" target="_blank" class="">Medium</a>
  <a href="https://linkedin.com/@wahyuikbal" target="_blank" class="">Linkedin</a>
  <a href="https://github.com/wahyudesu" target="_blank" class=" mt-1">GitHub</a>
  <a href="https://wahyuikbal.web.id" target="_blank" class=" mt-1">Personal Website</a>

</div>

---
color: navy
---
# AI Agent Intro

AI Agent itu sederhana, mari kita buat simpel:

1. Mikir dulu sebelum bertindak (step by step, human in the loop)
2. Pake alat atau sumber luar (tools)
3. Makin pintar seiring waktu (memory)

**From Models to Agents**

from single task -> breakdown task and delegating task -> orchestrator

<div v-click>

<Admonition title="AI Agent" color='amber-light'>
Agents don't just follow instructions — they adapt and makes intelligent decisions about next steps based on what it learns during the process, similar to how we human operate.
</Admonition>

</div>

---
layout: two-cols-title
columns: is-7
color: navy
---

:: title :: 

<div class="flex flex-col justify-center items-center mt-8">

# AI Agent Framework 

</div>

:: left ::

<div class="flex justify-center items-center">
  <img src="/framework.png" class="w-fit h-70" />
</div>

- **[Overview of leading frameworks](https://www.ibm.com/think/insights/top-ai-agent-frameworks)**
- **[Choosing AI Agent frameworks](https://diamantai.substack.com/p/how-to-choose-your-ai-agent-framework)**

:: right ::

<div class="flex justify-center items-center">
  <img src="/choose-framework.png" class="w-fit h-80" />
</div>

---
color: navy
---
# Read more

<div class="text-xl mt-8">

https://blog.langchain.com/building-langgraph/

https://github.com/humanlayer/12-factor-agents

https://www.anthropic.com/engineering/building-effective-agents


</div>

---
layout: iframe-right
title: iframe Right Layout
# the web page source
url: https://langchain-ai.github.io/langgraphjs/#full-stack-quickstart

# a custom class name to the content
class: my-cool-content-on-the-right
slide_info: false
---

# Why Langgraph and AI Agents Applications

- Ideal for complex workflows
- asdas

---
layout: side-title
color: navy
align : lm-lm
---

:: title ::

# Langgraph Core

LangGraph provides low-level supporting infrastructure for any long-running, stateful workflow or agent. LangGraph does not abstract prompts or architecture, and provides the following central benefits:
:: content ::

create an agent using prebuilt components:

<<< ../langgraph.py

---
layout: side-title
color: navy
align : lm-lm
---

:: title ::

# Graph

At its core, LangGraph models agent workflows as graphs. You define the behavior of your agents using three key components:

:: content ::

-> `State`: A shared data structure that represents the current snapshot of your application. It can be any data type, but is typically defined using a shared state schema.

-> `Nodes`: Functions that encode the logic of your agents. They receive the current state as input, perform some computation or side-effect, and return an updated state.

-> `Edges`: Functions that determine which Node to execute next based on the current state. They can be conditional branches or fixed transitions.

---
layout: side-title
side: r
color: navy
titlewidth: is-2
align: lm-lb
---

:: title ::
 
# State

# <mdi-arrow-right />

:: content ::

-> The State is a shared data structure that holds the
current information or context of the entire application.

-> In simple terms, it is like the application’s memory,
keeping track of the variables and data that nodes can
access and modify as they execute.

```python
from typing import TypedDict, Annotated, Sequence
from langchain_core.messages import HumanMessage, AIMessage
from langgraph.graph import StateGraph, END

class ConversationState(TypedDict):
    messages: Annotated[Sequence[HumanMessage | AIMessage], "Conversation history"]
    current_step: Annotated[str, "Current conversation step"]

graph = StateGraph(ConversationState)
```

`TypedDict`, `Pydantic Model`

---
layout: side-title
side: r
color: navy
titlewidth: is-2
align: lm-lb
---

:: title ::
 
# Nodes

# <mdi-arrow-right />

:: content ::

-> Nodes are individual functions or operations that perform specific tasks within the graph.

-> Each node receives input (often the current state), processes it, and produces an output or an updated state.

```python
from langchain_openai import ChatOpenAI

def respond_to_user(state: ConversationState) -> ConversationState:
    messages = state["messages"]
    model = ChatOpenAI()
    response = model.invoke(messages)
    new_messages = list(messages)
    new_messages.append(response)
    return {
        "messages": new_messages,
        "current_step": "response_generated"
    }

graph.add_node("respond_to_user", respond_to_user)
```

`Custom Node`, `START Node`, `END Node`, `Node Caching`

---
layout: side-title
side: r
color: navy
titlewidth: is-2
align: lm-lb
---

:: title ::
 
# Edges

# <mdi-arrow-right />

:: content ::

-> Edges are the connections between nodes that determine the flow of execution.

-> They tell us which node should be executed next after the current one completes its task.


```python
graph.add_edge("node_a", "node_b")

def route_based_on_step(state: ConversationState) -> str:
    if state["current_step"] == "response_generated":
        return "check_if_done"
    else:
        return "respond_to_user"

graph.add_conditional_edges(
    "respond_to_user",
    route_based_on_step,
    {
        "check_if_done": "check_if_done",
        "respond_to_user": "respond_to_user"
    }
)
```

`Normal Edges`, `Conditional Edges`, `Entry Point`, `Conditional Entry Point`


---
columns: is-8
color: navy
title: langgraph-component
---

<div class="flex justify-center items-center mb-8">
  <img src="/langgraph-core.png" class="w-fit h-50" />
</div>

<div class="flex justify-center items-center">
  <img src="/langgraph-core-2.png" class="w-fit h-60" />
</div>

---
layout: top-title-two-cols
color: navy
align: l-lt-lt
---

:: title ::

# LangGraph APIs


:: left ::

## Graph API

<div class="ns-c-supertight text-sm">

-> Deklaratif; mendefinisikan workflow sebagai graph / state graph.

-> State eksplisit, dengan deklarasi state + reducer untuk update state.

-> Checkpoint dibuat lebih granuler (setiap superstep / node)

-> Mudah divisualisasikan sebagai graph 

</div>

```python
from langgraph.graph import StateGraph,START, END
from typing import TypedDict

workflow = StateGraph(MyState)
workflow.add_node("inc", increment)
workflow.add_edge("inc", END)
workflow.set_entry_point("inc")

graph = workflow.compile()
```

<a href="https://langchain-ai.github.io/langgraph/concepts/low_level/" target="_blank" class=" mt-1">Graph API</a>

:: right ::

# Functional API

<div class="ns-c-supertight text-sm">

-> Imperatif/fungsional; memakai fungsi bawaan python, if, for, etc

-> State otomatis dikelola dalam entrypoint / decorator, tidak perlu state global eksplisit antar fungsi.

-> Checkpoint dibuat di entrypoint

-> Tidak ada visualisasi graph statis

</div>

```python
from langgraph.func import entrypoint, task

@task
def write_essay(topic: str) -> str:
  """API call or data processing step"""

@entrypoint()
def workflow(topic: str) -> dict:
  """simple workflow code in here"""
```

<a href="https://langchain-ai.github.io/langgraph/concepts/functional_api/#determinism" target="_blank" class=" mt-1">Functional API</a>


---
layout: fact
class: item-left
---

# Let's Practice! 🚀

## Get Started:

<<< ../README.md#getting

---
layout: side-title
color: navy
align: rm-lm
titlewidth: is-2
---

:: title ::
# Project Structure


:: content ::

<<< ../project-structure.md

<Admonition title="Langgraph Studio (Beta)" color='amber-light'>
</Admonition>

---
layout: side-title
color: navy
align: rm-lm
titlewidth: is-2
---

:: title ::
# More references

:: content ::

https://github.com/abhishekmaroon5/langgraph-cookbook/

https://github.com/langchain-ai/langgraph-101/agents/

Learn more on :
https://academy.langchain.com

---
layout: center
---

# Wrapping Up 🎉

## What We Built

- 🔄 **More know about AI Agents**
- 🤖 **Know concept of Langgraph**
- 🎨 **How AI Agents works**
- 📦 **More know about AI development**

---
layout: end
color: green
---

# Resources

<div class="text-xl mt-8">

https://github.com/abhishekmaroon5/langgraph-cookbook/

https://langchain-ai.github.io/langgraph/

https://github.com/wahyudesu/langchain-workshop-2

https://docs.langchain.com/oss/python/langchain/overview

</div>
