from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file=".env", extra="ignore")

    groq_api_key: str
    tavily_api_key: str

    # Groq model id. Confirm it's current at https://console.groq.com/docs/models
    llm_model: str = "openai/gpt-oss-120b"
    # How many search results to feed the model
    max_results: int = 6


settings = Settings()
