---
name: marp-topic-presentation
description: "Plan and create clear, source-grounded Marp presentations that introduce a topic. Use when asked to make a presentation, slide deck, or talk in Marp/Markdown, especially in the concise, structured style of the OpenCode presentation example."
argument-hint: "Topic, audience, duration, language, and any source material"
---

# Introducing a Topic with Marp

Turn a topic into a presentation that helps a specific audience understand what it is, why it matters, and what to learn or do next. Produce a concise planning document and a Marp Markdown deck, unless the user asks for only one.

## Workflow

1. **Establish the brief.** Identify the topic, audience, purpose, language, approximate duration, and any required context or source material. Use details already supplied; ask only for missing information that would materially change the deck. Otherwise make sensible assumptions and note them in the plan.
2. **Set the scope and takeaway.** Write one sentence stating what the audience should understand or remember. Choose a beginner-friendly scope appropriate to the time; do not try to cover everything about the topic.
3. **Gather and check facts.** Prefer user-provided material and authoritative, current primary sources. Verify dates, product capabilities, prices, statistics, comparisons, and forecasts before using them. Cite factual claims on the slide or in a readable sources slide. If a claim cannot be verified, omit it or label it clearly as something to verify; never invent testimonials, numbers, citations, or capabilities.
4. **Build the plan first.** Use [the planning template](./assets/presentation-plan.template.md). Give every slide a purpose and a single main message. Check that the story moves from audience relevance to understanding, then to application and a useful conclusion.
5. **Write the deck.** Use [the Marp starter](./assets/marp-deck.template.md), adapting its visual style to the topic. Save both deliverables as editable Markdown files, normally `[topic]-presentation-plan.md` and `[topic]-presentation.md` in the user's requested directory. Keep slide text concise, use examples or diagrams where they clarify an idea, and avoid dense paragraphs. Provide meaningful alt text or captions for visual assets; do not rely on color alone.
6. **Keep the plan and deck aligned.** Match slide titles, sequence, and key messages. Keep citations traceable. Add a final references slide when there are several sources, while keeping important citations close to their claims.
7. **Validate the deliverables.** Check Marp front matter and slide separators, spelling, links, citations, slide count against duration, and consistency with the plan. If a Marp renderer is already available, render and inspect the deck; do not install tools just for this check. Report clearly if rendering was not performed. Before writing, inspect intended output paths and do not overwrite existing user files without permission.

## Suggested introduction arc

Adapt this sequence to the topic and time; it is a menu, not a mandatory checklist:

1. Title and a hook, question, or concrete example
2. Why the topic matters to this audience
3. Learning objectives or a quick roadmap
4. Definition and boundaries: what it is (and, where useful, is not)
5. Origin, context, or the problem that led to it
6. Core ideas, components, or how it works
7. A concrete example, demonstration, or short walkthrough
8. Use cases and benefits
9. Limitations, risks, trade-offs, or alternatives
10. Local or industry context when relevant and supported by evidence
11. Practical first steps, skills, or what to explore next
12. Key takeaways, questions, and references

For a product or tool, relevant sections may include setup, integrations, pricing, privacy, and alternatives. Include them only when they help the audience and current sources support the claims. Never copy unverified claims from an example deck.

## Presentation quality checklist

- The opening gives the audience a reason to care.
- The explanation progresses from familiar concepts to new ones.
- Each slide has one clear point and a useful title.
- Examples are specific, accurate, and appropriate for the audience.
- Claims, images, and quotations have appropriate attribution.
- The conclusion reinforces the takeaway rather than introducing a new topic.
- The deck is readable when projected and does not depend on unavailable fonts or remote assets.
