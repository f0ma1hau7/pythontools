# Open bigfile, in this example rockyou.txt
with open("rockyou.txt", "r", errors="ignore") as bigfile:
  lines = bigfile.readlines()

# Divide bigfile into ten small files
for i in range(10):
  start = i * 1434439
  stop = start + 1434439
  with open("rockyou_div_%d.txt" % (i + 1), "w") as smallfile:
    smallfile.writelines(lines[start:end])
