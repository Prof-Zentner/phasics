"""
λ Phasics — Adaptive Learning Engine
Waves & Modern Physics
"""

import streamlit as st
import time
import sys
import os
import plotly.graph_objects as go

# Ensure local modules are importable on Streamlit Cloud
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from questions import QUESTION_BANK
from engine import (
    get_next_question,
    calculate_level,
    get_ability_estimate,
    get_topic_breakdown,
    check_answer,
)
from tutor import get_tutor_response, evaluate_drawing, evaluate_math_input

# Try importing drawable canvas
try:
    from streamlit_drawable_canvas import st_canvas
    HAS_CANVAS = True
except ImportError:
    HAS_CANVAS = False

# ─── Page Config ───
st.set_page_config(
    page_title="λ Phasics",
    page_icon="〰️",
    layout="centered",
    initial_sidebar_state="collapsed",
)

# ─── Custom CSS ───
st.markdown(
    """
<style>
    @import url('https://fonts.googleapis.com/css2?family=Playfair+Display:wght@400;600;700&family=Crimson+Text:wght@400;600&family=Inter:wght@400;500;600;700&display=swap');

    /* Main background */
    .stApp {
        background: linear-gradient(135deg, #0a0a1a 0%, #1a1a3e 50%, #0d0d2b 100%);
    }

    /* Header styling */
    .phasics-header {
        text-align: center;
        padding: 1rem 0 0.5rem;
    }
    .phasics-title {
        font-family: 'Playfair Display', Georgia, serif;
        font-size: 2.4rem;
        font-weight: 700;
        background: linear-gradient(135deg, #a78bfa, #60a5fa, #f9a8d4);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        margin: 0;
    }
    .phasics-subtitle {
        font-family: 'Inter', sans-serif;
        font-size: 0.75rem;
        letter-spacing: 3px;
        text-transform: uppercase;
        color: #6b6b8a;
        margin-top: 4px;
    }

    /* Card styling */
    .quiz-card {
        background: rgba(255, 255, 255, 0.03);
        border: 1px solid rgba(255, 255, 255, 0.08);
        border-radius: 16px;
        padding: 2rem;
        margin: 1rem 0;
        box-shadow: 0 8px 32px rgba(0, 0, 0, 0.2);
    }
    .stat-card {
        background: rgba(255, 255, 255, 0.03);
        border: 1px solid rgba(255, 255, 255, 0.08);
        border-radius: 12px;
        padding: 1.2rem;
        text-align: center;
    }

    /* Level badges */
    .level-badge {
        display: inline-block;
        padding: 4px 14px;
        border-radius: 20px;
        font-family: 'Inter', sans-serif;
        font-size: 0.75rem;
        font-weight: 600;
    }
    .level-1 { background: #E8F5E9; color: #2E7D32; }
    .level-2 { background: #E3F2FD; color: #1565C0; }
    .level-3 { background: #FFF3E0; color: #E65100; }
    .level-4 { background: #F3E5F5; color: #7B1FA2; }
    .level-5 { background: #FCE4EC; color: #C62828; }

    /* Correct/incorrect feedback */
    .feedback-correct {
        background: rgba(34, 197, 94, 0.08);
        border: 1px solid rgba(34, 197, 94, 0.2);
        border-radius: 12px;
        padding: 1.2rem;
        margin: 1rem 0;
    }
    .feedback-incorrect {
        background: rgba(239, 68, 68, 0.08);
        border: 1px solid rgba(239, 68, 68, 0.2);
        border-radius: 12px;
        padding: 1.2rem;
        margin: 1rem 0;
    }

    /* Feature cards */
    .feature-grid {
        display: grid;
        grid-template-columns: 1fr 1fr 1fr;
        gap: 1rem;
        margin: 2rem 0;
    }
    .feature-card {
        background: rgba(255, 255, 255, 0.03);
        border: 1px solid rgba(255, 255, 255, 0.06);
        border-radius: 12px;
        padding: 1.4rem 1rem;
        text-align: center;
    }
    .feature-icon { font-size: 1.8rem; margin-bottom: 0.5rem; }
    .feature-title {
        font-family: 'Inter', sans-serif;
        font-size: 0.85rem;
        font-weight: 600;
        color: #c4b5fd;
    }
    .feature-desc {
        font-family: 'Inter', sans-serif;
        font-size: 0.72rem;
        color: #777;
        margin-top: 4px;
    }

    /* Progress dots */
    .progress-dot {
        display: inline-flex;
        align-items: center;
        justify-content: center;
        width: 34px;
        height: 34px;
        border-radius: 8px;
        font-family: 'Inter', sans-serif;
        font-size: 0.7rem;
        font-weight: 600;
        margin: 2px;
    }
    .dot-correct {
        background: rgba(34, 197, 94, 0.2);
        border: 1px solid rgba(34, 197, 94, 0.3);
        color: #4ade80;
    }
    .dot-incorrect {
        background: rgba(239, 68, 68, 0.2);
        border: 1px solid rgba(239, 68, 68, 0.3);
        color: #f87171;
    }

    /* Difficulty meter */
    .diff-meter {
        display: flex;
        gap: 4px;
        margin: 0.8rem 0 1.5rem;
    }
    .diff-bar {
        flex: 1;
        height: 4px;
        border-radius: 2px;
    }
    .diff-active {
        background: linear-gradient(90deg, #7c3aed, #3b82f6);
    }
    .diff-inactive {
        background: rgba(255, 255, 255, 0.06);
    }

    /* Question type label */
    .q-type-label {
        font-family: 'Inter', sans-serif;
        font-size: 0.7rem;
        text-transform: uppercase;
        letter-spacing: 2px;
        color: #7c3aed;
        margin-bottom: 0.8rem;
    }

    /* Topic tag */
    .topic-tag {
        font-family: 'Inter', sans-serif;
        font-size: 0.75rem;
        color: #6b6b8a;
    }

    /* Override Streamlit defaults */
    .stButton > button {
        font-family: 'Inter', sans-serif;
        font-weight: 600;
        border-radius: 10px;
        transition: all 0.2s;
    }
    div[data-testid="stChatMessage"] {
        font-family: 'Crimson Text', serif;
    }

    /* Hide Streamlit branding */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
</style>
""",
    unsafe_allow_html=True,
)

