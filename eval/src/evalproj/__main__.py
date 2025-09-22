import os
from .text_similarity_eval import TextSimilarityEval

def main():
    # Load data
    data_path = os.path.join(os.path.dirname(__file__), "..", "..", "eval_data.json")
    data_path = os.path.abspath(data_path)
    eval_data = TextSimilarityEval.load_data(data_path)
    # Run batch evaluation
    evaluator = TextSimilarityEval()
    results = evaluator.evaluate_batch(eval_data)
    # Write results to output folder
    import json
    output_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", "output"))
    os.makedirs(output_dir, exist_ok=True)
    out_path = os.path.join(output_dir, "eval_results.json")
    with open(out_path, "w", encoding="utf-8") as f:
        json.dump(results, f, indent=2, ensure_ascii=False)
    print(f"Results written to {out_path}")

if __name__ == "__main__":
    main()
