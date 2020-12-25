f = open('input/25a_input.txt', 'r')
lines = [line.strip() for line in f.readlines()]
f.close()

card_public_key = int(lines[0])
door_public_key = int(lines[1])

modulus = 20201227
# 20201227 is prime!

subject_num = 7

prod = 1
card_loop_size = 0
while prod != card_public_key:
    prod *= subject_num
    prod = prod % modulus
    card_loop_size += 1

prod = 1
door_loop_size = 0
while prod != door_public_key:
    prod *= subject_num
    prod = prod % modulus
    door_loop_size += 1

print(f"The card loop size is {card_loop_size}")
print(f"The door loop size is {door_loop_size}")

card_enc_key = 1
for i in range(door_loop_size):
    card_enc_key *= card_public_key
    card_enc_key = card_enc_key % modulus

door_enc_key = 1
for i in range(card_loop_size):
    door_enc_key *= door_public_key
    door_enc_key = door_enc_key % modulus

# There aren't really two encryption keys, just checking that we get the same thing...
print(f"The card enc key is {card_enc_key}")
print(f"The door enc key is {door_enc_key}")