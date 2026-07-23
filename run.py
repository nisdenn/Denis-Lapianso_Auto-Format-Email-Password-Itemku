input_file = "akun.txt"     # file berisi username:password
output_file = "Format Denis.txt"     # file hasil format baru

email = "NoceurStore@gfmail.com" # Masukin email random aja
email_pw = "Yangmanadah" # Random Juga

with open(input_file, "r") as f:
    lines = f.read().splitlines()

result = []

for line in lines:
    if ":" in line:
        username, password = line.split(":", 1)
        formatted = f"USM:{username}/PW:{password}/EMAIL:{email}/PW:{email_pw}"
        result.append(formatted)

with open(output_file, "w") as f:
    f.write("\n".join(result))

print("Selesai! Hasil disimpan di:", output_file)
