import subprocess

def run_script(script_name):
    subprocess.run(["python", script_name])

if __name__ == "__main__":
    scripts = ["question_a.py", "question_b.py", "question_c.py", "question_d.py"]
    for script in scripts:
        run_script(script)
