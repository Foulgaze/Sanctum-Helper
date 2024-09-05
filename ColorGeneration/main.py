from PIL import Image, ImageDraw
import itertools

# Define color codes
colors = {
    'R': '#F9AA8F',
    'U': '#AAE0FA',
    'W': '#FFFBD5',
    'G': '#9BD3AE',
    'B': '#000000'
}

# Customize image size here
image_size = (500, 500)

# Generate all non-empty combinations of colors
def generate_combinations(colors):
    color_names = list(colors.keys())
    combinations = []
    for r in range(1, len(color_names) + 1):
        combinations += list(itertools.combinations(color_names, r))
    return combinations

# Draw the image for a given color combination
def draw_image_for_combination(combination, colors, image_size):
    image = Image.new("RGB", image_size, "white")
    draw = ImageDraw.Draw(image)

    # Calculate the width of each section
    section_width = image_size[0] // len(combination)
    
    # Draw each section
    for i, color in enumerate(combination):
        x_start = i * section_width
        x_end = (i + 1) * section_width if i != len(combination) - 1 else image_size[0]
        draw.rectangle([x_start, 0, x_end, image_size[1]], fill=colors[color])
    
    return image

# Generate images for all combinations
def generate_images(colors, image_size):
    combinations = generate_combinations(colors)
    
    for combination in combinations:
        print(combination)
        image = draw_image_for_combination(combination, colors, image_size)
        filename = "".join(sorted(combination)) + ".png"
        image.save(f"Colors/{filename}")
        print(f"Generated image: {filename}")

# Run the script
if __name__ == "__main__":
    generate_images(colors, image_size)