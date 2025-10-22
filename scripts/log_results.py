# scripts/log_results.py
import csv, os, subprocess, pathlib

def run_pytest(model_dir: str):
    env = os.environ.copy()
    env["MODEL_DIR"] = model_dir
    proc = subprocess.run(
        ["pytest", "tests", "-rA", "--disable-warnings", "--color=no"],
        text=True,
        capture_output=True,
        env=env,
    )

    stdout = proc.stdout.strip().splitlines()
    # grab the final non-empty line
    summary = next((l for l in reversed(stdout) if l.strip()), "")
    print(f"{model_dir} summary line:\n{summary}\n")

    parts = {"passed": 0, "failed": 0, "skipped": 0, "errors": 0}
    for word in summary.replace(",", "").split():
        if word.isdigit():
            # e.g. 29 passed -> key 'passed'
            idx = summary.replace(",", "").split().index(word)
            if idx + 1 < len(summary.split()):
                label = summary.split()[idx + 1].lower()
                if label.startswith("pass"):
                    parts["passed"] = int(word)
                elif label.startswith("fail"):
                    parts["failed"] = int(word)
                elif label.startswith("skip"):
                    parts["skipped"] = int(word)
                elif label.startswith("err"):
                    parts["errors"] = int(word)

    total = sum(parts.values())
    pct = round(100 * parts["passed"] / total, 1) if total else 0.0
    return model_dir, parts, total, pct

if __name__ == "__main__":
    pathlib.Path("results/eval").mkdir(parents=True, exist_ok=True)
    csv_path = "results/eval/self_repair_results.csv"

    with open(csv_path, "w", newline="") as f:
        w = csv.writer(f)
        w.writerow(["ModelDir", "Passed", "Failed", "Skipped", "Errors", "Total", "PassPercent"])
        for md in ("tasks_gpt", "tasks_gemini"):
            model, parts, total, pct = run_pytest(md)
            print(f"{model}: {parts['passed']}/{total} ({pct}%)")
            w.writerow([model, parts["passed"], parts["failed"], parts["skipped"],
                        parts["errors"], total, pct])
    print(f"Results written to {csv_path}") 