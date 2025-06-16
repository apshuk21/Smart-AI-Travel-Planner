# 🌍 AI Travel Agent & Expense Planner

Plan the perfect trip with real-time data and AI-powered insights. This modular Python + LangGraph system helps users choose destinations, explore attractions, estimate costs, and generate itineraries—all in one seamless workflow.

---

## ✈️ Project Purpose

Help users plan trips to any city worldwide by:
- Fetching **real-time weather**
- Recommending **top attractions, activities, and restaurants**
- Estimating **hotel and transport costs**
- Converting currencies based on live exchange rates
- Generating a **complete itinerary**
- Summarizing total trip expenses

---

## 🧱 Tech Stack

- **Python 3.10+**
- **LangChain / LangGraph** for agent orchestration
- **OpenAI or compatible LLM**
- **TavilySearchResults** for real-time search
- Optional: Currency, weather, and booking APIs

---

## 🧩 Modular Architecture

### Object-Oriented Components

- `UserInput`: Holds destination and preferences
- `WeatherService`: Fetches current and forecast weather
- `AttractionService`: Gets attractions, food, and activities
- `HotelService`: Estimates lodging cost
- `CurrencyConverter`: Real-time exchange handling
- `ExpenseCalculator`: Computes daily and total spend
- `ItineraryPlanner`: Builds day-by-day plan
- `SummaryGenerator`: Crafts a final report

---

## 🔀 Agent Workflow (LangGraph DAG)

```text
User Input
   ├──> Attractions, Restaurants, Activities, Transport  ┐
   ├──> Weather & Forecast                                ├──> Cost Estimator
   └──> Hotel Search                                      │
                                                         └──> Currency Converter
                                                                  │
                                                            Itinerary Planner
                                                                  │
                                                            Trip Summary Node
                                                                  │
                                                        ✅ Return Final Plan
