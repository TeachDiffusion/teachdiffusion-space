"""TeachDiffusion — HuggingFace Spaces Demo.

A Gradio interface for generating math teaching lessons.
"""

try:
    import gradio as gr
except ImportError:
    print("Install Gradio: pip install gradio")
    exit(1)

import json


def generate_lesson(topic: str, difficulty: str, persona: str) -> tuple[str, str, str]:
    """Generate a teaching lesson and return script + explanation."""
    try:
        from teachdiffusion.pipeline.orchestrator import TeachDiffusionPipeline
        pipeline = TeachDiffusionPipeline()
        result = pipeline.generate_lesson(
            topic=topic, difficulty=difficulty, persona=persona
        )

        # Format script
        script_text = f"# Lesson: {result.topic}\n\n"
        for step in result.script.steps:
            script_text += f"## Step {step.step_number}: {step.step_type.value}\n"
            script_text += f"{step.content}\n"
            script_text += f"*Gesture: {step.gesture.value} | Pacing: {step.pacing.value}*\n\n"

        # Format explanation
        explanation_text = result.explanation.to_full_text()

        # Video prompts
        prompts_text = "\n\n".join(
            f"**Clip {i+1}:**\n{prompt}"
            for i, prompt in enumerate(result.script.get_video_prompts())
        )

        return script_text, explanation_text, prompts_text

    except Exception as e:
        return f"Error: {e}", "", ""


def get_concept_info(topic: str) -> str:
    """Get information about a concept."""
    try:
        from teachdiffusion.pipeline.orchestrator import TeachDiffusionPipeline
        pipeline = TeachDiffusionPipeline()
        info = pipeline.get_concept_info(topic)
        return json.dumps(info, indent=2)
    except Exception as e:
        return f"Error: {e}"


# Build interface
with gr.Blocks(title="TeachDiffusion", theme=gr.themes.Soft()) as demo:
    gr.Markdown(
        """
        # TeachDiffusion
        ### Open-Source Video Diffusion for Math Education
        *The right to understand is a fundamental right.*
        """
    )

    with gr.Tab("Generate Lesson"):
        with gr.Row():
            topic_input = gr.Textbox(
                label="Math Topic",
                placeholder="e.g., quadratic equations, derivatives, eigenvalues",
                value="quadratic equations",
            )
            difficulty_input = gr.Dropdown(
                choices=["elementary", "intermediate", "advanced"],
                value="intermediate",
                label="Difficulty",
            )
            persona_input = gr.Textbox(
                label="Teacher Persona",
                value="Professor Aria",
            )

        generate_btn = gr.Button("Generate Lesson", variant="primary")

        with gr.Row():
            script_output = gr.Markdown(label="Teaching Script")
            explanation_output = gr.Markdown(label="Explanation")

        prompts_output = gr.Markdown(label="Video Generation Prompts")

        generate_btn.click(
            fn=generate_lesson,
            inputs=[topic_input, difficulty_input, persona_input],
            outputs=[script_output, explanation_output, prompts_output],
        )

    with gr.Tab("Concept Explorer"):
        concept_input = gr.Textbox(
            label="Search Concept",
            placeholder="e.g., eigenvalues, limits, matrices",
        )
        explore_btn = gr.Button("Look Up")
        concept_output = gr.Code(label="Concept Info", language="json")
        explore_btn.click(
            fn=get_concept_info,
            inputs=[concept_input],
            outputs=[concept_output],
        )

    gr.Markdown(
        """
        ---
        Built by [Calyx](https://github.com/calyxish) · [GitHub](https://github.com/TeachDiffusion) · Apache 2.0
        """
    )


if __name__ == "__main__":
    demo.launch()
