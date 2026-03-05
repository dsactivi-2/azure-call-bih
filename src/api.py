import os
from typing import Any

from dotenv import load_dotenv
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field

from sales_agent import build_response, build_system_prompt, create_client, load_config


class ChatRequest(BaseModel):
    message: str = Field(min_length=1, description="Korisnička poruka")
    history: list[dict[str, str]] = Field(default_factory=list)


class ChatResponse(BaseModel):
    reply: str


def _load_runtime() -> tuple[Any, str, dict[str, Any], str]:
    load_dotenv(override=False)

    config_path = os.getenv("SALES_AGENT_CONFIG", "config/sales_agent.bs.yaml")
    model = os.getenv("SALES_AGENT_MODEL", "gpt-4o-mini")

    config = load_config(config_path)
    system_prompt = build_system_prompt(config)
    model_settings = config.get("model_settings", {})
    client = create_client()

    return client, model, model_settings, system_prompt


app = FastAPI(title="Bosanski AI Sales Agent API", version="1.0.0")
client, model, model_settings, system_prompt = _load_runtime()


@app.get("/health")
def health() -> dict[str, str]:
    return {"status": "ok"}


@app.post("/chat", response_model=ChatResponse)
def chat(request: ChatRequest) -> ChatResponse:
    try:
        conversation = list(request.history)
        conversation.append({"role": "user", "content": request.message})

        reply = build_response(
            client=client,
            model=model,
            system_prompt=system_prompt,
            conversation=conversation,
            model_settings=model_settings,
        )
        return ChatResponse(reply=reply)
    except Exception as exc:
        raise HTTPException(status_code=500, detail=f"Agent error: {exc}") from exc
