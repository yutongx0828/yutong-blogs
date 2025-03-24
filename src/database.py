import os
from supabase import create_client, Client
from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    supabase_url: str
    supabase_key: str

    model_config = SettingsConfigDict(env_file=".env")

settings = Settings()
url = settings.supabase_url
key = settings.supabase_key
supabase: Client = create_client(url, key)