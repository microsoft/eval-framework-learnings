
# Import moved classes from new file
from .risk_safety_rag_eval import RiskSafetyEval, RAGEval

import os
import json
from typing import List, Dict, Any
from dotenv import load_dotenv
load_dotenv()
from azure.ai.evaluation import (
    AzureOpenAIModelConfiguration,
    SimilarityEvaluator,
    F1ScoreEvaluator,
    BleuScoreEvaluator,
    GleuScoreEvaluator,
    RougeScoreEvaluator,
    RougeType,
    MeteorScoreEvaluator,
)

class TextSimilarityEval:
    def __init__(self, model_config: AzureOpenAIModelConfiguration = None):
        if model_config is None:
            model_config = AzureOpenAIModelConfiguration(
                azure_endpoint=os.environ["AZURE_ENDPOINT"],
                api_key=os.environ.get("AZURE_API_KEY"),
                azure_deployment=os.environ.get("AZURE_DEPLOYMENT_NAME"),
                api_version=os.environ.get("AZURE_API_VERSION"),
            )
        self.similarity = SimilarityEvaluator(model_config=model_config, threshold=3)
        self.f1 = F1ScoreEvaluator(threshold=0.5)
        self.bleu = BleuScoreEvaluator(threshold=0.3)
        self.gleu = GleuScoreEvaluator(threshold=0.2)
        self.rouge = RougeScoreEvaluator(rouge_type=RougeType.ROUGE_L, precision_threshold=0.6, recall_threshold=0.5, f1_score_threshold=0.55)
        self.meteor = MeteorScoreEvaluator(threshold=0.9)

    def evaluate(self, question: str, actual: str, expected: str) -> Dict[str, Any]:
        print("Evaluating:")
        print(f"  question: {repr(question)}")
        print(f"  actual: {repr(actual)}")
        print(f"  expected: {repr(expected)}")
        results = {}

        def get_reason(res):
            if isinstance(res, dict):
                return res.get("reason", "")
            return ""

        # SimilarityEvaluator expects query, response, ground_truth
        similarity_result = self.similarity(query=question, response=actual, ground_truth=expected)
        print("RAW similarity_result:", similarity_result)

        # All other metrics expect response, ground_truth
        f1_result = self.f1(response=actual, ground_truth=expected)
        print("RAW f1_result:", f1_result)

        bleu_result = self.bleu(response=actual, ground_truth=expected)
        print("RAW bleu_result:", bleu_result)

        gleu_result = self.gleu(response=actual, ground_truth=expected)
        print("RAW gleu_result:", gleu_result)

        rouge_result = self.rouge(response=actual, ground_truth=expected)
        print("RAW rouge_result:", rouge_result)

        meteor_result = self.meteor(response=actual, ground_truth=expected)
        print("RAW meteor_result:", meteor_result)

        results["similarity"] = dict(similarity_result)
        results["similarity"]["reason"] = get_reason(similarity_result)

        results["f1"] = dict(f1_result)
        results["f1"]["reason"] = get_reason(f1_result)
        results["f1"]["f1_result"] = f1_result.get("f1_result") if isinstance(f1_result, dict) else None

        results["bleu"] = dict(bleu_result)
        results["bleu"]["reason"] = get_reason(bleu_result)
        results["bleu"]["bleu_result"] = bleu_result.get("bleu_result") if isinstance(bleu_result, dict) else None

        results["gleu"] = dict(gleu_result)
        results["gleu"]["reason"] = get_reason(gleu_result)
        results["gleu"]["gleu_result"] = gleu_result.get("gleu_result") if isinstance(gleu_result, dict) else None

        results["rouge"] = dict(rouge_result)
        results["rouge"]["reason"] = get_reason(rouge_result)
        results["rouge"]["rouge_precision_result"] = rouge_result.get("rouge_precision_result") if isinstance(rouge_result, dict) else None

        results["meteor"] = dict(meteor_result)
        results["meteor"]["reason"] = get_reason(meteor_result)
        results["meteor"]["meteor_result"] = meteor_result.get("meteor_result") if isinstance(meteor_result, dict) else None

        return results

    def evaluate_batch(self, data: List[Dict[str, str]]) -> List[Dict[str, Any]]:
        return [
            {
                **item,
                "metrics": self.evaluate(item["question"], item["actualAnswer"], item["expectedAnswer"])
            }
            for item in data
        ]

    @staticmethod
    def load_data(json_path: str) -> List[Dict[str, str]]:
        with open(json_path, "r", encoding="utf-8") as f:
            return json.load(f)

    @staticmethod
    def save_results(results: List[Dict[str, Any]], out_path: str):
        with open(out_path, "w", encoding="utf-8") as f:
            json.dump(results, f, indent=2)