# ─── Session State Initialization ───
defaults = {
    "screen": "welcome",
    "history": [],
    "current_level": 1,
    "current_question": None,
    "show_explanation": False,
    "is_correct": None,
    "question_start_time": None,
    "tutor_messages": [],
    "tutor_context": None,
}
for key, val in defaults.items():
    if key not in st.session_state:
        st.session_state[key] = val

LEVEL_LABELS = {
    1: "Foundational",
    2: "Developing",
    3: "Proficient",
    4: "Advanced",
    5: "Expert",
}


# ─── Helper functions ───
def start_quiz():
    q = get_next_question(st.session_state.history, QUESTION_BANK, 1)
    st.session_state.current_question = q
    st.session_state.question_start_time = time.time()
    st.session_state.show_explanation = False
    st.session_state.is_correct = None
    st.session_state.current_level = 1
    st.session_state.screen = "quiz"


def next_question():
    q = get_next_question(
        st.session_state.history,
        QUESTION_BANK,
        st.session_state.current_level,
    )
    if q is None:
        st.session_state.screen = "dashboard"
        return
    st.session_state.current_question = q
    st.session_state.show_explanation = False
    st.session_state.is_correct = None
    st.session_state.question_start_time = time.time()


def stop_quiz():
    st.session_state.screen = "dashboard"


def open_tutor(context=None):
    st.session_state.tutor_context = context
    if context:
        status = "Great job getting it right!" if context.get("was_correct") else "Let's work through this concept together."
        greeting = f"I see you're working on a question about **{context.get('subtopic', 'this topic')}**. {status} What would you like to understand better?"
    else:
        greeting = "Hi! I'm your AI physics tutor for Waves and Modern Physics. Ask me anything about SHM, standing waves, harmonics, or any concept you're working on."
    st.session_state.tutor_messages = [{"role": "assistant", "content": greeting}]
    st.session_state.screen = "tutor"


