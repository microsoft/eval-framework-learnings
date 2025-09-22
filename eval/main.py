
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "src")))
from evalproj.rag_eval import RAGEval
from evalproj.risk_safety_eval import RiskSafetyEval
from evalproj.agent_eval import AgentEval
from evalproj import __main__
from html_utils import generate_html_from_json, generate_rag_html_from_json, generate_risk_safety_html_from_json
from html_utils_agent import generate_agent_eval_html_from_json

if __name__ == "__main__":
    import json
    print("Which evaluation would you like to run?")
    print("1. Text Similarity Eval")
    print("2. RAG Eval")
    print("3. Risk/Safety Eval")
    print("4. Agent Eval")
    choice = input("Enter the number of the evaluation to run: ").strip()

    data_path = os.path.abspath(os.path.join(os.path.dirname(__file__), "eval_data.json"))
    with open(data_path, encoding="utf-8") as f:
        eval_data = json.load(f)

    if choice == "1":
        # Text Similarity Eval
        from evalproj.text_similarity_eval import TextSimilarityEval
        text_eval = TextSimilarityEval()
        results = text_eval.evaluate_batch(eval_data)
        out_json = os.path.abspath(os.path.join(os.path.dirname(__file__), "output", "eval_results.json"))
        with open(out_json, "w", encoding="utf-8") as f:
            json.dump(results, f, indent=2)
        out_html = os.path.abspath(os.path.join(os.path.dirname(__file__), "output", "eval_results.html"))
        generate_html_from_json(out_json, out_html)
        print(f"Text Similarity HTML report written to {out_html}")

    elif choice == "2":
        # RAG Eval
        rag_eval = RAGEval()
        rag_results = []
        for item in eval_data:
            query = item.get("question", "")
            response = item.get("actualAnswer", "")
            context = item.get("expectedAnswer", "")
            rag_result = {
                "id": item.get("id"),
                "question": query,
                "actualAnswer": response,
                "expectedAnswer": context,
                "retrieval": rag_eval.evaluate_retrieval(query, context),
                "groundedness": rag_eval.evaluate_groundedness(query, context, response),
                "relevance": rag_eval.evaluate_relevance(query, response),
                "response_completeness": rag_eval.evaluate_response_completeness(response, context),
            }
            rag_results.append(rag_result)
        rag_out_json = os.path.abspath(os.path.join(os.path.dirname(__file__), "output", "rag_eval_results.json"))
        with open(rag_out_json, "w", encoding="utf-8") as f:
            json.dump(rag_results, f, indent=2)
        rag_out_html = os.path.abspath(os.path.join(os.path.dirname(__file__), "output", "rag_eval_results.html"))
        generate_rag_html_from_json(rag_out_json, rag_out_html)
        print(f"RAG HTML report written to {rag_out_html}")

    elif choice == "3":
        # Risk/Safety Eval
        sub_id = os.environ.get("AZURE_SUBSCRIPTION_ID")
        rg = os.environ.get("AZURE_RESOURCE_GROUP")
        proj = os.environ.get("AZURE_PROJECT_NAME")
        if not (sub_id and rg and proj):
            print("Error: Risk/Safety Eval requires AZURE_SUBSCRIPTION_ID, AZURE_RESOURCE_GROUP, and AZURE_PROJECT_NAME to be set in your environment.")
            print("Please set these environment variables and try again.")
        else:
            risk_eval = RiskSafetyEval()
            risk_results = risk_eval.evaluate_batch(eval_data)
            risk_out_json = os.path.abspath(os.path.join(os.path.dirname(__file__), "output", "risk_safety_eval_results.json"))
            with open(risk_out_json, "w", encoding="utf-8") as f:
                json.dump(risk_results, f, indent=2)
            risk_out_html = os.path.abspath(os.path.join(os.path.dirname(__file__), "output", "risk_safety_eval_results.html"))
            generate_risk_safety_html_from_json(risk_out_json, risk_out_html)
            print(f"Risk/Safety HTML report written to {risk_out_html}")

    elif choice == "4":
        # Agent Eval
        agent_eval = AgentEval()
        agent_results = agent_eval.evaluate_batch(eval_data)
        agent_out_json = os.path.abspath(os.path.join(os.path.dirname(__file__), "output", "agent_eval_results.json"))
        with open(agent_out_json, "w", encoding="utf-8") as f:
            json.dump(agent_results, f, indent=2)
        agent_out_html = os.path.abspath(os.path.join(os.path.dirname(__file__), "output", "agent_eval_results.html"))
        generate_agent_eval_html_from_json(agent_out_json, agent_out_html)
        print(f"Agent HTML report written to {agent_out_html}")

    else:
        print("Invalid choice. Exiting.")
