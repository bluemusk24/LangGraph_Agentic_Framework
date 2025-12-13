### Create Virtual environment with uv 
```bash
mkdir LangGraph_lectures

cd LangGraph_lectures

uv init

uv sync

source .venv/bin/activate

uv run python main.py

uv add langgraph langgraph-prebuilt langgraph-sdk langgraph-checkpoint-sqlite langsmith langchain-community langchain-core langchain-ollama notebook tavily-python wikipedia trustcall langgraph-cli[inmem] jupyter notebook
```

***Note***: I use ```Langchain-Ollama``` with CPU locally. ```Langchain-OpenAI``` was used in the actual lecture.
```bash
curl -fsSL https://ollama.com/install.sh | sh

which ollama

ollama run <model_name>

ollama list
```

### Lecture Notes

### 1. Module-0
* [basics notebook](module-0/basics.ipynb)

### 2. Module-1: Introduction
* [simple-graph](module-1/simple-graph.ipynb)

***LANGGRAPH STUDIO LOCALLY*** :
* ensure to have a ```module-1/studio/langgraph.json``` file.

```bash
cd module-1/studio

langgraph dev

https://smith.langchain.com/studio/?baseUrl=http://127.0.0.1:2024
```

* [chain notebook](module-1/chain.ipynb)
* [router notebook](module-1/router.ipynb). Update the ```module-1/studio/langgraph.json``` file with the ```router.py``` file for Langgraph Studio view. Run ```langgraph dev``` in the ```studio/```
* [agent notebook](module-1/agent.ipynb)
* [agent_memory notebook](module-1/agent-memory.ipynb). Update the ```module-1/studio/langgraph.json``` file with the ```agent.py``` file for Langgraph Studio view. Run ```langgraph dev``` in the ```studio/```

### 3. Module-2: State and Memory
* [state-schema notebook](module-2/state-schema.ipynb)
* [state-reducers notebook](module-2/state-reducers.ipynb)
* [multiple-schemas notebook](module-2/multiple-schemas.ipynb)
* [trim-filter-message notebook](module-2/trim-filter-messages.ipynb)
* [chatbot-summary notebook](module-2/chatbot-summarization.ipynb)
* [chatbot-external-memory](module-2/chatbot-external-memory.ipynb)

Create ```module-2/studio/langgraph.json``` and ```module-2/studio/chatbot.py``` for Langgraph Studio view. Run ```langgraph dev``` in the ```studio/```.

### 4. Module-3: UX and Human-in-the-Loop
* [breakpoints notebook](module-3/breakpoints.ipynb)
* Create ```module-3/studio/langgraph.json``` and ```module-3/studio/agent.py``` for Langgraph Studio view. Run ```langgraph dev``` in the ```studio/```.
* [edit-state-human-feedback notebook](module-3/edit-state-human-feedback.ipynb)

```Note```: On Langgraph Studio, ```interrupt_before``` can be added to the ```assistant node``` using the same ```module-3/studio/agent.py```. Human messages can be edited, forked and updated to a new message.

## Project_1: Email Assistant

* [langraph_notebook_intro](email_agent/langgraph_101.ipynb)

***Local Deployment with Langgraph Studio***
create [langgraph101_script](email_agent/studio/langgraph_101.py) and [langgraph_json](email_agent/studio/langgraph.json) in ```email_agent/studio```. Run the code below to launch ```langgraph studio```.

```bash
cd email_agent/studio
langgraph dev
```

* [agent_notebook](email_agent/agent.ipynb)

***Local Deployment with Langgraph Studio***
update [langgraph_json](email_agent/studio/langgraph.json) in ```email_agent/studio``` with [email_assitant](email_agent/studio/email_assistant.py). Run the code below in a new terminal to launch ```langgraph studio```.

```bash
cd email_agent/studio
langgraph dev
```

* Note: I followed the lecture notebook on github for codes because I could not install library ```email_assistant.utils``` with uv.

***Agent Evaluation Test using Langsmith***
[agent_evaluation](email_agent/evaluation.ipynb)


## Project_2: Deep Agents with LangGraph 

* Deep Agents UI Setup with ```LangSmith Studio```

