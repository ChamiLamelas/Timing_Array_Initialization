import subprocess
import time
import numpy as np

TRIALS = 5

cscripts = ["calloc", "malloc", "memset"]
pyscripts = ["list_init", "np_empty", "np_zeros"]
jscripts = ["jarr"]
cppscripts = ["new"]
goscripts = ["array"]

for cscript in cscripts:
    subprocess.run(["gcc", "-o", cscript + ".exe", cscript + ".c"])

for jscript in jscripts:
    subprocess.run(["javac", jscript + ".java"])

for cppscript in cppscripts:
    subprocess.run(["g++", "-o", cppscript + ".exe", cppscript + ".cpp"])

subprocess.run(["go", "mod", "init", "example/array"])


def runandtime(cmd):
    results = np.empty(TRIALS)
    for t in range(TRIALS):
        ti = time.time()
        subprocess.run(cmd.split(), capture_output=True)
        tf = time.time()
        results[t] = tf - ti
    return results.mean(), results.std()


times = list()

for cscript in cscripts:
    times.append((cscript,) + runandtime("./" + cscript + ".exe"))
for pyscript in pyscripts:
    times.append((pyscript,) + runandtime("python3 " + pyscript + ".py"))
for jscript in jscripts:
    times.append((jscript,) + runandtime("java " + jscript))
for cppscript in cppscripts:
    times.append((cppscript,) + runandtime("./" + cppscript + ".exe"))
for goscript in goscripts:
    times.append((goscript,) + runandtime("go run " + goscript + ".go"))

ranking = "\n".join((s + '\t' + f'{m:.6f}' + u"\u00B1" + f'{d:.6f}')
                    for s, m, d in sorted(times, key=lambda e: e[1]))
print(ranking)
