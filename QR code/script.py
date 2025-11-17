import qrcode

Github_username = "Bharatths"
Github_repoName = "Bharatths_OOPs-with-java"
Pattern = "java%20merged%20week" #Week_(N)
base_url = f"https://github.com/{Github_username}/{Github_repoName}/blob/main/{Pattern}"

for i in range(1,13):
    data = f"{base_url}{i}.pdf"
    img = qrcode.make(data)
    img.save("QR_Of_Week_"+str(i)+".png")