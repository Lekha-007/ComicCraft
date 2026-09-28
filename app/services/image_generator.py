def generate_image(prompt):
    import hashlib
    seed = int(hashlib.md5(prompt.encode()).hexdigest(), 16) % 10000
    return f"https://picsum.photos/seed/{seed}/512/512"