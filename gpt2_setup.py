import os
import gpt_2_simple as gpt2

def ensure_model_exists():
    model_name = "124M"
    checkpoint_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'checkpoint')
    run_dir = os.path.join(checkpoint_dir, 'run1')
    if os.path.exists(run_dir) and os.path.isdir(run_dir):
        print("Directory run1 exists. Using files inside.")
    else:
        print("Directory run1 does not exist. Downloading " + model_name)
        gpt2.download_gpt2(model_dir='checkpoint', model_name=model_name)
        os.rename(os.path.join(checkpoint_dir, model_name), os.path.join(checkpoint_dir, "run1"))

if __name__ == "__main__":
    ensure_model_exists()
