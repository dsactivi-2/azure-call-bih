# Bosanski AI Sales Call Agent

Minimalni, praktični AI call agent za prodajne razgovore na bosanskom jeziku.

## Šta je već optimizovano

- Bosanski jezik je forsiran kroz sistemski prompt i guardrails.
- Prodajni tok prati consultative + SPIN pristup.
- Ugrađeni objection-handling playbook.
- Podešeni model parametri za stabilan i uvjerljiv sales ton:
  - `temperature: 0.35`
  - `top_p: 0.9`
  - `frequency_penalty: 0.2`
  - `presence_penalty: 0.0`
  - `max_output_tokens: 350`

## Setup

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
cp .env.example .env
```

U `.env` upiši API ključ:

```env
OPENAI_API_KEY=...
SALES_AGENT_MODEL=gpt-4o-mini
SALES_AGENT_CONFIG=config/sales_agent.bs.yaml
```

## Pokretanje

```bash
python src/sales_agent.py
```

## Kako dodatno „optimalno“ podesiti

1. Ako želiš kreativniji pitch, podigni `temperature` na `0.45`.
2. Ako želiš strožije i kraće odgovore, smanji `max_output_tokens` na `220-280`.
3. Ako targetiraš enterprise, u `audience` i `qualification.required_fields` dodaj:
   - `pravni_uslovi`
   - `proces_nabavke`
4. Za inbound leadove, promijeni `opening_goal` da ide odmah na kvalifikaciju.

## Datoteke

- `src/sales_agent.py` — runtime agent
- `config/sales_agent.bs.yaml` — persona, guardrails, sales logika i model settings
- `.env.example` — env var template
