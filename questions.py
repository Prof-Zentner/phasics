"""
Phasics — Full Course Question Bank
Waves & Modern Physics — 25 subtopics, ~100 questions
All questions use $...$ for inline LaTeX rendering.
"""

QUESTION_BANK = [
    # ╔═══════════════════════════════════════════════════════════╗
    # ║  1. SHM FOUNDATIONS                                      ║
    # ╚═══════════════════════════════════════════════════════════╝
    {
        "id": "shm-f1", "topic": "Simple Harmonic Motion", "subtopic": "SHM Foundations", "level": 1,
        "type": "multiple_choice",
        "question": "Which condition defines Simple Harmonic Motion?",
        "options": [
            "The restoring force is proportional to displacement: $F = -kx$",
            "The object moves at constant speed in a circle",
            "The acceleration is constant throughout the motion",
            "The object always returns to its starting position",
        ],
        "correct": 0,
        "explanation": "SHM requires a restoring force proportional to displacement and directed toward equilibrium: $F = -kx$, giving $a = -\\omega^2 x$.",
    },
    {
        "id": "shm-f2", "topic": "Simple Harmonic Motion", "subtopic": "SHM Foundations", "level": 1,
        "type": "multiple_choice",
        "question": "In SHM, $a(t)$ and $x(t)$ are related by $a = -\\omega^2 x$. What is the phase difference between them?",
        "options": ["$0$ (in phase)", "$\\pi/2$", "$\\pi$ (anti-phase)", "$3\\pi/2$"],
        "correct": 2,
        "explanation": "The negative sign in $a = -\\omega^2 x$ means acceleration is always opposite to displacement — they are $\\pi$ radians out of phase.",
    },
    {
        "id": "shm-f3", "topic": "Simple Harmonic Motion", "subtopic": "SHM Foundations", "level": 2,
        "type": "multiple_choice",
        "question": "For SHM with $x(t) = A\\cos(\\omega t)$, at what fraction of the period is the velocity first at its maximum magnitude?",
        "options": ["$t = 0$", "$t = T/4$", "$t = T/2$", "$t = T/8$"],
        "correct": 1,
        "explanation": "$v(t) = -A\\omega\\sin(\\omega t)$. Maximum $|v|$ when $|\\sin(\\omega t)| = 1$, first at $\\omega t = \\pi/2$, i.e. $t = T/4$.",
    },
    {
        "id": "shm-f4", "topic": "Simple Harmonic Motion", "subtopic": "SHM Foundations", "level": 3,
        "type": "numerical",
        "question": "An object in SHM has $A = 0.15$ m and $f = 2.0$ Hz. Calculate the maximum speed $v_{\\max}$ in m/s.",
        "correct": 1.885, "tolerance": 0.03, "unit": "m/s",
        "explanation": "$v_{\\max} = A\\omega = A(2\\pi f) = 0.15 \\times 2\\pi \\times 2.0 = 0.6\\pi \\approx 1.885$ m/s.",
    },
    # ╔═══════════════════════════════════════════════════════════╗
    # ║  2. SHM ENERGY                                           ║
    # ╚═══════════════════════════════════════════════════════════╝
    {
        "id": "shm-e1", "topic": "Simple Harmonic Motion", "subtopic": "SHM Energy", "level": 1,
        "type": "multiple_choice",
        "question": "In SHM, at which position is the kinetic energy maximum?",
        "options": ["At $x = A$", "At $x = 0$ (equilibrium)", "At $x = A/2$", "At $x = A/\\sqrt{2}$"],
        "correct": 1,
        "explanation": "At equilibrium ($x = 0$), all energy is kinetic: $\\text{KE}_{\\max} = \\frac{1}{2}kA^2$. PE is zero there.",
    },
    {
        "id": "shm-e2", "topic": "Simple Harmonic Motion", "subtopic": "SHM Energy", "level": 2,
        "type": "numerical",
        "question": "A $0.50$ kg mass on a spring ($k = 200$ N/m) oscillates with $A = 0.10$ m. What is the total energy in joules?",
        "correct": 1.0, "tolerance": 0.02, "unit": "J",
        "explanation": "$E = \\frac{1}{2}kA^2 = \\frac{1}{2}(200)(0.10)^2 = 1.0$ J.",
    },
    {
        "id": "shm-e3", "topic": "Simple Harmonic Motion", "subtopic": "SHM Energy", "level": 3,
        "type": "multiple_choice",
        "question": "At what displacement is $\\text{KE} = \\text{PE}$ in SHM?",
        "options": ["$x = A/2$", "$x = A/\\sqrt{2}$", "$x = A/4$", "$x = A\\sqrt{2}$"],
        "correct": 1,
        "explanation": "Setting $\\frac{1}{2}kx^2 = \\frac{1}{2}k(A^2 - x^2)$ gives $2x^2 = A^2$, so $x = A/\\sqrt{2}$.",
    },
    {
        "id": "shm-e4", "topic": "Simple Harmonic Motion", "subtopic": "SHM Energy", "level": 3,
        "type": "drawing",
        "question": "Sketch KE and PE vs displacement $x$ (from $-A$ to $+A$) for SHM. Include total energy.",
        "drawing_prompt": "Draw KE and PE vs displacement for SHM",
        "eval_criteria": ["PE is upward parabola centered at x=0", "KE is inverted parabola", "They cross at x=±A/√2", "Horizontal total energy line"],
        "explanation": "$\\text{PE} = \\frac{1}{2}kx^2$ (parabola). $\\text{KE} = \\frac{1}{2}k(A^2 - x^2)$ (inverted). They cross at $x = \\pm A/\\sqrt{2}$.",
    },
    # ╔═══════════════════════════════════════════════════════════╗
    # ║  3. SHM EQUATIONS                                        ║
    # ╚═══════════════════════════════════════════════════════════╝
    {
        "id": "shm-eq1", "topic": "Simple Harmonic Motion", "subtopic": "SHM Equations", "level": 2,
        "type": "multiple_choice",
        "question": "A particle in SHM: $x(t) = 0.12\\sin(5\\pi t + \\pi/4)$ (SI). What is $v(0)$?",
        "options": ["$0.60\\pi\\cos(\\pi/4) \\approx 1.33$ m/s", "$0.12\\cos(\\pi/4) \\approx 0.085$ m/s", "$0.60\\pi\\sin(\\pi/4)$", "$-0.60\\pi\\cos(\\pi/4)$"],
        "correct": 0,
        "explanation": "$v = 0.60\\pi\\cos(5\\pi t + \\pi/4)$. At $t=0$: $v = 0.60\\pi\\cos(\\pi/4) \\approx 1.33$ m/s.",
    },
    {
        "id": "shm-eq2", "topic": "Simple Harmonic Motion", "subtopic": "SHM Equations", "level": 3,
        "type": "math_input",
        "question": "Given $m = 0.5$ kg, $k = 200$ N/m, $A = 0.1$ m, starting at max displacement. Write $x(t)$.",
        "expected_form": "x(t) = 0.1\\cos(20t)",
        "eval_keywords": ["0.1", "cos", "20"],
        "eval_criteria": ["Amplitude 0.1 m", "ω = √(k/m) = 20 rad/s", "Uses cosine (max at t=0)"],
        "explanation": "$\\omega = \\sqrt{200/0.5} = 20$ rad/s. Starting at max → cosine: $x(t) = 0.1\\cos(20t)$.",
    },
    {
        "id": "shm-eq3", "topic": "Simple Harmonic Motion", "subtopic": "SHM Equations", "level": 4,
        "type": "math_input",
        "question": "From $x(t) = A\\cos(\\omega t + \\phi)$, derive $v(t)$ and $a(t)$.",
        "expected_form": "v(t) = -A\\omega\\sin(\\omega t+\\phi),\\; a(t) = -A\\omega^2\\cos(\\omega t+\\phi)",
        "eval_keywords": ["-A", "omega", "sin", "omega^2", "cos"],
        "eval_criteria": ["v = -Aω sin(ωt+φ)", "a = -Aω² cos(ωt+φ)", "a = -ω²x"],
        "explanation": "$v = -A\\omega\\sin(\\omega t+\\phi)$, $a = -A\\omega^2\\cos(\\omega t+\\phi) = -\\omega^2 x$.",
    },
    # ╔═══════════════════════════════════════════════════════════╗
    # ║  4. PENDULUMS                                            ║
    # ╚═══════════════════════════════════════════════════════════╝
    {
        "id": "pend1", "topic": "Pendulum & Mass-Spring", "subtopic": "Pendulum", "level": 1,
        "type": "multiple_choice",
        "question": "The period of a simple pendulum depends on:",
        "options": ["Length and $g$ only", "Mass and length", "Amplitude and mass", "Mass, length, and $g$"],
        "correct": 0,
        "explanation": "$T = 2\\pi\\sqrt{L/g}$. Period depends only on length and gravitational acceleration (for small angles).",
    },
    {
        "id": "pend2", "topic": "Pendulum & Mass-Spring", "subtopic": "Pendulum", "level": 2,
        "type": "numerical",
        "question": "A pendulum has $T = 2.00$ s on Earth ($g = 9.81$ m/s²). Find its length in meters.",
        "correct": 0.994, "tolerance": 0.02, "unit": "m",
        "explanation": "$L = gT^2/(4\\pi^2) = 9.81(4)/(4\\pi^2) \\approx 0.994$ m.",
    },
    {
        "id": "pend3", "topic": "Pendulum & Mass-Spring", "subtopic": "Pendulum", "level": 3,
        "type": "numerical",
        "question": "A pendulum of length $1.0$ m is taken to the Moon ($g_M = 1.62$ m/s²). What is its new period in seconds?",
        "correct": 4.93, "tolerance": 0.05, "unit": "s",
        "explanation": "$T = 2\\pi\\sqrt{L/g_M} = 2\\pi\\sqrt{1.0/1.62} \\approx 4.93$ s.",
    },
    {
        "id": "pend4", "topic": "Pendulum & Mass-Spring", "subtopic": "Pendulum", "level": 4,
        "type": "multiple_choice",
        "question": "A physical (compound) pendulum oscillates about a pivot. Its period is $T = 2\\pi\\sqrt{I/(mgh)}$. Compared to a simple pendulum of length $h$, the physical pendulum's period is:",
        "options": ["Always longer", "Always shorter", "Equal", "Longer if $I > mh^2$, shorter otherwise"],
        "correct": 3,
        "explanation": "Compare: $T_{\\text{phys}} = 2\\pi\\sqrt{I/(mgh)}$ vs $T_{\\text{simple}} = 2\\pi\\sqrt{h/g}$. If $I > mh^2$ then $T_{\\text{phys}} > T_{\\text{simple}}$.",
    },
    # ╔═══════════════════════════════════════════════════════════╗
    # ║  5. MASS-SPRING SYSTEMS                                  ║
    # ╚═══════════════════════════════════════════════════════════╝
    {
        "id": "ms1", "topic": "Pendulum & Mass-Spring", "subtopic": "Mass-Spring", "level": 1,
        "type": "numerical",
        "question": "A $0.25$ kg mass on a spring ($k = 100$ N/m) oscillates. Find the period $T$ in seconds.",
        "correct": 0.314, "tolerance": 0.005, "unit": "s",
        "explanation": "$T = 2\\pi\\sqrt{m/k} = 2\\pi\\sqrt{0.25/100} = 2\\pi(0.05) \\approx 0.314$ s.",
    },
    {
        "id": "ms2", "topic": "Pendulum & Mass-Spring", "subtopic": "Mass-Spring", "level": 2,
        "type": "numerical",
        "question": "Two springs in parallel ($k_1 = 200$ N/m, $k_2 = 300$ N/m) support a $2.0$ kg block. Find the oscillation frequency $f$ in Hz.",
        "correct": 2.52, "tolerance": 0.05, "unit": "Hz",
        "explanation": "$k_{\\text{eff}} = 500$ N/m. $f = \\frac{1}{2\\pi}\\sqrt{k_{\\text{eff}}/m} = \\frac{1}{2\\pi}\\sqrt{250} \\approx 2.52$ Hz.",
    },
    {
        "id": "ms3", "topic": "Pendulum & Mass-Spring", "subtopic": "Mass-Spring", "level": 3,
        "type": "multiple_choice",
        "question": "Two identical springs ($k$) in series support mass $m$. Compared to a single spring, the period is:",
        "options": ["$\\sqrt{2}$ times longer", "Twice as long", "The same", "$\\sqrt{2}$ times shorter"],
        "correct": 0,
        "explanation": "Series: $k_{\\text{eff}} = k/2$. $T = 2\\pi\\sqrt{m/k_{\\text{eff}}} = 2\\pi\\sqrt{2m/k} = \\sqrt{2} \\cdot T_{\\text{single}}$.",
    },
    {
        "id": "ms4", "topic": "Pendulum & Mass-Spring", "subtopic": "Mass-Spring", "level": 4,
        "type": "numerical",
        "question": "A $0.250$ kg mass on a spring ($k = 100$ N/m, $A = 0.08$ m). Find $|a_{\\max}|$ in m/s².",
        "correct": 32.0, "tolerance": 0.5, "unit": "m/s²",
        "explanation": "$|a_{\\max}| = \\omega^2 A = (k/m)A = (400)(0.08) = 32.0$ m/s².",
    },
    # ╔═══════════════════════════════════════════════════════════╗
    # ║  6. WAVEFORM PROPERTIES                                  ║
    # ╚═══════════════════════════════════════════════════════════╝
    {
        "id": "wf1", "topic": "Waveform", "subtopic": "Waveform", "level": 1,
        "type": "multiple_choice",
        "question": "A wave has $\\lambda = 0.50$ m and $f = 400$ Hz. What is the wave speed?",
        "options": ["$200$ m/s", "$800$ m/s", "$0.00125$ m/s", "$100$ m/s"],
        "correct": 0,
        "explanation": "$v = f\\lambda = 400 \\times 0.50 = 200$ m/s.",
    },
    {
        "id": "wf2", "topic": "Waveform", "subtopic": "Waveform", "level": 2,
        "type": "multiple_choice",
        "question": "In $y(x,t) = A\\sin(kx - \\omega t)$, the wave travels in the:",
        "options": ["$+x$ direction", "$-x$ direction", "$+y$ direction", "It's a standing wave"],
        "correct": 0,
        "explanation": "The form $kx - \\omega t$ means the wave travels in the $+x$ direction. ($kx + \\omega t$ → $-x$ direction.)",
    },
    {
        "id": "wf3", "topic": "Waveform", "subtopic": "Waveform", "level": 3,
        "type": "numerical",
        "question": "A wave is described by $y = 0.03\\sin(25x - 300t)$ (SI). Find the wavelength $\\lambda$ in meters.",
        "correct": 0.251, "tolerance": 0.005, "unit": "m",
        "explanation": "$k = 25$ rad/m. $\\lambda = 2\\pi/k = 2\\pi/25 \\approx 0.251$ m.",
    },
    {
        "id": "wf4", "topic": "Waveform", "subtopic": "Waveform", "level": 3,
        "type": "math_input",
        "question": "Write the wave equation for a wave with $A = 0.05$ m, $\\lambda = 2.0$ m, $f = 10$ Hz, traveling in the $+x$ direction.",
        "expected_form": "y = 0.05\\sin(\\pi x - 20\\pi t)",
        "eval_keywords": ["0.05", "sin", "pi", "20"],
        "eval_criteria": ["A = 0.05 m", "k = 2π/λ = π rad/m", "ω = 2πf = 20π rad/s", "Form: kx - ωt for +x"],
        "explanation": "$k = 2\\pi/2.0 = \\pi$, $\\omega = 2\\pi(10) = 20\\pi$. $y = 0.05\\sin(\\pi x - 20\\pi t)$.",
    },
    # ╔═══════════════════════════════════════════════════════════╗
    # ║  7. DAMPED OSCILLATIONS                                  ║
    # ╚═══════════════════════════════════════════════════════════╝
    {
        "id": "damp1", "topic": "Damped Oscillations", "subtopic": "Damped Oscillations", "level": 2,
        "type": "multiple_choice",
        "question": "In a damped oscillator, the amplitude decays as $A(t) = A_0 e^{-\\gamma t}$. What does $\\gamma$ depend on?",
        "options": ["$\\gamma = b/(2m)$ where $b$ is the damping coefficient", "$\\gamma = k/m$", "$\\gamma = \\omega_0$", "$\\gamma = b/k$"],
        "correct": 0,
        "explanation": "The decay constant is $\\gamma = b/(2m)$, where $b$ is the damping coefficient and $m$ is mass.",
    },
    {
        "id": "damp2", "topic": "Damped Oscillations", "subtopic": "Damped Oscillations", "level": 3,
        "type": "multiple_choice",
        "question": "A damped oscillator loses $5\\%$ energy per cycle. How many cycles until $E < E_0/2$?",
        "options": ["10", "14", "7", "20"],
        "correct": 1,
        "explanation": "$(0.95)^n < 0.5 \\implies n > \\ln(0.5)/\\ln(0.95) \\approx 13.5$. So $n = 14$.",
    },
    {
        "id": "damp3", "topic": "Damped Oscillations", "subtopic": "Damped Oscillations", "level": 4,
        "type": "numerical",
        "question": "Damped oscillator: $m = 0.200$ kg, $k = 50.0$ N/m, $b = 0.400$ kg/s. Find the Q-factor.",
        "correct": 7.91, "tolerance": 0.15, "unit": "",
        "explanation": "$Q = \\sqrt{mk}/b = \\sqrt{10}/0.400 \\approx 7.91$.",
    },
    {
        "id": "damp4", "topic": "Damped Oscillations", "subtopic": "Damped Oscillations", "level": 5,
        "type": "multiple_choice",
        "question": "For critical damping, the condition is:",
        "options": ["$b^2 = 4mk$", "$b^2 > 4mk$", "$b^2 < 4mk$", "$b = 2\\pi\\sqrt{mk}$"],
        "correct": 0,
        "explanation": "Critical damping: $b^2 = 4mk$ (or $\\gamma = \\omega_0$). Returns to equilibrium fastest without oscillating.",
    },
    # ╔═══════════════════════════════════════════════════════════╗
    # ║  8. DAMPED PENDULUM                                      ║
    # ╚═══════════════════════════════════════════════════════════╝
    {
        "id": "dp1", "topic": "Damped Oscillations", "subtopic": "Damped Pendulum", "level": 2,
        "type": "multiple_choice",
        "question": "A damped pendulum's angular frequency $\\omega_d$ compares to its natural frequency $\\omega_0$ as:",
        "options": ["$\\omega_d < \\omega_0$", "$\\omega_d > \\omega_0$", "$\\omega_d = \\omega_0$", "Depends on amplitude"],
        "correct": 0,
        "explanation": "$\\omega_d = \\sqrt{\\omega_0^2 - \\gamma^2}$. Damping always lowers the oscillation frequency.",
    },
    {
        "id": "dp2", "topic": "Damped Oscillations", "subtopic": "Damped Pendulum", "level": 3,
        "type": "numerical",
        "question": "A pendulum ($\\omega_0 = 5.0$ rad/s) is damped with $\\gamma = 0.3$ s$^{-1}$. Find $\\omega_d$ in rad/s.",
        "correct": 4.991, "tolerance": 0.01, "unit": "rad/s",
        "explanation": "$\\omega_d = \\sqrt{\\omega_0^2 - \\gamma^2} = \\sqrt{25 - 0.09} = \\sqrt{24.91} \\approx 4.991$ rad/s.",
    },
    {
        "id": "dp3", "topic": "Damped Oscillations", "subtopic": "Damped Pendulum", "level": 4,
        "type": "conceptual",
        "question": "Explain why driving a damped pendulum at its natural frequency $\\omega_0$ produces the largest amplitude response (resonance).",
        "rubric": ["energy transfer", "maximum", "driving frequency matches natural", "amplitude grows", "energy input per cycle exceeds losses", "phase relationship"],
        "explanation": "At $\\omega_{\\text{drive}} = \\omega_0$, energy is transferred most efficiently — the driving force is always in phase with the velocity, maximizing power input. Energy input per cycle exceeds damping losses, building amplitude until a steady state is reached.",
    },
    # ╔═══════════════════════════════════════════════════════════╗
    # ║  9. WAVES ON A STRING                                    ║
    # ╚═══════════════════════════════════════════════════════════╝
    {
        "id": "ws1", "topic": "Waves on a String", "subtopic": "Waves on a String", "level": 1,
        "type": "multiple_choice",
        "question": "Wave speed on a string depends on:",
        "options": ["Tension $T$ and linear density $\\mu$", "Frequency and amplitude", "Length and mass", "Wavelength only"],
        "correct": 0,
        "explanation": "$v = \\sqrt{T/\\mu}$. Speed depends on the medium properties, not the wave's frequency or amplitude.",
    },
    {
        "id": "ws2", "topic": "Waves on a String", "subtopic": "Waves on a String", "level": 2,
        "type": "numerical",
        "question": "A string ($\\mu = 0.010$ kg/m) is under $T = 90$ N tension. Find the wave speed in m/s.",
        "correct": 94.87, "tolerance": 1, "unit": "m/s",
        "explanation": "$v = \\sqrt{T/\\mu} = \\sqrt{90/0.010} = \\sqrt{9000} \\approx 94.87$ m/s.",
    },
    {
        "id": "ws3", "topic": "Waves on a String", "subtopic": "Waves on a String", "level": 3,
        "type": "multiple_choice",
        "question": "If the tension in a string is quadrupled, the wave speed:",
        "options": ["Doubles", "Quadruples", "Increases by $\\sqrt{2}$", "Stays the same"],
        "correct": 0,
        "explanation": "$v = \\sqrt{T/\\mu}$. If $T \\to 4T$: $v' = \\sqrt{4T/\\mu} = 2\\sqrt{T/\\mu} = 2v$.",
    },
    {
        "id": "ws4", "topic": "Waves on a String", "subtopic": "Waves on a String", "level": 4,
        "type": "numerical",
        "question": "A $1.20$ m wire ($m = 9.60\\times10^{-3}$ kg, $T = 120$ N). Find $f_3$ in Hz.",
        "correct": 153.0, "tolerance": 2, "unit": "Hz",
        "explanation": "$\\mu = 8.0\\times10^{-3}$ kg/m. $v = \\sqrt{15000} \\approx 122.5$ m/s. $f_3 = 3v/(2L) \\approx 153$ Hz.",
    },
    # ╔═══════════════════════════════════════════════════════════╗
    # ║  10. STANDING WAVES                                      ║
    # ╚═══════════════════════════════════════════════════════════╝
    {
        "id": "sw1", "topic": "Standing Waves", "subtopic": "Standing Waves", "level": 1,
        "type": "multiple_choice",
        "question": "Standing waves are produced by:",
        "options": ["Superposition of two waves traveling in opposite directions", "A single wave reflecting once", "Increasing frequency continuously", "Damping"],
        "correct": 0,
        "explanation": "Standing waves result from the superposition of two identical waves traveling in opposite directions, creating fixed nodes and antinodes.",
    },
    {
        "id": "sw2", "topic": "Standing Waves", "subtopic": "Standing Waves", "level": 2,
        "type": "drawing",
        "question": "Sketch the 3rd harmonic standing wave for a string fixed at both ends. Label nodes (N) and antinodes (A).",
        "drawing_prompt": "Draw the 3rd harmonic of a string fixed at both ends",
        "eval_criteria": ["3 half-wavelengths", "4 nodes (including endpoints)", "3 antinodes", "Sinusoidal shape"],
        "explanation": "3rd harmonic: $\\lambda = 2L/3$. There are 4 nodes and 3 antinodes.",
    },
    {
        "id": "sw3", "topic": "Standing Waves", "subtopic": "Standing Waves", "level": 3,
        "type": "multiple_choice",
        "question": "An open pipe has $f_1 = 440$ Hz. If one end is closed, the new $f_1$ is:",
        "options": ["$440$ Hz", "$220$ Hz", "$880$ Hz", "$110$ Hz"],
        "correct": 1,
        "explanation": "Open: $f = v/(2L)$. Closed: $f' = v/(4L) = f/2 = 220$ Hz.",
    },
    {
        "id": "sw4", "topic": "Standing Waves", "subtopic": "Standing Waves", "level": 4,
        "type": "numerical",
        "question": "A closed tube resonates at consecutive frequencies $850$ Hz and $1190$ Hz. Find $f_1$ in Hz.",
        "correct": 170.0, "tolerance": 2, "unit": "Hz",
        "explanation": "Closed tube: odd harmonics. Consecutive differ by $2f_1 = 340$ Hz $\\implies f_1 = 170$ Hz.",
    },
    # ╔═══════════════════════════════════════════════════════════╗
    # ║  11. SOUND WAVES                                         ║
    # ╚═══════════════════════════════════════════════════════════╝
    {
        "id": "snd1", "topic": "Sound Waves", "subtopic": "Sound Waves", "level": 1,
        "type": "multiple_choice",
        "question": "Sound waves in air are:",
        "options": ["Longitudinal waves", "Transverse waves", "Both longitudinal and transverse", "Neither"],
        "correct": 0,
        "explanation": "Sound in air is a longitudinal wave — particle displacement is parallel to the direction of wave propagation.",
    },
    {
        "id": "snd2", "topic": "Sound Waves", "subtopic": "Sound Waves", "level": 2,
        "type": "numerical",
        "question": "Sound travels at $343$ m/s in air. Find the wavelength of a $440$ Hz note (A4) in meters.",
        "correct": 0.780, "tolerance": 0.005, "unit": "m",
        "explanation": "$\\lambda = v/f = 343/440 \\approx 0.780$ m.",
    },
    {
        "id": "snd3", "topic": "Sound Waves", "subtopic": "Sound Waves", "level": 3,
        "type": "numerical",
        "question": "Two speakers emit $f = 680$ Hz sound ($v = 340$ m/s). An observer at equal distance from both moves sideways. What path difference $\\Delta$ (in m) gives the first destructive interference?",
        "correct": 0.25, "tolerance": 0.01, "unit": "m",
        "explanation": "First destructive: $\\Delta = \\lambda/2 = (v/f)/2 = (340/680)/2 = 0.25$ m.",
    },
    {
        "id": "snd4", "topic": "Sound Waves", "subtopic": "Sound Waves", "level": 4,
        "type": "numerical",
        "question": "Sound intensity at $2.0$ m from a point source is $I = 0.10$ W/m². Find the intensity at $5.0$ m in W/m².",
        "correct": 0.016, "tolerance": 0.001, "unit": "W/m²",
        "explanation": "Inverse square law: $I_2 = I_1(r_1/r_2)^2 = 0.10(2/5)^2 = 0.10(0.16) = 0.016$ W/m².",
    },
    # ╔═══════════════════════════════════════════════════════════╗
    # ║  12. DOPPLER EFFECT                                      ║
    # ╚═══════════════════════════════════════════════════════════╝
    {
        "id": "dop1", "topic": "Doppler Effect", "subtopic": "Doppler Effect", "level": 2,
        "type": "multiple_choice",
        "question": "An ambulance approaches you. The siren's perceived frequency is:",
        "options": ["Higher than emitted", "Lower than emitted", "Same as emitted", "Zero"],
        "correct": 0,
        "explanation": "Approaching source compresses wavefronts → shorter $\\lambda$ → higher perceived $f$.",
    },
    {
        "id": "dop2", "topic": "Doppler Effect", "subtopic": "Doppler Effect", "level": 3,
        "type": "numerical",
        "question": "A siren ($f_s = 500$ Hz) approaches at $v_s = 30$ m/s. Speed of sound $v = 340$ m/s. Find the observed frequency $f'$ in Hz.",
        "correct": 548.4, "tolerance": 2, "unit": "Hz",
        "explanation": "$f' = f_s \\cdot \\frac{v}{v - v_s} = 500 \\cdot \\frac{340}{310} \\approx 548.4$ Hz.",
    },
    {
        "id": "dop3", "topic": "Doppler Effect", "subtopic": "Doppler Effect", "level": 4,
        "type": "numerical",
        "question": "A car ($v_s = 25$ m/s) sounds its horn ($f = 400$ Hz) while receding from a stationary observer. $v = 343$ m/s. Find $f'$ in Hz.",
        "correct": 372.8, "tolerance": 2, "unit": "Hz",
        "explanation": "$f' = f \\cdot \\frac{v}{v + v_s} = 400 \\cdot \\frac{343}{368} \\approx 372.8$ Hz.",
    },
    {
        "id": "dop4", "topic": "Doppler Effect", "subtopic": "Doppler Effect", "level": 5,
        "type": "math_input",
        "question": "Write the general Doppler formula for moving source AND moving observer (both along the line connecting them, $v$ = sound speed).",
        "expected_form": "f' = f\\frac{v \\pm v_o}{v \\mp v_s}",
        "eval_keywords": ["f", "v", "v_o", "v_s", "plus", "minus"],
        "eval_criteria": ["Numerator: v ± v_observer", "Denominator: v ∓ v_source", "Sign convention explained"],
        "explanation": "$f' = f\\frac{v \\pm v_o}{v \\mp v_s}$. Upper signs: approaching. Lower signs: receding.",
    },
    # ╔═══════════════════════════════════════════════════════════╗
    # ║  13. MUSICAL INSTRUMENTS                                 ║
    # ╚═══════════════════════════════════════════════════════════╝
    {
        "id": "mus1", "topic": "Musical Instruments", "subtopic": "Musical Instruments", "level": 2,
        "type": "multiple_choice",
        "question": "A guitar string produces its fundamental at $330$ Hz. The frequency of the 2nd harmonic is:",
        "options": ["$660$ Hz", "$330$ Hz", "$165$ Hz", "$990$ Hz"],
        "correct": 0,
        "explanation": "Strings support all harmonics: $f_n = nf_1$. $f_2 = 2(330) = 660$ Hz.",
    },
    {
        "id": "mus2", "topic": "Musical Instruments", "subtopic": "Musical Instruments", "level": 3,
        "type": "multiple_choice",
        "question": "A clarinet (closed-open pipe) and a flute (open-open pipe) have the same $f_1$. Which has richer harmonics?",
        "options": ["Flute — supports all harmonics", "Clarinet — odd harmonics give a distinctive timbre", "Both identical", "Cannot determine"],
        "correct": 1,
        "explanation": "The clarinet (closed pipe) supports only odd harmonics ($f_1, 3f_1, 5f_1\\ldots$), giving its characteristic hollow sound. The flute supports all harmonics.",
    },
    {
        "id": "mus3", "topic": "Musical Instruments", "subtopic": "Musical Instruments", "level": 3,
        "type": "numerical",
        "question": "Two guitar strings play $440$ Hz and $444$ Hz simultaneously. What is the beat frequency in Hz?",
        "correct": 4.0, "tolerance": 0.1, "unit": "Hz",
        "explanation": "$f_{\\text{beat}} = |f_1 - f_2| = |440 - 444| = 4$ Hz.",
    },
    {
        "id": "mus4", "topic": "Musical Instruments", "subtopic": "Musical Instruments", "level": 4,
        "type": "drawing",
        "question": "Sketch the 1st and 3rd harmonics of a closed-open pipe. Label nodes (N) and antinodes (A).",
        "drawing_prompt": "Draw 1st and 3rd harmonics of a closed-open pipe",
        "eval_criteria": ["Node at closed end", "Antinode at open end", "1st: quarter wavelength", "3rd: three-quarter wavelength"],
        "explanation": "Closed-open: node at closed, antinode at open. 1st: $L = \\lambda/4$. 3rd: $L = 3\\lambda/4$. Only odd harmonics.",
    },
    # ╔═══════════════════════════════════════════════════════════╗
    # ║  14. LIGHT AS A WAVE                                     ║
    # ╚═══════════════════════════════════════════════════════════╝
    {
        "id": "lw1", "topic": "Light as a Wave", "subtopic": "Light as a Wave", "level": 1,
        "type": "multiple_choice",
        "question": "In Young's double-slit experiment, the bright fringes occur when the path difference is:",
        "options": ["$m\\lambda$ ($m = 0, 1, 2\\ldots$)", "$(m + \\frac{1}{2})\\lambda$", "$m\\lambda/2$", "$m\\pi$"],
        "correct": 0,
        "explanation": "Constructive interference: $d\\sin\\theta = m\\lambda$ for integer $m$.",
    },
    {
        "id": "lw2", "topic": "Light as a Wave", "subtopic": "Light as a Wave", "level": 2,
        "type": "numerical",
        "question": "Double slit: $d = 0.20$ mm, $\\lambda = 600$ nm, screen at $L = 1.5$ m. Find the fringe spacing $\\Delta y$ in mm.",
        "correct": 4.5, "tolerance": 0.1, "unit": "mm",
        "explanation": "$\\Delta y = \\lambda L/d = (600\\times10^{-9})(1.5)/(0.20\\times10^{-3}) = 4.5\\times10^{-3}$ m $= 4.5$ mm.",
    },
    {
        "id": "lw3", "topic": "Light as a Wave", "subtopic": "Light as a Wave", "level": 3,
        "type": "multiple_choice",
        "question": "In single-slit diffraction, the first minimum occurs at $\\sin\\theta = \\lambda/a$. If the slit width $a$ is halved:",
        "options": ["Central maximum widens", "Central maximum narrows", "No change", "Fringes disappear"],
        "correct": 0,
        "explanation": "Smaller slit → larger diffraction angle → wider central maximum. $\\theta \\propto 1/a$.",
    },
    {
        "id": "lw4", "topic": "Light as a Wave", "subtopic": "Light as a Wave", "level": 4,
        "type": "numerical",
        "question": "A diffraction grating has $5000$ lines/cm. Find the angle $\\theta$ (in degrees) for the 1st-order maximum of $\\lambda = 550$ nm.",
        "correct": 15.96, "tolerance": 0.2, "unit": "°",
        "explanation": "$d = 1/5000$ cm $= 2.0\\times10^{-6}$ m. $\\sin\\theta = \\lambda/d = 550\\times10^{-9}/2.0\\times10^{-6} = 0.275$. $\\theta = \\arcsin(0.275) \\approx 15.96°$.",
    },
    # ╔═══════════════════════════════════════════════════════════╗
    # ║  15. ANGULAR RESOLUTION                                  ║
    # ╚═══════════════════════════════════════════════════════════╝
    {
        "id": "ar1", "topic": "Angular Resolution", "subtopic": "Angular Resolution", "level": 2,
        "type": "multiple_choice",
        "question": "The Rayleigh criterion for resolving two point sources through a circular aperture is:",
        "options": ["$\\theta_{\\min} = 1.22\\lambda/D$", "$\\theta_{\\min} = \\lambda/D$", "$\\theta_{\\min} = \\lambda/(2D)$", "$\\theta_{\\min} = D/\\lambda$"],
        "correct": 0,
        "explanation": "For a circular aperture: $\\theta_{\\min} = 1.22\\lambda/D$, where $D$ is the diameter.",
    },
    {
        "id": "ar2", "topic": "Angular Resolution", "subtopic": "Angular Resolution", "level": 3,
        "type": "numerical",
        "question": "A telescope ($D = 0.10$ m) observes $\\lambda = 550$ nm. Find the angular resolution $\\theta_{\\min}$ in arcseconds.",
        "correct": 1.38, "tolerance": 0.05, "unit": "arcsec",
        "explanation": "$\\theta = 1.22\\lambda/D = 1.22(550\\times10^{-9})/0.10 = 6.71\\times10^{-6}$ rad $= 6.71\\times10^{-6} \\times 206265 \\approx 1.38$ arcsec.",
    },
    {
        "id": "ar3", "topic": "Angular Resolution", "subtopic": "Angular Resolution", "level": 4,
        "type": "numerical",
        "question": "To resolve two stars separated by $0.5$ arcsec at $\\lambda = 500$ nm, what minimum telescope diameter $D$ is needed in meters?",
        "correct": 0.251, "tolerance": 0.005, "unit": "m",
        "explanation": "$\\theta = 0.5'' = 2.42\\times10^{-6}$ rad. $D = 1.22\\lambda/\\theta = 1.22(500\\times10^{-9})/2.42\\times10^{-6} \\approx 0.252$ m.",
    },
    # ╔═══════════════════════════════════════════════════════════╗
    # ║  16. THIN FILM INTERFERENCE                              ║
    # ╚═══════════════════════════════════════════════════════════╝
    {
        "id": "tf1", "topic": "Thin Film", "subtopic": "Thin Film", "level": 2,
        "type": "multiple_choice",
        "question": "Light reflects off a thin film of oil ($n = 1.40$) on water ($n = 1.33$). At the oil-air interface, the reflected wave undergoes:",
        "options": ["$\\pi$ phase shift (low to high $n$)", "No phase shift", "$\\pi/2$ phase shift", "Depends on thickness"],
        "correct": 0,
        "explanation": "Reflection at a boundary from low $n$ to high $n$ produces a $\\pi$ phase shift. Air ($n=1$) to oil ($n=1.40$): shift occurs.",
    },
    {
        "id": "tf2", "topic": "Thin Film", "subtopic": "Thin Film", "level": 3,
        "type": "numerical",
        "question": "A soap film ($n = 1.33$) appears bright green ($\\lambda = 530$ nm) in reflected light. Find the minimum non-zero thickness $t$ in nm.",
        "correct": 99.6, "tolerance": 2, "unit": "nm",
        "explanation": "Both surfaces: $\\pi$ shift (air→soap, soap→air if $n_{\\text{air}}<n_{\\text{soap}}>n_{\\text{air}}$). Wait — soap film in air: both reflections get a phase shift, so they cancel. Constructive: $2nt = m\\lambda$. Min: $t = \\lambda/(2n) = 530/(2 \\times 1.33) \\approx 199.2$ nm. Actually for soap film in air: top reflection gets π shift, bottom does NOT (high to low n). So net π shift. Constructive: $2nt = (m+1/2)\\lambda$. Min: $t = \\lambda/(4n) = 530/(4\\times1.33) \\approx 99.6$ nm.",
    },
    {
        "id": "tf3", "topic": "Thin Film", "subtopic": "Thin Film", "level": 4,
        "type": "multiple_choice",
        "question": "An anti-reflection coating ($n_c$) on glass ($n_g$) eliminates reflection for $\\lambda$ when its thickness is $t = \\lambda/(4n_c)$. For this to work, the ideal $n_c$ is:",
        "options": ["$n_c = \\sqrt{n_g}$", "$n_c = n_g/2$", "$n_c = n_g$", "$n_c = 1/n_g$"],
        "correct": 0,
        "explanation": "For equal reflection amplitudes at both surfaces (complete cancellation): $n_c = \\sqrt{n_{\\text{air}} \\cdot n_g} = \\sqrt{n_g}$.",
    },
    # ╔═══════════════════════════════════════════════════════════╗
    # ║  17. POLARIZATION                                        ║
    # ╚═══════════════════════════════════════════════════════════╝
    {
        "id": "pol1", "topic": "Polarization", "subtopic": "Polarization", "level": 1,
        "type": "multiple_choice",
        "question": "Unpolarized light passes through a polarizer. The transmitted intensity is:",
        "options": ["$I_0/2$", "$I_0$", "$I_0/4$", "Zero"],
        "correct": 0,
        "explanation": "A polarizer transmits only the component along its axis. Averaging over all orientations: $I = I_0/2$.",
    },
    {
        "id": "pol2", "topic": "Polarization", "subtopic": "Polarization", "level": 2,
        "type": "numerical",
        "question": "Polarized light ($I_0 = 100$ W/m²) passes through a polarizer at $30°$ to its polarization. Find transmitted $I$ in W/m².",
        "correct": 75.0, "tolerance": 1, "unit": "W/m²",
        "explanation": "Malus's law: $I = I_0\\cos^2\\theta = 100\\cos^2(30°) = 100(3/4) = 75$ W/m².",
    },
    {
        "id": "pol3", "topic": "Polarization", "subtopic": "Polarization", "level": 3,
        "type": "numerical",
        "question": "Unpolarized light passes through two crossed polarizers ($90°$ apart). A third polarizer at $45°$ is inserted between them. What fraction of $I_0$ is transmitted?",
        "correct": 0.125, "tolerance": 0.005, "unit": "",
        "explanation": "1st: $I_0/2$. 2nd (at $45°$): $(I_0/2)\\cos^2 45° = I_0/4$. 3rd (at $45°$ to 2nd): $(I_0/4)\\cos^2 45° = I_0/8 = 0.125I_0$.",
    },
    {
        "id": "pol4", "topic": "Polarization", "subtopic": "Polarization", "level": 4,
        "type": "numerical",
        "question": "Find Brewster's angle for light going from air into glass ($n = 1.52$) in degrees.",
        "correct": 56.66, "tolerance": 0.3, "unit": "°",
        "explanation": "$\\theta_B = \\arctan(n_2/n_1) = \\arctan(1.52) \\approx 56.66°$.",
    },
    # ╔═══════════════════════════════════════════════════════════╗
    # ║  18. BLACK BODY RADIATION                                ║
    # ╚═══════════════════════════════════════════════════════════╝
    {
        "id": "bb1", "topic": "Thermal Physics", "subtopic": "Black Body", "level": 2,
        "type": "multiple_choice",
        "question": "According to Wien's displacement law, if a star's surface temperature doubles, the peak wavelength $\\lambda_{\\max}$:",
        "options": ["Halves", "Doubles", "Quadruples", "Stays the same"],
        "correct": 0,
        "explanation": "$\\lambda_{\\max} T = b$ (constant). If $T \\to 2T$, then $\\lambda_{\\max} \\to b/(2T) = \\lambda_{\\max}/2$.",
    },
    {
        "id": "bb2", "topic": "Thermal Physics", "subtopic": "Black Body", "level": 3,
        "type": "numerical",
        "question": "The Sun's surface is $T = 5778$ K. Find $\\lambda_{\\max}$ in nm. ($b = 2.898 \\times 10^{-3}$ m·K)",
        "correct": 501.4, "tolerance": 3, "unit": "nm",
        "explanation": "$\\lambda_{\\max} = b/T = 2.898\\times10^{-3}/5778 \\approx 5.014\\times10^{-7}$ m $= 501.4$ nm.",
    },
    {
        "id": "bb3", "topic": "Thermal Physics", "subtopic": "Black Body", "level": 3,
        "type": "numerical",
        "question": "A black body at $T = 1000$ K. Using the Stefan-Boltzmann law ($\\sigma = 5.67\\times10^{-8}$ W/m²K⁴), find the radiated power per unit area in W/m².",
        "correct": 56700, "tolerance": 200, "unit": "W/m²",
        "explanation": "$P/A = \\sigma T^4 = 5.67\\times10^{-8} \\times (1000)^4 = 5.67\\times10^4 = 56700$ W/m².",
    },
    {
        "id": "bb4", "topic": "Thermal Physics", "subtopic": "Black Body", "level": 4,
        "type": "multiple_choice",
        "question": "The 'ultraviolet catastrophe' in classical physics was resolved by:",
        "options": ["Planck's quantization of energy: $E = nhf$", "Einstein's special relativity", "Maxwell's equations", "Bohr's atomic model"],
        "correct": 0,
        "explanation": "Planck proposed energy is quantized in units of $hf$, suppressing high-frequency modes and matching observed spectra.",
    },
    # ╔═══════════════════════════════════════════════════════════╗
    # ║  19. PHOTOELECTRIC EFFECT                                ║
    # ╚═══════════════════════════════════════════════════════════╝
    {
        "id": "pe1", "topic": "Light as a Particle", "subtopic": "Photoelectric", "level": 2,
        "type": "multiple_choice",
        "question": "In the photoelectric effect, increasing the light intensity (above threshold $f$):",
        "options": ["Increases the number of electrons emitted, not their max KE", "Increases the max KE of electrons", "Decreases the threshold frequency", "Has no effect"],
        "correct": 0,
        "explanation": "Intensity ↑ → more photons → more electrons. Max KE depends only on frequency: $KE_{\\max} = hf - \\phi$.",
    },
    {
        "id": "pe2", "topic": "Light as a Particle", "subtopic": "Photoelectric", "level": 3,
        "type": "numerical",
        "question": "A metal has work function $\\phi = 2.30$ eV. Find the threshold wavelength $\\lambda_0$ in nm. ($hc = 1240$ eV·nm)",
        "correct": 539.1, "tolerance": 3, "unit": "nm",
        "explanation": "$\\lambda_0 = hc/\\phi = 1240/2.30 \\approx 539.1$ nm.",
    },
    {
        "id": "pe3", "topic": "Light as a Particle", "subtopic": "Photoelectric", "level": 4,
        "type": "numerical",
        "question": "UV light ($\\lambda = 200$ nm) hits a metal ($\\phi = 4.20$ eV). Find the max KE of ejected electrons in eV.",
        "correct": 2.0, "tolerance": 0.05, "unit": "eV",
        "explanation": "$E = hc/\\lambda = 1240/200 = 6.20$ eV. $KE_{\\max} = E - \\phi = 6.20 - 4.20 = 2.00$ eV.",
    },
    {
        "id": "pe4", "topic": "Light as a Particle", "subtopic": "Photoelectric", "level": 5,
        "type": "numerical",
        "question": "Find the stopping potential $V_s$ (in V) for the above electrons ($KE_{\\max} = 2.0$ eV).",
        "correct": 2.0, "tolerance": 0.05, "unit": "V",
        "explanation": "$eV_s = KE_{\\max}$. $V_s = KE_{\\max}/e = 2.0$ eV / $e$ = $2.0$ V.",
    },
    # ╔═══════════════════════════════════════════════════════════╗
    # ║  20. PHOTON ENERGY & MOMENTUM                            ║
    # ╚═══════════════════════════════════════════════════════════╝
    {
        "id": "ph1", "topic": "Light as a Particle", "subtopic": "Photon Energy", "level": 2,
        "type": "numerical",
        "question": "Find the energy of a photon with $\\lambda = 500$ nm in eV. ($hc = 1240$ eV·nm)",
        "correct": 2.48, "tolerance": 0.02, "unit": "eV",
        "explanation": "$E = hc/\\lambda = 1240/500 = 2.48$ eV.",
    },
    {
        "id": "ph2", "topic": "Light as a Particle", "subtopic": "Photon Energy", "level": 3,
        "type": "numerical",
        "question": "Find the de Broglie wavelength of an electron ($m = 9.11\\times10^{-31}$ kg) moving at $v = 1.0\\times10^6$ m/s. ($h = 6.63\\times10^{-34}$ J·s)",
        "correct": 0.728, "tolerance": 0.01, "unit": "nm",
        "explanation": "$\\lambda = h/(mv) = 6.63\\times10^{-34}/(9.11\\times10^{-31} \\times 10^6) = 7.28\\times10^{-10}$ m $= 0.728$ nm.",
    },
    {
        "id": "ph3", "topic": "Light as a Particle", "subtopic": "Photon Energy", "level": 4,
        "type": "multiple_choice",
        "question": "In Compton scattering, a photon scatters off an electron at $\\theta = 90°$. The wavelength shift $\\Delta\\lambda$ is:",
        "options": ["$h/(m_e c) \\approx 0.00243$ nm", "$2h/(m_e c)$", "$0$", "Depends on $\\lambda$"],
        "correct": 0,
        "explanation": "$\\Delta\\lambda = \\frac{h}{m_e c}(1 - \\cos\\theta)$. At $\\theta = 90°$: $\\Delta\\lambda = h/(m_e c) = 0.00243$ nm.",
    },
    # ╔═══════════════════════════════════════════════════════════╗
    # ║  21. RADIOACTIVE DECAY                                   ║
    # ╚═══════════════════════════════════════════════════════════╝
    {
        "id": "rad1", "topic": "Radioactivity", "subtopic": "Radioactive Decay", "level": 1,
        "type": "multiple_choice",
        "question": "In alpha decay, the nucleus emits:",
        "options": ["A helium-4 nucleus ($^4_2$He)", "An electron", "A photon", "A neutron"],
        "correct": 0,
        "explanation": "Alpha particle = $^4_2$He (2 protons + 2 neutrons). $Z$ decreases by 2, $A$ by 4.",
    },
    {
        "id": "rad2", "topic": "Radioactivity", "subtopic": "Radioactive Decay", "level": 2,
        "type": "numerical",
        "question": "A sample has $N_0 = 10000$ atoms and half-life $t_{1/2} = 5.0$ days. How many remain after $15$ days?",
        "correct": 1250, "tolerance": 5, "unit": "atoms",
        "explanation": "$15$ days $= 3$ half-lives. $N = N_0/2^3 = 10000/8 = 1250$.",
    },
    {
        "id": "rad3", "topic": "Radioactivity", "subtopic": "Radioactive Decay", "level": 3,
        "type": "numerical",
        "question": "The decay constant of C-14 is $\\lambda = 3.83\\times10^{-12}$ s$^{-1}$. Find the half-life in years. ($1$ yr $= 3.156\\times10^7$ s)",
        "correct": 5734, "tolerance": 30, "unit": "years",
        "explanation": "$t_{1/2} = \\ln(2)/\\lambda = 0.693/(3.83\\times10^{-12}) = 1.81\\times10^{11}$ s $\\approx 5734$ years.",
    },
    {
        "id": "rad4", "topic": "Radioactivity", "subtopic": "Radioactive Decay", "level": 4,
        "type": "math_input",
        "question": "Write the radioactive decay equation $N(t)$ in terms of $N_0$, $\\lambda$, and $t$. Also express using half-life $t_{1/2}$.",
        "expected_form": "N(t) = N_0 e^{-\\lambda t} = N_0 (1/2)^{t/t_{1/2}}",
        "eval_keywords": ["N_0", "exp", "lambda", "half", "t"],
        "eval_criteria": ["N = N₀e^(-λt)", "Equivalent: N = N₀(1/2)^(t/t½)", "λ = ln2/t½"],
        "explanation": "$N(t) = N_0 e^{-\\lambda t} = N_0 \\left(\\frac{1}{2}\\right)^{t/t_{1/2}}$ where $\\lambda = \\ln 2/t_{1/2}$.",
    },
    # ╔═══════════════════════════════════════════════════════════╗
    # ║  22. NUCLEAR REACTIONS                                   ║
    # ╚═══════════════════════════════════════════════════════════╝
    {
        "id": "nuc1", "topic": "Radioactivity", "subtopic": "Nuclear Reactions", "level": 2,
        "type": "multiple_choice",
        "question": "In beta-minus decay, a neutron converts to:",
        "options": ["Proton + electron + antineutrino", "Proton + positron + neutrino", "Alpha particle + photon", "Two protons"],
        "correct": 0,
        "explanation": "$n \\to p + e^- + \\bar{\\nu}_e$. $Z$ increases by 1, $A$ unchanged.",
    },
    {
        "id": "nuc2", "topic": "Radioactivity", "subtopic": "Nuclear Reactions", "level": 3,
        "type": "numerical",
        "question": "A nuclear reaction has mass defect $\\Delta m = 0.0200$ u. Find the energy released in MeV. ($1$ u $= 931.5$ MeV/$c^2$)",
        "correct": 18.63, "tolerance": 0.1, "unit": "MeV",
        "explanation": "$E = \\Delta m \\cdot c^2 = 0.0200 \\times 931.5 = 18.63$ MeV.",
    },
    {
        "id": "nuc3", "topic": "Radioactivity", "subtopic": "Nuclear Reactions", "level": 4,
        "type": "multiple_choice",
        "question": "Which has higher binding energy per nucleon?",
        "options": ["Iron-56 (most stable)", "Uranium-238", "Hydrogen-1", "Helium-4"],
        "correct": 0,
        "explanation": "Fe-56 has the highest binding energy per nucleon (~8.8 MeV). Fusion of lighter nuclei and fission of heavier nuclei both move toward iron.",
    },
    # ╔═══════════════════════════════════════════════════════════╗
    # ║  23. TIME DILATION                                       ║
    # ╚═══════════════════════════════════════════════════════════╝
    {
        "id": "td1", "topic": "Relativity", "subtopic": "Time Dilation", "level": 2,
        "type": "multiple_choice",
        "question": "A spaceship moves at $v = 0.8c$ relative to Earth. Clocks on the ship, as seen from Earth:",
        "options": ["Run slower", "Run faster", "Run at the same rate", "Stop completely"],
        "correct": 0,
        "explanation": "Time dilation: $\\Delta t = \\gamma \\Delta t_0$ where $\\gamma > 1$. Moving clocks run slow as seen by stationary observers.",
    },
    {
        "id": "td2", "topic": "Relativity", "subtopic": "Time Dilation", "level": 3,
        "type": "numerical",
        "question": "A muon has proper lifetime $\\tau_0 = 2.20$ μs and moves at $v = 0.99c$. Find its dilated lifetime in μs.",
        "correct": 15.6, "tolerance": 0.3, "unit": "μs",
        "explanation": "$\\gamma = 1/\\sqrt{1 - 0.99^2} = 1/\\sqrt{0.0199} \\approx 7.09$. $\\tau = \\gamma\\tau_0 = 7.09 \\times 2.20 \\approx 15.6$ μs.",
    },
    {
        "id": "td3", "topic": "Relativity", "subtopic": "Time Dilation", "level": 4,
        "type": "numerical",
        "question": "An astronaut travels at $v = 0.95c$ for $\\Delta t = 10.0$ years (Earth time). How much time passes on the ship in years?",
        "correct": 3.12, "tolerance": 0.05, "unit": "years",
        "explanation": "$\\gamma = 1/\\sqrt{1-0.95^2} = 1/\\sqrt{0.0975} \\approx 3.203$. $\\Delta t_0 = \\Delta t/\\gamma = 10.0/3.203 \\approx 3.12$ years.",
    },
    # ╔═══════════════════════════════════════════════════════════╗
    # ║  24. LENGTH CONTRACTION                                  ║
    # ╚═══════════════════════════════════════════════════════════╝
    {
        "id": "lc1", "topic": "Relativity", "subtopic": "Length Contraction", "level": 2,
        "type": "multiple_choice",
        "question": "A $100$ m spaceship moves at $0.6c$ past Earth. Earth observers measure its length as:",
        "options": ["$80$ m", "$100$ m", "$125$ m", "$60$ m"],
        "correct": 0,
        "explanation": "$\\gamma = 1/\\sqrt{1-0.36} = 1/0.8 = 1.25$. $L = L_0/\\gamma = 100/1.25 = 80$ m.",
    },
    {
        "id": "lc2", "topic": "Relativity", "subtopic": "Length Contraction", "level": 3,
        "type": "numerical",
        "question": "A spaceship at $v = 0.90c$ has proper length $L_0 = 200$ m. Find the contracted length in meters.",
        "correct": 87.2, "tolerance": 1, "unit": "m",
        "explanation": "$\\gamma = 1/\\sqrt{1-0.81} = 1/\\sqrt{0.19} \\approx 2.294$. $L = L_0/\\gamma = 200/2.294 \\approx 87.2$ m.",
    },
    {
        "id": "lc3", "topic": "Relativity", "subtopic": "Length Contraction", "level": 4,
        "type": "multiple_choice",
        "question": "Length contraction occurs only along the:",
        "options": ["Direction of motion", "All three spatial dimensions", "Perpendicular directions", "Dimension the observer chooses"],
        "correct": 0,
        "explanation": "Contraction is only along the direction of relative motion. Perpendicular dimensions are unaffected.",
    },
    # ╔═══════════════════════════════════════════════════════════╗
    # ║  25. RELATIVISTIC ENERGY                                 ║
    # ╚═══════════════════════════════════════════════════════════╝
    {
        "id": "re1", "topic": "Relativity", "subtopic": "Relativistic Energy", "level": 2,
        "type": "multiple_choice",
        "question": "The rest energy of an electron ($m_e = 9.11\\times10^{-31}$ kg) is approximately:",
        "options": ["$0.511$ MeV", "$931.5$ MeV", "$13.6$ eV", "$1.022$ MeV"],
        "correct": 0,
        "explanation": "$E_0 = m_e c^2 = 9.11\\times10^{-31} \\times (3\\times10^8)^2 \\approx 8.2\\times10^{-14}$ J $\\approx 0.511$ MeV.",
    },
    {
        "id": "re2", "topic": "Relativity", "subtopic": "Relativistic Energy", "level": 3,
        "type": "numerical",
        "question": "An electron is accelerated to $v = 0.80c$. Find its total relativistic energy in MeV. ($m_e c^2 = 0.511$ MeV)",
        "correct": 0.852, "tolerance": 0.01, "unit": "MeV",
        "explanation": "$\\gamma = 1/\\sqrt{1-0.64} = 1/0.6 = 5/3 \\approx 1.667$. $E = \\gamma m_e c^2 = 1.667 \\times 0.511 \\approx 0.852$ MeV.",
    },
    {
        "id": "re3", "topic": "Relativity", "subtopic": "Relativistic Energy", "level": 4,
        "type": "numerical",
        "question": "A proton ($m_p c^2 = 938.3$ MeV) has kinetic energy $KE = 500$ MeV. Find its speed as a fraction of $c$.",
        "correct": 0.759, "tolerance": 0.005, "unit": "c",
        "explanation": "$E = KE + m_pc^2 = 1438.3$ MeV. $\\gamma = E/(m_pc^2) = 1.533$. $v/c = \\sqrt{1 - 1/\\gamma^2} = \\sqrt{1 - 0.4254} \\approx 0.759$.",
    },
    {
        "id": "re4", "topic": "Relativity", "subtopic": "Relativistic Energy", "level": 5,
        "type": "math_input",
        "question": "Write the relativistic energy-momentum relation linking total energy $E$, momentum $p$, and rest mass $m$.",
        "expected_form": "E^2 = (pc)^2 + (mc^2)^2",
        "eval_keywords": ["E^2", "pc", "mc^2", "squared"],
        "eval_criteria": ["E² = (pc)² + (mc²)²", "Reduces to E=mc² when p=0", "Reduces to E=pc for massless particles"],
        "explanation": "$E^2 = (pc)^2 + (mc^2)^2$. For $p=0$: $E = mc^2$. For $m=0$ (photons): $E = pc$.",
    },
]
