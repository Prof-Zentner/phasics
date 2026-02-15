"""
Phasics — AI Tutor powered by Gemini
Socratic method with high-level detailed explanations
+ Drawing evaluation and math input review
"""

import google.generativeai as genai
import base64
from io import BytesIO


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


DRAWING_EVAL_PROMPT = """You are evaluating a physics student's hand-drawn sketch for a Waves and Modern Physics course.

QUESTION: {question}

EVALUATION CRITERIA (the drawing should show):
{criteria}

EXPECTED ANSWER EXPLANATION:
{explanation}

Analyze the student's drawing and respond in EXACTLY this JSON format (no markdown, no backticks):
{{"score": <number 0-100>, "correct": <true or false>, "feedback": "<detailed feedback explaining what they got right and wrong, with specific physics corrections>"}}

Scoring guide:
- 80-100: Drawing captures all key physics features correctly
- 60-79: Most features correct, minor issues
- 40-59: Some correct elements, significant gaps
- 0-39: Major misconceptions or missing key features

Be encouraging but precise. If something is wrong, explain the physics clearly."""


MATH_REVIEW_PROMPT = """You are evaluating a physics student's mathematical expression/derivation for a Waves and Modern Physics course.

QUESTION: {question}

EXPECTED FORM: {expected_form}

EVALUATION CRITERIA:
{criteria}

STUDENT'S ANSWER: {student_answer}

Analyze the student's math and respond in EXACTLY this JSON format (no markdown, no backticks):
{{"score": <number 0-100>, "correct": <true or false>, "feedback": "<detailed feedback on their mathematical work, noting what's correct and explaining any errors step by step>"}}

Be thorough in your feedback. If their notation is different but mathematically equivalent, count it as correct."""


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


def evaluate_drawing(image_data, question: dict, api_key: str) -> dict:
    """
    Send a student's drawing to Gemini Vision for evaluation.
    
    Args:
        image_data: PIL Image or bytes of the student's drawing
        question: The question dict with eval_criteria and explanation
        api_key: Gemini API key
        
    Returns:
        dict with keys: score (int), correct (bool), feedback (str)
    """
    if not api_key:
        return {
            "score": 0,
            "correct": False,
            "feedback": "⚠️ Please enter your Gemini API key in the sidebar to evaluate drawings.",
        }

    try:
        genai.configure(api_key=api_key)
        model = genai.GenerativeModel("gemini-2.0-flash")

        # Convert PIL image to bytes if needed
        if hasattr(image_data, "save"):
            buffer = BytesIO()
            image_data.save(buffer, format="PNG")
            img_bytes = buffer.getvalue()
        else:
            img_bytes = image_data

        img_b64 = base64.b64encode(img_bytes).decode("utf-8")

        criteria_text = "\n".join(
            f"- {c}" for c in question.get("eval_criteria", [])
        )

        prompt = DRAWING_EVAL_PROMPT.format(
            question=question["question"],
            criteria=criteria_text,
            explanation=question.get("explanation", ""),
        )

        response = model.generate_content(
            [
                {"mime_type": "image/png", "data": img_b64},
                prompt,
            ]
        )

        # Parse JSON response
        import json

        response_text = response.text.strip()
        # Clean up if wrapped in markdown code block
        if response_text.startswith("```"):
            response_text = response_text.split("\n", 1)[-1].rsplit("```", 1)[0].strip()

        result = json.loads(response_text)
        return {
            "score": int(result.get("score", 0)),
            "correct": bool(result.get("correct", False)),
            "feedback": str(result.get("feedback", "Unable to parse evaluation.")),
        }

    except json.JSONDecodeError:
        # If JSON parsing fails, try to extract useful info
        return {
            "score": 50,
            "correct": False,
            "feedback": f"I reviewed your drawing but had trouble scoring it precisely. Here's my analysis:\n\n{response.text if 'response' in dir() else 'Could not get response.'}",
        }
    except Exception as e:
        return {
            "score": 0,
            "correct": False,
            "feedback": f"⚠️ Error evaluating drawing: {str(e)}",
        }


def evaluate_math_input(student_answer: str, question: dict, api_key: str) -> dict:
    """
    Send a student's math expression to Gemini for evaluation.
    
    Args:
        student_answer: The student's typed mathematical expression
        question: The question dict with expected_form and eval_criteria
        api_key: Gemini API key
        
    Returns:
        dict with keys: score (int), correct (bool), feedback (str)
    """
    if not api_key:
        return {
            "score": 0,
            "correct": False,
            "feedback": "⚠️ Please enter your Gemini API key in the sidebar for AI-powered math evaluation.",
        }

    try:
        genai.configure(api_key=api_key)
        model = genai.GenerativeModel("gemini-2.0-flash")

        criteria_text = "\n".join(
            f"- {c}" for c in question.get("eval_criteria", [])
        )

        prompt = MATH_REVIEW_PROMPT.format(
            question=question["question"],
            expected_form=question.get("expected_form", ""),
            criteria=criteria_text,
            student_answer=student_answer,
        )

        response = model.generate_content(prompt)

        import json

        response_text = response.text.strip()
        if response_text.startswith("```"):
            response_text = response_text.split("\n", 1)[-1].rsplit("```", 1)[0].strip()

        result = json.loads(response_text)
        return {
            "score": int(result.get("score", 0)),
            "correct": bool(result.get("correct", False)),
            "feedback": str(result.get("feedback", "Unable to parse evaluation.")),
        }

    except json.JSONDecodeError:
        return {
            "score": 50,
            "correct": False,
            "feedback": f"I reviewed your work but had trouble scoring precisely. Here's my analysis:\n\n{response.text if 'response' in dir() else 'Could not get response.'}",
        }
    except Exception as e:
        return {
            "score": 0,
            "correct": False,
            "feedback": f"⚠️ Error evaluating math: {str(e)}",
        }


def _build_system_prompt(context: dict = None, student_stats: dict = None) -> str:
    """Build the full system prompt with optional context."""
    prompt = SYSTEM_PROMPT
    if context:
        status = "correctly answered" if context.get("was_correct") else "struggled with"
        prompt += f"\n\nThe student just {status} a Level {context.get('level', '?')}/5 question about {context.get('subtopic', 'unknown')}: \"{context.get('question_text', '')}\""
    if student_stats:
        prompt += f"\n\nStudent performance so far: {student_stats.get('correct', 0)}/{student_stats.get('total', 0)} correct, current adaptive level: {student_stats.get('level', 1)}/5"
    return prompt