# ─── Initialize Gemini Key in session state ───
if "gemini_key_stored" not in st.session_state:
    st.session_state["gemini_key_stored"] = ""

# ─── Sidebar ───
with st.sidebar:
    st.markdown("### ⚙️ Settings")

    # Check for Streamlit secrets first
    secret_key = ""
    try:
        if "GEMINI_API_KEY" in st.secrets:
            secret_key = st.secrets["GEMINI_API_KEY"]
    except Exception:
        pass

    # If we have a secret, use it directly
    if secret_key:
        st.session_state["gemini_key_stored"] = secret_key
        st.success("✓ API key loaded from secrets", icon="🔑")
    else:
        # Manual input — use a callback to store the key
        def _save_key():
            val = st.session_state.get("_gemini_key_widget", "")
            if val:
                st.session_state["gemini_key_stored"] = val

        st.text_input(
            "Gemini API Key",
            value=st.session_state["gemini_key_stored"],
            type="password",
            help="Get a free key at ai.google.dev",
            key="_gemini_key_widget",
            on_change=_save_key,
        )

        if st.session_state["gemini_key_stored"]:
            st.success("✓ API key set", icon="🔑")
        else:
            st.warning("Enter a Gemini API key for AI features (drawing eval, math review, tutor)")

    st.markdown("---")
    st.markdown(
        "<small style='color:#666'>λ Phasics v1.0<br>Adaptive Learning Engine</small>",
        unsafe_allow_html=True,
    )

# Global reference to the key — persists across reruns
gemini_key = st.session_state.get("gemini_key_stored", "")


# ─── Header ───
st.markdown(
    """
<div class="phasics-header">
    <div class="phasics-title">λ Phasics</div>
    <div class="phasics-subtitle">Adaptive Learning Engine</div>
</div>
""",
    unsafe_allow_html=True,
)

# Navigation (show after welcome)
if st.session_state.screen != "welcome":
    cols = st.columns([1, 1, 1, 2])
    with cols[0]:
        if st.button("📝 Quiz", use_container_width=True):
            if st.session_state.current_question:
                st.session_state.screen = "quiz"
            else:
                start_quiz()
            st.rerun()
    with cols[1]:
        if st.button("📊 Progress", use_container_width=True):
            st.session_state.screen = "dashboard"
            st.rerun()
    with cols[2]:
        if st.button("🤖 Tutor", use_container_width=True):
            open_tutor()
            st.rerun()

st.markdown("---")

# ═══════════════════════════════════════════════════════════
# WELCOME SCREEN
# ═══════════════════════════════════════════════════════════
if st.session_state.screen == "welcome":
    st.markdown("<br>", unsafe_allow_html=True)

    col1, col2, col3 = st.columns([1, 3, 1])
    with col2:
        st.markdown(
            "<h2 style='text-align:center; font-family: Playfair Display, serif; font-size: 2.2rem; margin-bottom: 0.5rem;'>Waves & Modern Physics</h2>",
            unsafe_allow_html=True,
        )
        st.markdown(
            "<p style='text-align:center; color: #aaa; font-size: 1.05rem; line-height: 1.6;'>Adaptive learning that meets you where you are.</p>",
            unsafe_allow_html=True,
        )
        st.markdown(
            "<p style='text-align:center; color: #777; font-size: 0.85rem; line-height: 1.6; max-width: 450px; margin: 0 auto;'>Questions adapt in real time — getting harder as you improve and easier when you need more practice. Always working at your edge.</p>",
            unsafe_allow_html=True,
        )

    st.markdown(
        """
    <div class="feature-grid">
        <div class="feature-card">
            <div class="feature-icon">🎯</div>
            <div class="feature-title">Adaptive</div>
            <div class="feature-desc">Difficulty adjusts to you</div>
        </div>
        <div class="feature-card">
            <div class="feature-icon">📊</div>
            <div class="feature-title">Diagnostic</div>
            <div class="feature-desc">See exactly where you're weak</div>
        </div>
        <div class="feature-card">
            <div class="feature-icon">🤖</div>
            <div class="feature-title">AI Tutor</div>
            <div class="feature-desc">Get help when you're stuck</div>
        </div>
    </div>
    """,
        unsafe_allow_html=True,
    )

    st.markdown(
        "<p style='text-align:center; color: #666; font-size: 0.8rem; margin-bottom: 1rem;'><strong style='color:#888;'>Pilot Module:</strong> SHM & Standing Waves</p>",
        unsafe_allow_html=True,
    )

    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        if st.button("Begin Assessment →", use_container_width=True, type="primary"):
            start_quiz()
            st.rerun()


