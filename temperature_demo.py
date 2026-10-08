"""Temperature experiment for LLM parameters article."""

import random
from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt


PROMPT = "Write a short description of a rainy evening in Bangalore."
TEMPERATURES = [0.0, 0.3, 0.7, 1.0]


def mock_generate(prompt: str, temperature: float) -> str:
    base = [
        "Rain tapped softly on the windows while the city glowed in warm neon light.",
        "The evening smelled of wet earth and chai, as traffic hummed quietly below.",
        "Bangalore turned cinematic as the roads shimmered and the breeze cooled the air.",
        "Clouds settled over the skyline while the streets reflected a calm, silver haze.",
        "A gentle drizzle drifted across the city, mixing with distant honking and cozy lights.",
    ]
    if temperature <= 0.1:
        return base[0]
    if temperature <= 0.4:
        return base[1]
    if temperature <= 0.8:
        return base[2]
    return random.choice(base[3:])


def render_temperature_chart() -> None:
    labels = ["0.0", "0.3", "0.7", "1.0"]
    variability = ["Very low", "Low", "Moderate", "High"]
    fig, ax = plt.subplots(figsize=(8, 5))
    ax.bar(labels, [1, 2, 3, 4], color=["#60a5fa", "#7dd3fc", "#a78bfa", "#fbbf24"])
    ax.set_title("Temperature vs Output Variability")
    ax.set_xlabel("Temperature")
    ax.set_ylabel("Output variation")
    ax.set_yticks([])
    for i, label in enumerate(variability):
        ax.text(i, 4.2, label, ha="center", va="bottom", fontsize=10)
    fig.tight_layout()
    output_path = Path(__file__).with_name("temperature_variability.png")
    fig.savefig(output_path)
    plt.close(fig)
    print(f"Chart saved to: {output_path}")


if __name__ == "__main__":
    print("Temperature Experiment")
    print(f"Prompt: {PROMPT}\n")
    for temperature in TEMPERATURES:
        output = mock_generate(PROMPT, temperature)
        print(f"Temperature = {temperature}")
        print(output)
        print("-" * 60)

    render_temperature_chart()
