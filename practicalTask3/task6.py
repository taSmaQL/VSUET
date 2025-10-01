sentence = ("Lorem ipsum dolor sit amet, consectetur adipiscing elit. Cras risus mi, maximus cursus elementum eget, convallis sit amet est. Nullam in scelerisque leo. Aliquam diam diam, finibus id dignissim quis.")
sentence = sentence.replace(" ","")

counts = {}
for ch in sentence:
    if ch in counts:
        counts[ch] += 1
    else:
        counts[ch] = 1

sortedCounts = sorted(counts.items(), key=lambda x: x[1], reverse=True)
top3 = sortedCounts[:3]
result = ", ".join([f"{sym} – {cnt}" for sym, cnt in top3])
print(result)