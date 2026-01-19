import streamlit as st
import streamlit.components.v1 as components

# --- Page config (must be first Streamlit command) ---
st.set_page_config(
    page_title="Fullscreen HTML App",
    layout="wide",
    initial_sidebar_state="collapsed",
)

# --- Hide Streamlit UI ---
hide_streamlit_style = """
<style>
#MainMenu {visibility: hidden;}
footer {visibility: hidden;}
header {visibility: hidden;}
[data-testid="stSidebar"] {display: none;}
</style>
"""
st.markdown(hide_streamlit_style, unsafe_allow_html=True)

# ---------------- HTML ----------------
html_code = """
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <title>Shouji Rating System</title>
  <link rel="stylesheet" href="style.css">
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Orbitron:wght@400..900&display=swap" rel="stylesheet"></head>
<body>

  <h1>Shouji Rating System</h1>
  <h2>A new rating concept!?</h2>

  <div class="container">

    <div class="Player_A_Container">
        <h2>Player A</h2>
        <p>Rating µ</p>
        <input id="A_mu" type="number" value="1500" placeholder="A µ (Rating)">
        <p>Deviation σ</p>
        <input id="A_sigma" type="number" value="225" placeholder="A σ (Deviation)">
        <p>Volatility ς</p>
        <input id="A_ksi" type="range" value="0" min="-1" max="1" step="0.01" placeholder="A ς (Volatility)">
    </div>

    <div class="Player_B_Container">
        <h2>Player B</h2>
        <p>Rating µ</p>
        <input id="B_mu" type="number" value="1500" placeholder="B µ (Rating)">
        <p>Deviation σ</p>
        <input id="B_sigma" type="number" value="225" placeholder="B σ (Deviation)">
        <p>Volatility ς</p>
        <input id="B_ksi" type="range" value="0" min="-1" max="1" step="0.01" placeholder="B ς (Volatility)">
    </div>

    <div class="Control_Container">
        <h2>Control Parameters</h2>
        <p>β (Variation)</p>
        <input id="beta" type="number" value="400" placeholder="β (Variation)">
        <p>α (Momentum)</p>
        <input id="alpha" type="range" value="0.5" step="0.01" min="0" max="1" placeholder="α (Momentum)">
        <p>φ (Memory)</p>
        <input id="phi" type="range" value="0.5" step="0.01" min="0" max="1" placeholder="φ (Memory)">
    </div>

    <h2>Match Result</h2>
    <select id="result">
      <option class="A_Text" value="A">A Wins</option>
      <option class="D_Text" value="D">Draw</option>
      <option class="B_Text" value="B">B Wins</option>
    </select>

    <button id="calcBtn">Calculate</button>

    <pre id="output"></pre>

  </div>

  <script src="script.js"></script>
</body>
</html>

"""

# ---------------- CSS ----------------
css_code = """
<style>
/* ================= ROOT ================= */
:root {
  --bg-color: #000064;
  --bg-color2: #6464ff;
  --container-bg: #6464ff;
  --text-color: #ffffff;
  --input-bg: #000064;
  --button-bg: #6464ff;
  --button-hover-bg: #000064;
  --pre-bg: #000064;
  --border: #ffffff;
  --base-font: "Orbitron", Arial, sans-serif;
  --title-font-weight: 900;
  --button-font-weight: 600;
  --h2-font-weight: 700;
}

/* ================= GLOBAL RESET ================= */
* {
  box-sizing: border-box;
}

body {
  margin: 0;
  font-family: var(--base-font);
  background: var(--bg-color);
  color: var(--text-color);
  text-align: center;
  text-shadow: 0 0 5px var(--text-color);
}

/* ================= CONTAINERS ================= */
.container,
.Control_Container {
  max-width: 480px;
  margin: 20px auto;
  background: var(--container-bg);
  padding: 20px;
  border-radius: 12px;
  border: 2px solid var(--border);
  box-shadow: 0 0 10px var(--border);
  text-shadow: 0 0 5px var(--border);
}

.Player_A_Container {
  max-width: 480px;
  margin: 20px auto;
  background: var(--bg-color);
  padding: 20px;
  border-radius: 12px;
  color: cyan;
  border: 2px solid cyan;
  box-shadow: 0 0 10px cyan;
  text-shadow: 0 0 5px cyan;
}

.Player_B_Container {
  max-width: 480px;
  margin: 20px auto;
  background: var(--bg-color);
  padding: 20px;
  border-radius: 12px;
  color: red;
  border: 2px solid red;
  box-shadow: 0 0 10px red;
  text-shadow: 0 0 5px red;
}

/* ================= TEXT COLORS ================= */
.A_Text {
  color: cyan;
  background-color: var(--bg-color2);
}

.B_Text {
  color: red;
  background-color: var(--bg-color2);
}

.D_Text {
  color: white;
  background-color: var(--bg-color2);
}

/* ================= HEADINGS ================= */
h1 {
  margin: 20px 0;
  font-size: 30px;
  font-weight: var(--title-font-weight);
}

h2 {
  margin-top: 15px;
  font-size: 20px;
  font-weight: var(--h2-font-weight);
}

/* ================= INPUTS & SELECTS ================= */
input[type="number"] {
  width: 100%;
  margin: 8px 0;
  padding: 10px;
  border-radius: 6px;
  font-size: 14px;
  background: var(--input-bg);
  color: var(--text-color);
  border: 2px solid var(--border);
  box-shadow: 0 0 5px var(--border);
  font-family: var(--base-font);
}

select {
  width: 100%;
  margin: 8px 0;
  padding: 10px;
  border-radius: 6px;
  font-size: 14px;
  background: var(--input-bg);
  color: var(--text-color);
  border: 2px solid var(--border);
  box-shadow: 0 0 5px var(--border);
  font-family: var(--base-font);
}

select {
  cursor: pointer;
}

/* ================= BUTTON ================= */
button {
  margin-top: 15px;
  padding: 12px;
  width: 100%;
  background: var(--button-bg);
  border: 2px solid var(--text-color);
  border-radius: 6px;
  font-size: 16px;
  font-weight: var(--button-font-weight);
  cursor: pointer;
  color: var(--text-color);
  box-shadow: 0 0 8px var(--border);
  font-family: var(--base-font);
}

button:hover {
  background: var(--button-hover-bg);
}

/* ================= OUTPUT ================= */
pre {
  margin-top: 15px;
  background: var(--pre-bg);
  color: var(--text-color);
  padding: 12px;
  border-radius: 6px;
  text-align: left;
  font-size: 14px;
  border: 2px solid var(--border);
  box-shadow: 0 0 8px var(--border);
  font-family: var(--base-font);
}

</style>
"""