```bash
uv add deepagents

cd deep_agents

pip install deepagents

pip install -U langgraph-cli

pip install -U langgraph-api

langgraph dev
```
[deep_agent notebook](deep_agents/4_full_agent.ipynb)
[test_agent](deep_agents/test_agent.py)
[research_agent](deep_agents/research_agent.py)
[langraph_json](deep_agents/langgraph.json)

* Running Deep Agent UI Locally:

***Note***: Ensure Langsmith Studio ```http://127.0.0.1:2024``` is running if Deep Agent UI is to run alongside it.

```bash
git clone https://github.com/langchain-ai/deep-agents-ui.git

cd deep-agents-ui

npm install

touch .env.local

nano .env.local

# NEXT_PUBLIC_DEPLOYMENT_URL="http://127.0.0.1:2024"  ---> Paste in .env.local 
# NEXT_PUBLIC_AGENT_ID=research (agent name from langgraph.json)   ---> Paste in .env.local

npm run dev

# Open [http://localhost:3000](http://localhost:3000) to test out your deep agent!
```

## LangGraph Deployment with Ollama Locally. 

* create [docker-compose file](langgraph_deployment/docker-compose.yml) and [Dockerfile](langgraph_deployment/Dockerfile) for ```Langgraph Postgres, Redis and API Server```. Run the following:
```bash
langgraph build -t my-image     # Build docker image for Langgraph API Server 
docker-compose up (--build)     # Launch 3 Langgraph containers: API Server, Redis and Postgres
```

***API***: http://localhost:8123   ---> connect deployment locally to notebook. Check video lectures for more.
***Docs***: http://localhost:8123/docs   -----> view documentation for Thread, Runs, Assistant, 
***LangGraph Studio***: https://smith.langchain.com/studio/?baseUrl=http://127.0.0.1:8123

```Note```: 
1. lecture video used OpenAI
2. connect to the deployment API Server above using Langgraph SDK. Watch Lecture video and codes for reference.

## LangSmith: Agent Observability and Evaluations
 * Watch Lecture Video 

### Module_0
- [simple_rag notebook](LangSmith/module_0/rag_application.ipynb)
- [utils scripts](LangSmith/module_0/utils.py)


## Links for more Langgraph Knowledge
[Deep Agents Made Easy](https://github.com/langchain-ai/deepagents)
[MCP with Langchain](https://github.com/langchain-ai/langchain-mcp-adapters)


## Agentic AI with LangGraph (YouTube Lectures)

Lesson_1: LangGraph Tutorial-Getting Started With Pydantic-Data Validations
- [pydantic_basics](agentic_ai/lesson1_Pydantic/pydantic_basics.ipynb)

Lesson_2: Getting Started With LangGraph For Building AI Agents
- [simple_graph](agentic_ai/lesson2_LangGraph Basics/simplegraph.ipynb)

Lesson_3: Build Agentic AI Chatbot Using LangGraph
- [tools_calling](agentic_ai/lesson3_Agentic AI Chatbot wt LangGraph/chat_tools.ipynb)

Lesson_4: Agentic AI With Langgraph And MCP Crash Course-Part 1
***Stdio***
- [math_server](agentic_ai/lesson4_Langgraph & MCP/math_server.py)        
- [math_client_script](agentic_ai/lesson4_Langgraph & MCP/math_client.py)
- [weather_stdio](agentic_ai/lesson4_Langgraph & MCP/weather_stdio.py)

***Streamable-http (sse)***
- [weather_http](agentic_ai/lesson4_Langgraph & MCP/weather_http.py)         
- [weather_client](agentic_ai/lesson4_Langgraph & MCP/weather_client.py)

***MCP Inspector***
- [servers_script](agentic_ai/lesson4_Langgraph & MCP/servers.py)

```bash
# run math_server and math_client alone
uv run python math_server.py
uv run python math_client.py

# run weather_server and weather_client 
uv run python weather.py        # for stremable-http
uv run python weather_client.py

# run combined weather_stdio and math servers.
uv run python client.py

# Using with LangGraph StateGraph
uv run python mcp_langgraph.py

# run MCP Inspector
mcp dev servers.py
```
***Multimodal RAG***
[multimodal_rag](agentic_ai/multimodalopenai.ipynb)

***Multi-Agent with LangGraph***
[multi-agent](agentic_ai/multi-agent.ipynb)
