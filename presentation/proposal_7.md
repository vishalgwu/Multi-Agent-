
# Capstone Proposal
## NewsNet Agents - AI agents forming a network to process news
### Proposed by: Fulsundar Vishal
#### Email: vishal.fulsundar@gwu.edu
#### Advisor: Amir Jafari
#### The George Washington University, Washington DC  
#### Data Science Program


## 1 Objective:  
 
             
            The objective of this project is to develop an intelligent multi-agent AI system that delivers concise, personalized, and bias-aware news summaries in real time. Designed to tackle the challenges of information overload, misinformation, and user attention fatigue, the system leverages a team of autonomous LLM-powered agents � each specializing in a distinct task across the news pipeline.

            Core agents in the system include a News Fetcher Agent to source live headlines, a Summarizer Agent to distill long-form articles into brief 2�3 sentence overviews, a Personalization Agent to tailor news feeds based on user interests, and optional modules such as Bias Detector, Voice Narrator, and Fact-Checker agents for added credibility and accessibility.

            The system offers multi-source integration via RSS feeds, APIs (e.g., NewsAPI, NYT), and social channels (e.g., Reddit, Twitter), enabling users to receive coherent, multi-perspective daily digests through a web dashboard or messaging interface like Telegram.

         Key goals of the project include:
             - Designing a collaborative architecture of LLM-based agents capable of communicating contextually to deliver end-to-end news experiences.
            - Summarizing complex articles using state-of-the-art models like GPT-4, BART, or T5.
            - Enhancing credibility through optional fact-checking and bias analysis using sentiment/tone models.
            - Supporting accessibility through voice-enabled summaries and multilingual delivery.
            - Providing a distraction-free, personalized news experience through topic filtering, time limits, and clean UI delivery.

            The project envisions a future-ready, human-centric news assistant � serving as both a curator and a conscience in the evolving information landscape.
    
            

