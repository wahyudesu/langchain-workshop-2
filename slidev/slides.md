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

color: dark
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
- AI Agent production so hard
</div>
<div v-click>
- Company says is so hard
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
  <img src="/framework.png" class="w-fit h-80" />
</div>

- **[Overview of leading frameworks](https://www.ibm.com/think/insights/top-ai-agent-frameworks)**
- **[Choosing AI Agent frameworks](https://diamantai.substack.com/p/how-to-choose-your-ai-agent-framework)**


:: right ::

<div class="flex justify-center items-center">
  <img src="/choose-framework.png" class="w-fit h-80" />
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

---
layout: fact
class: item-left
---

# Let's Build! 🚀

## Get Started:

```bash {}
git clone https://github.com/wahyudesu/langchain-workshop
cd rag
uv venv
.venv\Scripts\activate
uv sync
uv run chainlit run app.py -w
```

<div class="mt-8 text-2xl">
Run <code>app.py</code> and begin!
</div>


---

# Vector Database, Embeddings, Retrieval

<div class="grid grid-cols-2 gap-8">

<div>

## Vector Databases

**Storage for embeddings:**
- **Chroma**: Open-source, easy to use
- **Pinecone**: Managed, scalable
- **Weaviate**: Hybrid search capabilities
- **FAISS**: Facebook AI Similarity Search (free)

**Choose based on:**
- Data scale
- Budget
- Self-hosted vs managed

</div>

<div>

## Embeddings

**Convert text to vectors:**
```python
from langchain.embeddings import OpenAIEmbeddings

embeddings = OpenAIEmbeddings()
vectors = embeddings.embed_documents([
    "Langchain is great",
    "AI is powerful"
])
```

**Alternatives:**
- HuggingFace embeddings (free)
- Cohere embeddings
- Custom embeddings

</div>

</div>
---
layout: side-title
color: emerald-light
align: rm-lm
titlewidth: is-3
---

<StickyNote color="emerald-light" textAlign="left" width="180px"  v-drag="[719,291,180,180,16]">

Don't worry if you don't understand all the details, yet we are still talking about **color schemes**.
</StickyNote>


:: title ::
# Langchain


:: content ::

Or we can use the `emerald-light` scheme in a slide layout to set the overall color and style of a slide with a matching sticky note:

```md
---
layout: side-title
color: emerald-light
align: rm-lm
titlewidth: is-3
---
```

---
layout: side-title
side: left
color: violet
titlewidth: is-4
align: rm-lt
title: Code Example
---


:: title ::

# <mdi-code-braces /> Langchain

More cool code stuff

:: content ::

Scrollable with clicks 🤯

```ts {2|3|7|12}{maxHeight:'100px'}
function helloworld() {
  console.log('Hello, World 1!')
  console.log('Hello, World 2!')
  console.log('Hello, World 3!')
  console.log('Hello, World 4!')
  console.log('Hello, World 5!')
  console.log('Hello, World 6!')
  console.log('Hello, World 7!')
  console.log('Hello, World 8!')
  console.log('Hello, World 9!')
  console.log('Hello, World 10!')
  console.log('Hello, World 11!')
}
```

You can even edit the code in the browser

```ts {monaco}
console.log('HelloWorld')
```

You can even run the code in the browser

```ts {monaco-run} {showOutputAt:'+1'}
function distance(x: number, y: number) {
  return Math.sqrt(x ** 2 + y ** 2)
}
console.log(distance(3, 4))
```


---
layout: center
---

# Langchain JS via Cloudflare Worker

<div class="grid grid-cols-2 gap-8">

<div>

## Cloudflare Workers Benefits

- **Edge Computing**: Low latency globally
- **Serverless**: No server management
- **Durable Objects**: State management
- **KV Storage**: Key-value database
- **R2**: Object storage

**Perfect for:**
- Real-time chat applications
- Global AI services
- Low-latency RAG

</div>

<div>

## Implementation Example

```javascript
import { OpenAI } from 'langchain/llms/openai';
import { ConversationChain } from 'langchain/chains';
import { BufferMemory } from 'langchain/memory';

export default {
  async fetch(request, env) {
    const llm = new OpenAI({
      openAIApiKey: env.OPENAI_API_KEY,
      temperature: 0.7
    });
    
    const memory = new BufferMemory();
    const chain = new ConversationChain({ llm, memory });
    
    const { message } = await request.json();
    const response = await chain.call({ input: message });
    
    return new Response(JSON.stringify({ response: response.response }));
  }
};
```

</div>

</div>

---
layout: center
---

# Wrapping Up 🎉

## What We Built

- 🔄 **More know about Generative AI**
- 🤖 **Know more about langchain**
- 🎨 **How RAG Chat works**
- 📦 **More know about AI development**

---
layout: end
color: green
---

# Resources

<div class="text-xl mt-8">

https://business.udemy.com/resources/top-work-employee-skills-2025/

https://github.com/wahyudesu/Fastapi-AI-Production-Template

https://github.com/wahyudesu/langchain-workshop

https://python.langchain.com/docs/introduction/

https://github.com/langchain-ai/langchain/tree/master/cookbook

https://www.pinecone.io/learn/series/langchain/

</div>
