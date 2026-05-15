from pydantic_settings import BaseSettings


class Settings(BaseSettings):

    app_name: str = "RTC Audio Server Settings"
    recordings_dir: str
    transcriber_model_name: str
    voice_model_name: str
    log_level: str
    chat_upstream_read_timeout: float