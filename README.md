## **Web Page Text Summarization using LangChain And Google Gemini**

Summarize a web page, an article and blog post. This application allows to provide a URL which then use Langchain and Google Gemini model to summarize the web content for the provided URL.
A web interface built with Streamlit.


## **Installation Steps**

1. **Clone the repository**
   ```bash
   git clone https://github.com/shwetavw/web-url-text-summarization.git
   cd web-url-text-summarization
   ```

2. **Create Python env**
   ```bash
   conda create -n {env_name} python=3.10 -y
   conda activate {env_name}
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Run the Streamlit app**
   ```bash
   streamlit run app.py
   ```

## **Features**

- **Provide URL** : Use the interface to provide a WEB URL.
- **Concise Summary** : Get the summarized content from the provided URL

## **Techstack**
- Python
- LangChain
- Google Gemini
- Streamlit

