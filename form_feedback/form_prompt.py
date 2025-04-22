def generate_physical_therapist_prompt(data):
    exercise = data["exercise"]
    rep_count = data["rep_count"]
    form_issues = data["form_issues"]
    mobility_flags = data.get("mobility_flags", [])
    experience_level = data["experience_level"]

    form_issues_str = "\n".join(
        f"- Rep {issue['rep']}: {issue['issue']}" for issue in form_issues
    )
    mobility_flags_str = ", ".join(mobility_flags) if mobility_flags else "None"

    return f"""You are a licensed physical therapist specializing in strength and mobility. 
A client has just performed {exercise} for {rep_count} reps.

Movement analysis showed:
{form_issues_str}

Mobility limitations detected: {mobility_flags_str}

The client is at an {experience_level} training level.

Based on the above, provide a short, technical, and supportive response with:
1. A clinical explanation of possible causes
2. 3 specific mobility/activation drills
3. 2 precise coaching cues
4. A short motivational closing statement

Use the calm, analytical tone of a physical therapist. Avoid hype—focus on joint function, movement correction, and long-term progress.
"""
