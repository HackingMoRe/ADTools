#!/usr/bin/env python3
import subprocess
import concurrent.futures
import time
import json
import argparse

# --- CONFIGURAZIONE ---
GITHUB_TOKEN = "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"

# --- FUNZIONI ---
def run_deploy(module, password):
    cmd = [
        "ansible-playbook", "vulnbox_deploy.yml",
        "-i", "vulnbox,",
        "-u", "root",
        "--extra-vars", f"ansible_user=root ansible_password={password} token={GITHUB_TOKEN}",
        "--extra-vars", "@.env.json",
        "--extra-vars", f'{{"modules": ["{module}"]}}'
    ]

    print(f"\n[INFO] Starting deploy for module: {module}\n{'='*50}")
    process = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True)

    for line in iter(process.stdout.readline, ''):
        print(f"[{module}] {line.strip()}")

    process.stdout.close()
    returncode = process.wait()

    if returncode == 0:
        print(f"\n[SUCCESS] {module} completed successfully.\n{'='*50}")
    else:
        print(f"\n[ERROR] {module} failed with return code {returncode}.\n{'='*50}")

    return (module, returncode == 0)

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--modules', nargs='+', help='Lista dei moduli da deployare')
    args = parser.parse_args()

    selected_modules = args.modules
    if not selected_modules:
        selected_modules =  ["common", "s4dfarm", "packmate", "threesome", "dashboard", "wisscon", "kickstarterpy"]

    start_time = time.time()

    if "common" in selected_modules:
        # Step 1: deploy common
        print("[STEP 1] Deploying 'common' module...")
        module_common_result = run_deploy("common", "root")
        if not module_common_result[1]:
            print("[FATAL] 'common' deploy failed. Aborting parallel deploys.")
            return

    # Step 2: read new root password
    try:
        with open(".env.json") as f:
            data = json.load(f)
        root_password = data["root_password"]
        print(f"\n[INFO] Retrieved updated root password from .env.json.")
    except Exception as e:
        print(f"[ERROR] Failed to read new password: {e}")
        return

    # Step 3: deploy selected modules in parallel
    print("\n[STEP 2] Deploying selected modules in parallel...\n" + "="*50)
    with concurrent.futures.ThreadPoolExecutor(max_workers=len(selected_modules)) as executor:
        futures = [executor.submit(run_deploy, mod, root_password) for mod in selected_modules]
        for future in concurrent.futures.as_completed(futures):
            module, success = future.result()
            status = "[DONE]" if success else "[FAILED]"
            print(f"[{module}] Deploy result: {status}")

    # Profiling: tempo totale
    end_time = time.time()
    duration = end_time - start_time
    minutes, seconds = divmod(duration, 60)
    print(f"\n⏱  Tempo totale di esecuzione: {int(minutes)} min {seconds:.2f} sec")

if __name__ == "__main__":
    main()
