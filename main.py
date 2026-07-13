import uvicorn
from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

app = FastAPI(title="Google Gemini Knowledge Universe")
templates = Jinja2Templates(directory="templates")

# Structured data extracted from the exercise sheets
EXERCISES_DATA = {
    "topic": "Topic 1: Welcome to Google Gemini",
    "set_title": "Exercise Set 1: Getting Started with Google Gemini",
    "description": "These five hands-on exercises guide you through your very first steps with Google Gemini — from logging in and identifying your plan, to setting custom instructions, exploring chat modes, refining prompts, and connecting your Google apps.",
    "meta": ["5 Exercises", "Beginner to Advanced", "Hands-On Practice"],
    "exercises": [
        {
            "id": 1,
            "title": "Exercise 1: First Login & Plan Check",
            "difficulty": "Beginner",
            "difficulty_color": "bg-green-100 text-green-800 border-green-300",
            "border_color": "border-l-4 border-l-blue-600",
            "scenario": "You are a new Gemini user. Your goal is to log in, identify your current plan, and get comfortable with the interface before doing anything else.",
            "steps": [
                "Open gemini.google.com in your browser.",
                "Check whether you are automatically signed in using your Google account.",
                "Look at the background colour — white means Free plan, black means Pro plan.",
                "Locate the prompt box at the bottom of the screen.",
                "Type your very first message: 'What can you help me with today?'",
                "Read the response and note the range of capabilities Gemini lists."
            ],
            "outcome": "You have successfully identified your plan and sent your first prompt. Gemini should respond with a helpful overview of its capabilities."
        },
        {
            "id": 2,
            "title": "Exercise 2: Set Your Custom Instructions",
            "difficulty": "Beginner",
            "difficulty_color": "bg-green-100 text-green-800 border-green-300",
            "border_color": "border-l-4 border-l-blue-600",
            "scenario": "You want Gemini to know you are a small business owner who uses Android and prefers concise, bullet-point answers. You will configure this once so it applies to every future conversation.",
            "steps": [
                "Open Gemini Settings using the gear icon.",
                "Navigate to the 'Custom Instructions' section.",
                "In the 'About you' field, write: 'I'm a small business owner. I use an Android phone and a Windows laptop.'",
                "In the 'Response style' field, write: 'Give me concise answers using bullet points. Keep examples practical and business-relevant.'",
                "Save your instructions.",
                "Test it immediately: Ask 'How can I improve my customer response time?'",
                "Evaluate: Are the answers in bullet points? Do they avoid Apple or Mac-specific advice?"
            ],
            "outcome": "Gemini should respond with bullet points, and its suggestions should be relevant to a business context without any irrelevant platform-specific advice."
        },
        {
            "id": 3,
            "title": "Exercise 3: Normal Chat vs Temporary Chat",
            "difficulty": "Beginner",
            "difficulty_color": "bg-green-100 text-green-800 border-green-300",
            "border_color": "border-l-4 border-l-blue-600",
            "scenario": "You want to clearly understand the difference between standard chat (saved history) and Temporary Chat (incognito mode), and know when to use each.",
            "steps": [
                "Start a New Chat from the main interface.",
                "Ask: 'Give me 3 tips for better sleep.'",
                "After the response, check your chat history on the left sidebar — this conversation should appear.",
                "Now start a Temporary Chat using the menu option.",
                "Ask the exact same question: 'Give me 3 tips for better sleep.'",
                "After the response, return to your chat history — the temporary conversation should NOT appear there.",
                "Reflect and write down: In what situations would you choose Temporary Chat? (e.g., health questions, confidential business topics, sensitive research)"
            ],
            "outcome": "You clearly observe the privacy difference. The temporary chat leaves no trace in your history, making it ideal for private or sensitive queries."
        },
        {
            "id": 4,
            "title": "Exercise 4: Edit Your Last Prompt",
            "difficulty": "Intermediate",
            "difficulty_color": "bg-yellow-100 text-yellow-800 border-yellow-300",
            "border_color": "border-l-4 border-l-blue-600",
            "scenario": "You asked Gemini a question but the response was too long and detailed. Instead of starting a new chat, you use the prompt editing feature to refine your request.",
            "steps": [
                "Ask Gemini: 'Explain how solar panels work.'",
                "Read the response — it is likely very detailed and lengthy.",
                "Scroll up to your original message and click the edit icon (pencil symbol).",
                "Change your prompt to: 'Explain how solar panels work in exactly 3 sentences.'",
                "Submit the edited prompt and compare the two responses side by side.",
                "Edit again: Change the prompt to 'Explain how solar panels work using an analogy a 10-year-old would understand.'",
                "Reflect: How does editing prompts save time compared to starting a new conversation?"
            ],
            "outcome": "You receive a much shorter, targeted response without losing the conversation thread. This is a critical skill for refining AI outputs efficiently."
        },
        {
            "id": 5,
            "title": "Exercise 5: Connect Google Apps & Ask a Personal Question",
            "difficulty": "Intermediate",
            "difficulty_color": "bg-yellow-100 text-yellow-800 border-yellow-300",
            "border_color": "border-l-4 border-l-blue-600",
            "scenario": "You want Gemini to act as a true personal assistant by accessing your real Gmail inbox — demonstrating the difference between a search engine and a personal AI.",
            "steps": [
                "Go to Gemini Settings and find the Extensions section.",
                "Enable the Google Workspace extension (grants access to Gmail and Google Drive).",
                "Return to a new chat and type: 'Summarise the last 3 emails in my Gmail inbox using @Gmail'",
                "Observe how Gemini accesses and reads your live inbox data.",
                "Follow up: 'Draft a polite, professional reply to the most recent email.'",
                "Review the draft: Does it reflect the correct sender, subject, and appropriate tone?",
                "Reflect: How is this different from searching your inbox manually?"
            ],
            "outcome": "Gemini should produce accurate summaries from your real inbox and a contextually appropriate draft reply — acting as a genuine personal assistant, not just a search tool."
        }
    ]
}

@app.get("/", response_class=HTMLResponse)
async def read_root(request: Request):
    return templates.TemplateResponse(
        request=request,
        name="index.html", 
        context={"data": EXERCISES_DATA}
    )

if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)