# ═══════════════════════════════════════════════════════════
# QUIZ SCREEN
# ═══════════════════════════════════════════════════════════
elif st.session_state.screen == "quiz" and st.session_state.current_question:
    q = st.session_state.current_question
    history = st.session_state.history
    level = st.session_state.current_level
    correct_count = sum(1 for h in history if h["correct"])

    # Status bar
    status_cols = st.columns([3, 2, 1])
    with status_cols[0]:
        q_num = len(history) + (0 if st.session_state.show_explanation else 1)
        level_label = LEVEL_LABELS.get(level, "?")
        st.markdown(
            f"""<span class="topic-tag">Q{q_num}</span> &nbsp;
            <span class="level-badge level-{level}">{level_label} (L{level})</span> &nbsp;
            <span class="topic-tag">{q['topic']} → {q['subtopic']}</span>""",
            unsafe_allow_html=True,
        )
    with status_cols[1]:
        st.markdown(
            f"<span class='topic-tag'>{correct_count}/{len(history)} correct</span>",
            unsafe_allow_html=True,
        )
    with status_cols[2]:
        if st.button("■ Stop", type="secondary", key="stop_quiz"):
            stop_quiz()
            st.rerun()

    # Difficulty meter
    bars = "".join(
        f'<div class="diff-bar {"diff-active" if i <= level else "diff-inactive"}"></div>'
        for i in range(1, 6)
    )
    st.markdown(f'<div class="diff-meter">{bars}</div>', unsafe_allow_html=True)

    # Question card
    type_labels = {
        "multiple_choice": "Multiple Choice",
        "numerical": "Numerical Answer",
        "conceptual": "Conceptual Response",
    }
    st.markdown(
        f'<div class="q-type-label">{type_labels.get(q["type"], "")}</div>',
        unsafe_allow_html=True,
    )
    st.markdown(f"**{q['question']}**")
    st.markdown("")

    # ─── Answer input ───
    if not st.session_state.show_explanation:
        if q["type"] == "multiple_choice":
            options_with_letters = [
                f"{chr(65+i)}.  {opt}" for i, opt in enumerate(q["options"])
            ]
            answer = st.radio(
                "Select your answer:",
                options=range(len(q["options"])),
                format_func=lambda i: options_with_letters[i],
                key=f"mc_{q['id']}",
                label_visibility="collapsed",
            )

        elif q["type"] == "numerical":
            ncols = st.columns([2, 1])
            with ncols[0]:
                answer = st.number_input(
                    "Your answer:",
                    format="%.4f",
                    key=f"num_{q['id']}",
                    step=0.001,
                )
            with ncols[1]:
                st.markdown(
                    f"<br><span style='color:#888; font-size: 1.1rem;'>{q.get('unit', '')}</span>",
                    unsafe_allow_html=True,
                )

        elif q["type"] == "conceptual":
            answer = st.text_area(
                "Explain your reasoning:",
                key=f"concept_{q['id']}",
                height=150,
                placeholder="Use key physics concepts and reasoning...",
            )
            st.caption(f"💡 Key concepts to address: {', '.join(q.get('rubric', []))}")

        elif q["type"] == "drawing":
            st.markdown(
                f"<p style='color: #c4b5fd; font-size: 0.85rem; margin-bottom: 0.5rem;'>🎨 <strong>Drawing prompt:</strong> {q.get('drawing_prompt', q['question'])}</p>",
                unsafe_allow_html=True,
            )

            if HAS_CANVAS:
                # Drawing tools
                tool_cols = st.columns([1, 1, 1, 1])
                with tool_cols[0]:
                    drawing_mode = st.selectbox(
                        "Tool",
                        ["freedraw", "line", "circle", "rect"],
                        key=f"tool_{q['id']}",
                        format_func=lambda x: {"freedraw": "✏️ Pen", "line": "📏 Line", "circle": "⭕ Circle", "rect": "⬜ Rectangle"}.get(x, x),
                    )
                with tool_cols[1]:
                    stroke_color = st.color_picker("Color", "#60a5fa", key=f"color_{q['id']}")
                with tool_cols[2]:
                    stroke_width = st.slider("Width", 1, 8, 3, key=f"width_{q['id']}")
                with tool_cols[3]:
                    bg_color = "#1a1a2e"

                canvas_result = st_canvas(
                    fill_color="rgba(0, 0, 0, 0)",
                    stroke_width=stroke_width,
                    stroke_color=stroke_color,
                    background_color=bg_color,
                    height=350,
                    width=700,
                    drawing_mode=drawing_mode,
                    key=f"canvas_{q['id']}",
                    display_toolbar=True,
                )

                st.caption("💡 Use the toolbar above the canvas to undo or clear. Draw clearly — your sketch will be evaluated by AI.")
                if not gemini_key:
                    st.error("⚠️ **Gemini API key required** — open the sidebar (click `>` top-left) and enter your key to enable AI drawing evaluation.")

                # Store canvas data in session state
                if canvas_result and canvas_result.image_data is not None:
                    st.session_state[f"drawing_{q['id']}"] = canvas_result.image_data
            else:
                st.warning("Drawing canvas not available. Install `streamlit-drawable-canvas` for drawing features.")
                st.markdown("**Alternative:** Describe your drawing in words below:")
                answer = st.text_area(
                    "Describe your drawing:",
                    key=f"draw_text_{q['id']}",
                    height=150,
                    placeholder="Describe what you would draw...",
                )

        elif q["type"] == "math_input":
            st.markdown(
                """<p style='color: #888; font-size: 0.8rem; margin-bottom: 0.5rem;'>
                ✍️ Type your mathematical expression below. Use standard notation:<br>
                <code>√(x)</code> for square root · <code>x^2</code> for powers · <code>π</code> or <code>pi</code> for pi · <code>ω</code> or <code>omega</code> for omega<br>
                <code>sin(x)</code>, <code>cos(x)</code> for trig · <code>Δx</code> or <code>delta_x</code> for delta
                </p>""",
                unsafe_allow_html=True,
            )

            math_answer = st.text_area(
                "Your mathematical expression / derivation:",
                key=f"math_{q['id']}",
                height=120,
                placeholder="e.g., x(t) = A cos(ωt + φ)  or  v(t) = -Aω sin(ωt + φ)",
            )

            if q.get("expected_form"):
                st.caption(f"💡 Expected form example: `{q['expected_form']}`")

        st.markdown("")
        if st.button("Submit Answer", type="primary", use_container_width=True):
            # Get the answer based on type
            if q["type"] == "multiple_choice":
                user_answer = st.session_state.get(f"mc_{q['id']}", None)
                correct = check_answer(q, user_answer)
                ai_feedback = None

            elif q["type"] == "numerical":
                user_answer = st.session_state.get(f"num_{q['id']}", None)
                correct = check_answer(q, user_answer)
                ai_feedback = None

            elif q["type"] == "conceptual":
                user_answer = st.session_state.get(f"concept_{q['id']}", "")
                correct = check_answer(q, user_answer)
                ai_feedback = None

            elif q["type"] == "drawing":
                drawing_data = st.session_state.get(f"drawing_{q['id']}", None)
                ai_feedback = None
                if drawing_data is not None and HAS_CANVAS:
                    import numpy as np
                    from PIL import Image
                    # Check if the canvas actually has drawing content (not just blank)
                    img_array = drawing_data.astype("uint8")
                    # Check alpha channel — blank canvas has uniform alpha
                    has_content = np.any(img_array[:, :, 3] > 0) if img_array.shape[-1] == 4 else np.any(img_array > 0)

                    if not has_content:
                        correct = False
                        ai_feedback = "It looks like the canvas is blank. Please draw your answer before submitting."
                    elif not gemini_key:
                        correct = False
                        ai_feedback = "⚠️ Please enter your Gemini API key in the **sidebar** (click the `>` arrow in the top-left) to enable AI drawing evaluation."
                    else:
                        img = Image.fromarray(img_array, "RGBA")
                        with st.spinner("🤖 AI is evaluating your drawing..."):
                            result = evaluate_drawing(img, q, gemini_key)
                        correct = result["correct"]
                        ai_feedback = result["feedback"]
                        st.session_state[f"drawing_score_{q['id']}"] = result["score"]
                else:
                    # Fallback to text description
                    user_answer = st.session_state.get(f"draw_text_{q['id']}", "")
                    if user_answer and gemini_key:
                        # Evaluate text description via math evaluator as fallback
                        with st.spinner("🤖 AI is evaluating your description..."):
                            result = evaluate_math_input(
                                user_answer,
                                {
                                    "question": q["question"],
                                    "expected_form": q.get("explanation", ""),
                                    "eval_criteria": q.get("eval_criteria", []),
                                },
                                gemini_key,
                            )
                        correct = result["correct"]
                        ai_feedback = result["feedback"]
                    else:
                        correct = False
                        ai_feedback = "Drawing canvas was not available and no description was provided."

            elif q["type"] == "math_input":
                user_answer = st.session_state.get(f"math_{q['id']}", "")
                ai_feedback = None
                # First do basic keyword check
                basic_correct = check_answer(q, user_answer)
                # Then get detailed AI evaluation if API key available
                if gemini_key:
                    with st.spinner("🤖 AI is reviewing your math..."):
                        result = evaluate_math_input(user_answer, q, gemini_key)
                    correct = result["correct"]
                    ai_feedback = result["feedback"]
                    st.session_state[f"math_score_{q['id']}"] = result["score"]
                else:
                    correct = basic_correct
                    ai_feedback = "⚠️ Add your Gemini API key in the **sidebar** (click the `>` arrow in the top-left) for detailed AI evaluation of your math. Using basic keyword matching for now."
            else:
                user_answer = None
                correct = False
                ai_feedback = None

            st.session_state.is_correct = correct
            st.session_state.show_explanation = True
            st.session_state[f"ai_feedback_{q['id']}"] = ai_feedback

            elapsed = round(time.time() - (st.session_state.question_start_time or time.time()))
            st.session_state.history.append(
                {
                    "question_id": q["id"],
                    "correct": correct if correct is not None else False,
                    "level": q["level"],
                    "time_taken": elapsed,
                }
            )
            st.session_state.current_level = calculate_level(st.session_state.history)
            st.rerun()

    # ─── Explanation ───
    else:
        is_correct = st.session_state.is_correct
        css_class = "feedback-correct" if is_correct else "feedback-incorrect"
        icon = "✅" if is_correct else "❌"
        label = "Correct!" if is_correct else "Not quite"

        if q["type"] == "multiple_choice":
            correct_letter = chr(65 + q["correct"])
            correct_text = q["options"][q["correct"]]
            st.markdown(
                f"**Correct answer: {correct_letter}. {correct_text}**"
            )
        elif q["type"] == "numerical":
            st.markdown(
                f"**Correct answer: {q['correct']} {q.get('unit', '')}**"
            )
        elif q["type"] == "math_input" and q.get("expected_form"):
            st.markdown(
                f"**Expected form:** `{q['expected_form']}`"
            )

        # Show AI feedback if available (for drawing and math questions)
        ai_feedback = st.session_state.get(f"ai_feedback_{q['id']}", None)
        if ai_feedback:
            st.markdown(
                f"""<div class="{css_class}">
                <strong>{icon} {label}</strong><br><br>
                <strong>🤖 AI Evaluation:</strong><br>{ai_feedback}
                </div>""",
                unsafe_allow_html=True,
            )

            # Show score for drawing/math
            draw_score = st.session_state.get(f"drawing_score_{q['id']}", None)
            math_score = st.session_state.get(f"math_score_{q['id']}", None)
            score = draw_score or math_score
            if score is not None:
                score_color = "#4ade80" if score >= 70 else "#eab308" if score >= 40 else "#f87171"
                st.markdown(
                    f"<p style='font-family: Inter, sans-serif; font-size: 0.85rem;'>Score: <span style='color: {score_color}; font-weight: 700; font-size: 1.1rem;'>{score}/100</span></p>",
                    unsafe_allow_html=True,
                )

        st.markdown(
            f"""<div class="{css_class}" style="margin-top: 0.5rem;">
            <strong>📖 Full Explanation:</strong><br><br>
            {q['explanation']}
            </div>""",
            unsafe_allow_html=True,
        )

        btn_cols = st.columns([3, 1])
        with btn_cols[0]:
            if st.button("Next Question →", type="primary", use_container_width=True):
                next_question()
                st.rerun()
        with btn_cols[1]:
            if st.button("🤖 Ask Tutor", use_container_width=True):
                open_tutor(
                    {
                        "subtopic": q["subtopic"],
                        "level": q["level"],
                        "was_correct": is_correct,
                        "question_text": q["question"],
                    }
                )
                st.rerun()