# ---------------- JavaScript ----------------
js_code = """
<script>
document.getElementById("calcBtn").addEventListener("click", calculate);

function calculate() {

  // Inputs
  const Aμ = +document.getElementById("A_mu").value;
  const Bμ = +document.getElementById("B_mu").value;
  const Aσ = +document.getElementById("A_sigma").value;
  const Bσ = +document.getElementById("B_sigma").value;
  const Aς = +document.getElementById("A_ksi").value;
  const Bς = +document.getElementById("B_ksi").value;

  const β = +document.getElementById("beta").value;
  const α = +document.getElementById("alpha").value;
  const φ = +document.getElementById("phi").value;

  const result = document.getElementById("result").value;

  // Scores
  let As, Bs;
  if (result === "A") {
    As = 1;   Bs = 0;
  } else if (result === "B") {
    As = 0;   Bs = 1;
  } else {
    As = 0.5; Bs = 0.5;
  }

  // Deviation stability
  const At = Math.pow(Aσ / (Aσ + β), 1 - α);
  const Bt = Math.pow(Bσ / (Bσ + β), 1 - α);

  // Uncertainty probability
  const ρ = β * ((At + Bt) / 2);

  // Exponent factor
  const Af = Math.pow(Aσ, At);
  const Bf = Math.pow(Bσ, Bt);

  // Win probability
  const Ap = Math.atan((Aμ - Bμ) / ρ) / Math.PI + 0.5;
  const Bp = Math.atan((Bμ - Aμ) / ρ) / Math.PI + 0.5;

  // Updated ratings
  const Aμ_new = Aμ + Af * (As - Ap) + Af * Aς;
  const Bμ_new = Bμ + Bf * (Bs - Bp) + Bf * Bς;

  // Updated deviations
  const Aσ_new = φ * Aσ + β * Math.abs(Aς);
  const Bσ_new = φ * Bσ + β * Math.abs(Bς);

  // Output
  document.getElementById("output").textContent =
`=== Stats ===
Player A
New Rating (µ): ${Aμ_new.toFixed(0)}
New Deviation (σ): ${Aσ_new.toFixed(0)}
Recorded Volatility (ς): ${(Aς*100).toFixed(0)}%

Player B
New Rating (µ): ${Bμ_new.toFixed(0)}
New Deviation (σ): ${Bσ_new.toFixed(0)}
Recorded Volatility (ς): ${(Bς*100).toFixed(0)}%

Probabilities
A win probability: ${(Ap * 100).toFixed(0)}%
B win probability: ${(Bp * 100).toFixed(0)}%

Parameters
Variation (β): ${β.toFixed(0)}
Monentum (α): ${(α*100).toFixed(0)}%
Memory (φ): ${(φ*100).toFixed(0)}%
`;
}

</script>
"""

# ---------------- Render ----------------
components.html(
    css_code + html_code + js_code,
    height=1000,
    scrolling=False,
)
