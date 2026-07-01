import subprocess

print("Getting weather...")
subprocess.run(["python3", "scripts/get_weather.py"])

print("Loading database...")
subprocess.run(["python3", "scripts/load_weather.py"])

print("Creating report...")
subprocess.run(["python3", "scripts/check_data.py"])

print("Pipeline finished")