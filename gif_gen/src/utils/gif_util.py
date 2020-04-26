def build_gif_name(video_name):
    name_parts = video_name.split('.')
    gif_name = ''
    for i in range(len(name_parts) - 1):
        name_part = name_parts[i] + '.'
        gif_name += name_part
    gif_name += "gif"
    return gif_name