![ Multi-Agent diagrame](https://github.com/vishalgwu/Multi-Agent-/blob/main/Multi-agent-Diagram.drawio.png)

*Figure 1: Caption*

## 2 Dataset:  

            The dataset for fine-tuning and agent-level customization is still to be 
            finalized (TBD). However, the system will primarily rely on a combination
             of publicly available datasets and real-time data streams. 
             These will support the training, evaluation, and deployment of various agents
              across summarization, personalization, bias detection, and fact-checking tasks.
              
              following data sources are being considered:
              News Summarization Datasets- 
                CNN/DailyMail Dataset - https://www.kaggle.com/datasets/gowrishankarp/newspaper-text-summarization-cnn-dailymail
                BBC News summary Dataset- https://www.kaggle.com/datasets/pariza/bbc-news-summary
                Multi-news dataset- https://huggingface.co/datasets/alexfabbri/multi_news
                
              News classification dataset - 
                news catagory datset- https://huggingface.co/datasets/khalidalt/HuffPost
                AG news class dataset- https://www.kaggle.com/datasets/amananandrai/ag-news-classification-dataset
                
              News sentiment analysis (Bias detection)-
                Twitter/ Reddit - 
                media bias by all media - https://github.com/irgroup/Qbias/tree/main
                custom web scraping - of media pages or allside media page 
                
              Check the fact of the news- 
                FEVER DATASET- https://fever.ai/dataset/fever.html
                Fake news detection  dataset- https://www.kaggle.com/datasets/emineyetm/fake-news-detection-datasets
                Real time fact check with google RAG - https://cloud.google.com/generative-ai-app-builder/docs/check-grounding
                
              Real time News - 
               News apis -  https://newsapi.org/
               Google news- https://rss.app/en/rss-feed/google-news-rss-feed
                           and 
                Serpi api -Scrape Google and other search engines from our fast, easy, and complete API
                         https://serpapi.com/
                         
                Gnews api , News Api , web scrping ,NY time , the gurdians
                
                And GPT BART  
                
            
                           
                
                
              
            

## 3 Rationale:  

            Generative AI (genAI) technology offers a novel approach to supporting IPE given that routinely the diversity of team member participants is limited, and some fields are under-represented in IPE training but influential in "real world" teams. By using LLM-based chatbots for this educational
             interventions, there is potential to both improve how learning experiences are delivered and  enhance student post-IPE performance . In this project, we will explore how an AI-driven team collaboration can  act as A news 
             Agent.
            

## 4 Approach:  

           The development of the Short News Multi-Agent AI System will be executed in structured phases, each targeting a critical component of the overall system functionality:
        
            **Phase 1 � Requirement Analysis**: 
            Define user personas, topic preferences, and key features such as summarization depth, delivery modes (text/audio), bias detection level, and supported platforms (web, chat interface).
        
            **Phase 2 � Agent Architecture Design**: 
            Design modular agent roles including News Fetcher, Summarizer, Bias Detector, Fact-Checker, Personalization Agent, and Voice Reader. Determine inter-agent communication and task delegation flows.
        
            **Phase 3 � Dataset Integration & Fine-Tuning**: 
            Collect and preprocess both static (e.g., CNN/DailyMail, BBC) and live (e.g., NewsAPI, Google RSS) news data. Fine-tune summarization and bias detection models using labeled datasets and apply RAG where needed.
        
            **Phase 4 � Agent Development**: 
            Implement each agent using LLMs and supporting APIs. Integrate them into a collaborative pipeline using tools like LangChain, FastAPI, or custom orchestration scripts.
        
            **Phase 5 � System Testing & Evaluation**: 
            Evaluate performance across key metrics: summary quality (fluency, coherence, factuality), bias detection accuracy, personalization relevance, and system response time.
        
            **Phase 6 � User Interface & Delivery Integration**: 
            Build a clean UI or messaging interface (e.g., Streamlit or Telegram bot) to present news digests. Optionally, enable voice output using TTS tools and multilingual support.
        
            **Phase 7 � Real-Time Deployment & Feedback Loop**: 
            Deploy the system in real-time, allowing for continuous feedback collection, usage analytics, and future updates via retraining or agent tuning.
            

## 5 Timeline:  

             This is a projected timeline for the development and evaluation of the Short News Multi-Agent AI System:

            **Weeks 1�2**: 
            Requirement analysis, agent role definition, and setup of core tools (e.g., Git, APIs, model libraries, Streamlit/Telegram interface). Finalize project scope and datasets.
        
            **Weeks 3�5**: 
            Develop initial versions of the News Fetcher, Summarizer, and Personalization agents. Test with static datasets (e.g., CNN/DailyMail, BBC News).
        
            **Weeks 6�8**: 
            Integrate live news sources (e.g., NewsAPI, RSS) and implement Bias Detector and Fact-Checker agents. Begin inter-agent communication and pipeline orchestration.
        
            **Weeks 9�11**: 
            Conduct iterative testing on the full agent workflow. Evaluate output quality (summarization, bias detection, fact-checking) and optimize model performance.
        
            **Weeks 12�13**: 
            Build user interface (Streamlit web app or Telegram bot). Integrate personalization logic and optional voice/audio delivery features.
        
            **Weeks 14�15**: 
            Perform usability testing and gather user feedback. Refine based on user experience and interaction data.
        
            **Week 16**: 
            Finalize documentation, project report, and system demonstration for presentation or deployment.
                    


## 6 Expected Number Students:  

            This project is doing individually given the scope and need for interdisciplinary collaboration we will in future.
            
            

## 7 Possible Issues:  

            Potential challenges for this project include:
                **Limited Access to Real-Time News Data**: Some APIs (e.g., NewsAPI, NYTimes) may impose rate limits or require paid access for full article content, potentially impacting the real-time capabilities of the system.

                **Dataset Alignment for Bias and Fact-Checking**: High-quality, labeled datasets for political bias detection or factual verification are limited. Building or curating custom datasets may be necessary.
            
                **LLM Output Reliability**: Summarization and fact-checking using large language models may occasionally produce hallucinations, biased phrasing, or unsupported claims, requiring additional post-processing or human verification layers.
            
                **Agent Coordination Complexity**: Ensuring that each agent (fetcher, summarizer, bias detector, etc.) communicates seamlessly without errors or logical breakdowns may require careful orchestration and testing.
            
                **Latency and Scalability**: Real-time performance with multiple agents could introduce delays, especially when querying external APIs or running large models on limited compute resources.
            
                **User Trust and Explainability**: Users may question the credibility of AI-generated summaries. Providing explainability (e.g., source highlighting, bias score justification) will be key to adoption and trust.
            
                **Optional Voice/Chatbot Integration**: Converting text into audio or integrating chat interfaces (Telegram, WhatsApp) may present compatibility issues, especially across platforms or languages.
                        


## Contact :
- Student : Fulsundar Vishal
- instructor: Amir Jafari
- Email: [ajafari@gmail.com](mailto:ajafari@gmail.com)
- GitHub: [https://github.com/vishalgwu/Multi-Agent-](https://github.com/https://github.com/vishalgwu/Multi-Agent-)
