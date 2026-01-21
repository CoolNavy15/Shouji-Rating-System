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
  const Af = Math.pow(β, At);
  const Bf = Math.pow(β, Bt);

  // Win probability
  const Ap = Math.atan((Aμ - Bμ) / ρ) / Math.PI + 0.5;
  const Bp = Math.atan((Bμ - Aμ) / ρ) / Math.PI + 0.5;

  // Updated ratings
  const Aμ_new = Aμ + Af * (As - Ap) + Af * Aς;
  const Bμ_new = Bμ + Bf * (Bs - Bp) + Bf * Bς;

  // Updated deviations
  const Aσ_new = φ * Aσ + Aσ * Math.abs(Aς);
  const Bσ_new = φ * Bσ + Bσ * Math.abs(Bς);

  // Output
  document.getElementById("output").textContent =
`=== Stats ===
Player A
  New Rating µ: ${Aμ_new.toFixed(0)}
  New Deviation σ: ${Aσ_new.toFixed(0)}
  Recorded Volatility ς: ${(Aς*100).toFixed(0)}%

Player B
  New Rating µ: ${Bμ_new.toFixed(0)}
  New Deviation σ: ${Bσ_new.toFixed(0)}
  Recorded Volatility ς: ${(Bς*100).toFixed(0)}%

Probabilities
  A win probability: ${(Ap * 100).toFixed(0)}%
  B win probability: ${(Bp * 100).toFixed(0)}%

Parameters
  Monentum α: ${(α*100).toFixed(0)}%
  Memory φ: ${(φ*100).toFixed(0)}%
`;
}