# ═══════════════════════════════════════════════════════════
# DASHBOARD SCREEN
# ═══════════════════════════════════════════════════════════
elif st.session_state.screen == "dashboard":
    history = st.session_state.history

    st.markdown(
        "<h2 style='font-family: Playfair Display, serif;'>Your Progress</h2>",
        unsafe_allow_html=True,
    )

    if not history:
        st.info("Complete some questions to see your diagnostic breakdown.")
        if st.button("Start Quiz →", type="primary"):
            start_quiz()
            st.rerun()
    else:
        correct_count = sum(1 for h in history if h["correct"])
        ability = get_ability_estimate(history)
        level = st.session_state.current_level

        # Summary cards
        c1, c2, c3 = st.columns(3)
        with c1:
            st.markdown(
                f"""<div class="stat-card">
                <div style="font-size: 2.2rem; font-weight: 700; color: #c4b5fd;">{ability}%</div>
                <div style="font-size: 0.75rem; color: #888; font-family: Inter, sans-serif; margin-top: 4px;">Ability Estimate</div>
                </div>""",
                unsafe_allow_html=True,
            )
        with c2:
            st.markdown(
                f"""<div class="stat-card">
                <div style="font-size: 2.2rem; font-weight: 700; color: #4ade80;">{correct_count}/{len(history)}</div>
                <div style="font-size: 0.75rem; color: #888; font-family: Inter, sans-serif; margin-top: 4px;">Correct Answers</div>
                </div>""",
                unsafe_allow_html=True,
            )
        with c3:
            st.markdown(
                f"""<div class="stat-card">
                <div style="font-size: 2.2rem; font-weight: 700; color: #60a5fa;">L{level}</div>
                <div style="font-size: 0.75rem; color: #888; font-family: Inter, sans-serif; margin-top: 4px;">Current Level</div>
                </div>""",
                unsafe_allow_html=True,
            )

        st.markdown("<br>", unsafe_allow_html=True)

        # Topic breakdown
        st.markdown(
            "<h4 style='font-family: Inter, sans-serif; color: #aaa; font-weight: 500;'>Topic Breakdown</h4>",
            unsafe_allow_html=True,
        )

        breakdown = get_topic_breakdown(history, QUESTION_BANK)
        for topic, data in breakdown.items():
            pct = round((data["correct"] / data["total"]) * 100) if data["total"] else 0
            avg_lvl = (
                round(sum(data["levels"]) / len(data["levels"]), 1)
                if data["levels"]
                else 0
            )

            if pct >= 70:
                bar_color = "#22c55e"
            elif pct >= 40:
                bar_color = "#eab308"
            else:
                bar_color = "#ef4444"

            # Use plotly for a clean bar
            fig = go.Figure(
                go.Bar(
                    x=[pct],
                    y=[topic],
                    orientation="h",
                    marker_color=bar_color,
                    text=f"{data['correct']}/{data['total']} · Avg L{avg_lvl}",
                    textposition="outside",
                    textfont=dict(color="#aaa", size=12),
                )
            )
            fig.update_layout(
                xaxis=dict(range=[0, 105], visible=False),
                yaxis=dict(visible=True, tickfont=dict(color="#ddd", size=14)),
                height=60,
                margin=dict(l=0, r=80, t=0, b=0),
                paper_bgcolor="rgba(0,0,0,0)",
                plot_bgcolor="rgba(0,0,0,0)",
                bargap=0.5,
            )
            st.plotly_chart(fig, use_container_width=True, config={"displayModeBar": False})

            if pct < 50:
                st.caption(f"⚠️ **{topic}** is a weak area — consider reviewing with the AI tutor")

        # Question history
        st.markdown("<br>", unsafe_allow_html=True)
        st.markdown(
            "<h4 style='font-family: Inter, sans-serif; color: #aaa; font-weight: 500;'>Question History</h4>",
            unsafe_allow_html=True,
        )

        dots_html = ""
        for h in history:
            css = "dot-correct" if h["correct"] else "dot-incorrect"
            dots_html += f'<span class="progress-dot {css}">L{h["level"]}</span>'
        st.markdown(dots_html, unsafe_allow_html=True)

        st.markdown("<br>", unsafe_allow_html=True)
        if st.button("Continue Quiz →", type="primary", use_container_width=True):
            next_question()
            st.session_state.screen = "quiz"
            st.rerun()


