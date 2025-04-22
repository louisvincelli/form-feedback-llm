def format_response_blocks(response_text: str):
    sections = {
        "movement_findings": "",
        "corrective_work": "",
        "form_cues": "",
        "closing_note": ""
    }

    current_section = None
    for line in response_text.splitlines():
        line = line.strip()
        if not line:
            continue
        if "finding" in line.lower():
            current_section = "movement_findings"
        elif "drill" in line.lower() or "mobility" in line.lower():
            current_section = "corrective_work"
        elif "cue" in line.lower():
            current_section = "form_cues"
        elif "note" in line.lower():
            current_section = "closing_note"
        elif current_section:
            sections[current_section] += line + "\n"

    return sections
