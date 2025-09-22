def generate_agent_eval_html_from_json(json_path, html_path):
    import json
    with open(json_path, encoding="utf-8") as f:
        data = json.load(f)
    html = [
        "<html><head><meta charset='utf-8'><title>Agent Eval Results</title>",
        "<style>table{border-collapse:collapse;}th,td{border:1px solid #ccc;padding:4px;}th{background:#eee;}</style>",
        "</head><body>",
        "<h2>Agent Evaluation Results</h2>",
        "<table>",
        "<tr>"
        "<th>Question</th><th>Actual Answer</th><th>Intent Resolution</th><th>Intent Reason</th>"
        "<th>Tool Call Accuracy</th><th>Tool Call Reason</th>"
        "<th>Task Adherence</th><th>Task Reason</th>"
        "</tr>"
    ]
    for item in data:
        agent = item.get("agent_eval", {})
        intent = agent.get("intent_resolution", {})
        tool = agent.get("tool_call_accuracy", {})
        task = agent.get("task_adherence", {})
        html.append(f"<tr>"
            f"<td>{item.get('question','')}</td>"
            f"<td>{item.get('actualAnswer','')}</td>"
            f"<td>{intent.get('intent_resolution','')}</td>"
            f"<td>{intent.get('intent_resolution_reason','')}</td>"
            f"<td>{tool.get('tool_call_accuracy','')}</td>"
            f"<td>{tool.get('tool_call_accuracy_reason','')}</td>"
            f"<td>{task.get('task_adherence','')}</td>"
            f"<td>{task.get('task_adherence_reason','')}</td>"
        "</tr>")
    html.append("</table></body></html>")
    with open(html_path, "w", encoding="utf-8") as f:
        f.write("\n".join(html))
