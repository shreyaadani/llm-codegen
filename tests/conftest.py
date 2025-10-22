# tests/conftest.py
import os, importlib.util, pathlib, pytest

def get_model_dir():
    model_dir = pathlib.Path(os.environ.get("MODEL_DIR", "tasks_gpt")).resolve()
    print(f"[DEBUG] Using model directory: {model_dir}")  # <-- Add this line
    return model_dir

def load_func(task_num: int, func_name: str):
    model_dir = get_model_dir()
    task_path = model_dir / f"task{task_num}.py"
    if not task_path.exists():
        raise FileNotFoundError(f"Missing file: {task_path}")
    spec = importlib.util.spec_from_file_location(f"task{task_num}", str(task_path))
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return getattr(mod, func_name)

@pytest.fixture(scope="session")
def model_dir():
    return get_model_dir()
