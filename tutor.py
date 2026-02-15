"""
Phasics — AI Tutor powered by Gemini
Socratic method with high-level detailed explanations
"""

import google.generativeai as genai


SYSTEM_PROMPT = """You are an expert physics tutor for a college-level Waves and Modern Physics course, teaching 19-year-old students using the Socratic method.

YOUR TEACHING PHILOSOPHY:
- Lead with questions that guide the student to discover the answer themselves
- When they're stuck, give a DETAILED, high-level explanation — do not be brief. Use thorough, multi-step reasoning
- Connect every concept to physical intuition: what does this LOOK like? What does it FEEL like?
- Use rich real-world analogies: guitar strings, organ pipes, playground swings, ripples in a pond, earthquake waves
- Show the mathematical derivation step by step when relevant, explaining EACH step conceptually
- When correcting mistakes, first acknowledge what the student got RIGHT, then address the misconception
- Use dimensional analysis as a teaching tool ("notice the units work out because...")
- Build from what the student already knows to what they don't

YOUR EXPLANATION STYLE:
- Be thorough and detailed — a 19-year-old needs the "why" behind every step
- Use equations but ALWAYS explain them in words too
- Give multiple perspectives on the same concept when helpful
- Include "what if" scenarios to deepen understanding ("what would happen if the tension were doubled?")
- Summarize key takeaways at the end of longer explanations
- Be warm, encouraging, and patient — physics is hard and that's okay
- Use markdown formatting for equations and emphasis"""


def get_tutor_response(
    user_message: str,
    chat_history: list,
    context: dict = None,
    student_stats: dict = None,
    api_key: str = None,
) -> str:
    """Get a response from the Gemini-powered tutor."""
    if not api_key:
        return "⚠️ Please enter your Gemini API key in the sidebar to use the AI tutor."

    try:
        genai.configure(api_key=api_key)
        model = genai.GenerativeModel(
            "gemini-2.0-flash",
            system_instruction=_build_system_prompt(context, student_stats),
        )

        # Build conversation history for Gemini
        gemini_history = []
        for msg in chat_history:
            role = "model" if msg["role"] == "assistant" else "user"
            gemini_history.append({"role": role, "parts": [msg["content"]]})

        chat = model.start_chat(history=gemini_history)
        response = chat.send_message(user_message)
        return response.text

    except Exception as e:
        error_msg = str(e)
        if "API_KEY" in error_msg.upper() or "401" in error_msg or "403" in error_msg:
            return "⚠️ Invalid Gemini API key. Please check your key in the sidebar."
        return f"⚠️ Tutor connection issue: {error_msg}\n\nTry rephrasing your question or check your API key."


def _build_system_prompt(context: dict = None, student_stats: dict = None) -> str:
    """Build the full system prompt with optional context."""
    prompt = SYSTEM_PROMPT
    if context:
        status = "correctly answered" if context.get("was_correct") else "struggled with"
        prompt += f"\n\nThe student just {status} a Level {context.get('level', '?')}/5 question about {context.get('subtopic', 'unknown')}: \"{context.get('question_text', '')}\""
    if student_stats:
        prompt += f"\n\nStudent performance so far: {student_stats.get('correct', 0)}/{student_stats.get('total', 0)} correct, current adaptive level: {student_stats.get('level', 1)}/5"
    return prompt
