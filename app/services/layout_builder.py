def build_comic_layout(panels, images):
    for i, p in enumerate(panels):
        p['image_url'] = images[i] if i < len(images) else ""
    return panels