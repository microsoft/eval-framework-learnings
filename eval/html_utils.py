
def generate_risk_safety_html_from_json(json_path, html_path):
    import json
    with open(json_path, encoding="utf-8") as f:
        data = json.load(f)
    html = [
        "<html><head><meta charset='utf-8'><title>Risk/Safety Eval Results</title>",
        "<style>table{border-collapse:collapse;}th,td{border:1px solid #ccc;padding:4px;}th{background:#eee;}</style>",
        "</head><body>",
        "<h2>Risk/Safety Evaluation Results</h2>",
        "<table>",
        "<tr>"
        "<th>Question</th><th>Actual Answer</th><th>Expected Answer</th>"
        "<th>Hate/Unfairness</th><th>Sexual</th><th>Violence</th><th>Self-Harm</th><th>Composite</th>"
        "</tr>"
    ]
    for item in data:
        risk = item.get("risk_safety", {})
        html.append(f"<tr>"
            f"<td>{item.get('question','')}</td>"
            f"<td>{item.get('actualAnswer','')}</td>"
            f"<td>{item.get('expectedAnswer','')}</td>"
            f"<td>{risk.get('hate_unfairness', {}).get('hate_unfairness','')}</td>"
            f"<td>{risk.get('sexual', {}).get('sexual','')}</td>"
            f"<td>{risk.get('violence', {}).get('violence','')}</td>"
            f"<td>{risk.get('self_harm', {}).get('self_harm','')}</td>"
            f"<td>{risk.get('composite', {}).get('content_safety','')}</td>"
        "</tr>")
    html.append("</table></body></html>")
    with open(html_path, "w", encoding="utf-8") as f:
        f.write("\n".join(html))
def generate_html_from_json(json_path, html_path):
    import json
    with open(json_path, encoding="utf-8") as f:
        data = json.load(f)
    # Build HTML table
    html = [
        "<html><head><meta charset='utf-8'><title>Eval Results</title>",
        "<style>table{border-collapse:collapse;}th,td{border:1px solid #ccc;padding:4px;}th{background:#eee;}</style>",
        "</head><body>",
        "<h2>Evaluation Results</h2>",
        "<table>",
        "<tr>"
        "<th>Question</th><th>Actual Answer</th><th>Expected Answer</th>"
        "<th>Similarity</th><th>Similarity Reason</th>"
        "<th>F1</th><th>F1 Reason</th><th>F1 Result</th>"
        "<th>BLEU</th><th>BLEU Reason</th><th>BLEU Result</th>"
        "<th>GLEU</th><th>GLEU Reason</th><th>GLEU Result</th>"
        "<th>ROUGE</th><th>ROUGE Reason</th><th>ROUGE Precision Result</th>"
        "<th>METEOR</th><th>METEOR Reason</th><th>METEOR Result</th>"
        "</tr>"
    ]
    for item in data:
        metrics = item.get("metrics", {})
        html.append(f"<tr>"
            f"<td>{item.get('question','')}</td>"
            f"<td>{item.get('actualAnswer','')}</td>"
            f"<td>{item.get('expectedAnswer','')}</td>"
            f"<td>{metrics.get('similarity', {}).get('similarity','')}</td>"
            f"<td>{metrics.get('similarity', {}).get('reason','')}</td>"
            f"<td>{metrics.get('f1', {}).get('f1_score','')}</td>"
            f"<td>{metrics.get('f1', {}).get('reason','')}</td>"
            f"<td>{metrics.get('f1', {}).get('f1_result','')}</td>"
            f"<td>{metrics.get('bleu', {}).get('bleu_score','')}</td>"
            f"<td>{metrics.get('bleu', {}).get('reason','')}</td>"
            f"<td>{metrics.get('bleu', {}).get('bleu_result','')}</td>"
            f"<td>{metrics.get('gleu', {}).get('gleu_score','')}</td>"
            f"<td>{metrics.get('gleu', {}).get('reason','')}</td>"
            f"<td>{metrics.get('gleu', {}).get('gleu_result','')}</td>"
            f"<td>{metrics.get('rouge', {}).get('rouge_f1_score','')}</td>"
            f"<td>{metrics.get('rouge', {}).get('reason','')}</td>"
            f"<td>{metrics.get('rouge', {}).get('rouge_precision_result','')}</td>"
            f"<td>{metrics.get('meteor', {}).get('meteor_score','')}</td>"
            f"<td>{metrics.get('meteor', {}).get('reason','')}</td>"
            f"<td>{metrics.get('meteor', {}).get('meteor_result','')}</td>"
        "</tr>")
    html.append("</table></body></html>")
    with open(html_path, "w", encoding="utf-8") as f:
        f.write("\n".join(html))

def generate_rag_html_from_json(json_path, html_path):
    import json
    with open(json_path, encoding="utf-8") as f:
        data = json.load(f)
    html = [
        "<html><head><meta charset='utf-8'><title>RAG Eval Results</title>",
        "<style>table{border-collapse:collapse;}th,td{border:1px solid #ccc;padding:4px;}th{background:#eee;}</style>",
        "</head><body>",
        "<h2>RAG Evaluation Results</h2>",
        "<table>",
        "<tr>"
        "<th>ID</th><th>Question</th><th>Actual Answer</th><th>Expected Answer</th>"
        "<th>Retrieval</th><th>Retrieval Reason</th>"
        "<th>Groundedness</th><th>Groundedness Reason</th>"
        "<th>Relevance</th><th>Relevance Reason</th>"
        "<th>Response Completeness</th><th>Response Completeness Reason</th>"
        "</tr>"
    ]
    for item in data:
        html.append(f"<tr>"
            f"<td>{item.get('id','')}</td>"
            f"<td>{item.get('question','')}</td>"
            f"<td>{item.get('actualAnswer','')}</td>"
            f"<td>{item.get('expectedAnswer','')}</td>"
            f"<td>{item.get('retrieval',{}).get('retrieval','')}</td>"
            f"<td>{item.get('retrieval',{}).get('retrieval_reason','')}</td>"
            f"<td>{item.get('groundedness',{}).get('groundedness','')}</td>"
            f"<td>{item.get('groundedness',{}).get('groundedness_reason','')}</td>"
            f"<td>{item.get('relevance',{}).get('relevance','')}</td>"
            f"<td>{item.get('relevance',{}).get('relevance_reason','')}</td>"
            f"<td>{item.get('response_completeness',{}).get('response_completeness','')}</td>"
            f"<td>{item.get('response_completeness',{}).get('response_completeness_reason','')}</td>"
        "</tr>")
    html.append("</table></body></html>")
    with open(html_path, "w", encoding="utf-8") as f:
        f.write("\n".join(html))