# ═══════════════════════════════════════════════════════════
# AI TUTOR SCREEN
# ═══════════════════════════════════════════════════════════
elif st.session_state.screen == "tutor":
    tutor_cols = st.columns([3, 1])
    with tutor_cols[0]:
        st.markdown(
            "<h3 style='font-family: Playfair Display, serif;'>🤖 AI Physics Tutor</h3>",
            unsafe_allow_html=True,
        )
    with tutor_cols[1]:
        st.markdown(
            "<p style='text-align:right; font-size: 0.72rem; color: #666; font-family: Inter, sans-serif; margin-top: 12px;'>Powered by Gemini · Socratic method</p>",
            unsafe_allow_html=True,
        )

    # Display chat history
    for msg in st.session_state.tutor_messages:
        with st.chat_message(msg["role"]):
            st.markdown(msg["content"])

    # Chat input
    if prompt := st.chat_input("Ask about SHM, standing waves, harmonics..."):
        # Add user message
        st.session_state.tutor_messages.append({"role": "user", "content": prompt})
        with st.chat_message("user"):
            st.markdown(prompt)

        # Get tutor response
        with st.chat_message("assistant"):
            with st.spinner("Thinking..."):
                history = st.session_state.history
                stats = {
                    "correct": sum(1 for h in history if h["correct"]),
                    "total": len(history),
                    "level": st.session_state.current_level,
                }
                response = get_tutor_response(
                    user_message=prompt,
                    chat_history=st.session_state.tutor_messages[:-1],  # exclude the just-added user msg
                    context=st.session_state.tutor_context,
                    student_stats=stats if history else None,
                    api_key=gemini_key,
                )
                st.markdown(response)
                st.session_state.tutor_messages.append(
                    {"role": "assistant", "content": response}
                )
