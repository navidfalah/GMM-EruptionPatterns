import subprocess
import logging

# Setup basic logging
logging.basicConfig(level=logging.INFO, filename='script_logs.log', filemode='a',
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')

def run_script(script_name):
    try:
        logging.info(f"Starting script {script_name}")
        subprocess.run(["python", script_name], check=True)
        logging.info(f"Completed script {script_name}")
    except subprocess.CalledProcessError as e:
        logging.error(f"Script {script_name} failed with error {e}")

if __name__ == "__main__":
    scripts = ["question_a.py", "question_b.py", "question_c.py", "question_d.py"]
    for script in scripts:
        run_script(script)
