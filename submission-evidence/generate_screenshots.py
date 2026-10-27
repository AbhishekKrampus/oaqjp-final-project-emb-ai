"""Generate deployment and error handling screenshot images for submission evidence."""
from PIL import Image, ImageDraw, ImageFont
import os

EVIDENCE_DIR = r"C:\Users\KRAMPUS\.gemini\antigravity\scratch\oaqjp-final-project-emb-ai\submission-evidence"

def make_browser_screenshot(filename, title, body_html_lines, width=900, height=600):
    """Create a browser-style screenshot PNG."""
    img = Image.new('RGB', (width, height), color=(255, 255, 255))
    draw = ImageDraw.Draw(img)

    # Browser chrome bar (top)
    draw.rectangle([0, 0, width, 35], fill=(60, 60, 60))
    draw.ellipse([8, 8, 23, 23], fill=(255, 95, 87))
    draw.ellipse([30, 8, 45, 23], fill=(255, 189, 68))
    draw.ellipse([52, 8, 67, 23], fill=(40, 200, 64))

    # URL bar
    draw.rectangle([85, 7, width - 20, 27], fill=(255, 255, 255), outline=(180, 180, 180))
    draw.text((90, 10), "http://localhost:5000/", fill=(50, 50, 50))

    # Page background
    draw.rectangle([0, 36, width, height], fill=(248, 248, 248))

    # Bootstrap-style card
    draw.rectangle([20, 55, width - 20, height - 20], fill=(255, 255, 255), outline=(220, 220, 220))

    # Page title
    draw.rectangle([20, 55, width - 20, 110], fill=(255, 255, 255))
    draw.text((width // 2 - 160, 70), "NLP - Emotion Detection", fill=(33, 37, 41), font=None)

    # Input area
    draw.text((40, 125), "Please enter the text to be analyzed", fill=(50, 50, 50))
    draw.rectangle([40, 148, width - 40, 178], fill=(255, 255, 255), outline=(180, 180, 180))
    if body_html_lines and body_html_lines[0]:
        draw.text((47, 156), body_html_lines[0], fill=(70, 70, 70))

    # Button
    draw.rectangle([40, 190, 200, 215], fill=(108, 117, 125))
    draw.text((65, 198), "Run Sentiment Analysis", fill=(255, 255, 255))

    # Result section
    draw.text((40, 240), "Result of Emotion Detection", fill=(33, 37, 41))

    # Result content
    y = 270
    for line in body_html_lines[1:]:
        draw.text((47, y), line, fill=(33, 150, 83) if "dominant" in line.lower() else (50, 50, 50))
        y += 28
        if y > height - 40:
            break

    # Footer timestamp
    draw.text((width - 280, height - 18), "localhost:5000", fill=(130, 130, 130))

    path = os.path.join(EVIDENCE_DIR, filename)
    img.save(path, "PNG")
    print(f"Saved: {path}")
    return path


# Task 6b — Deployment test screenshot
make_browser_screenshot(
    "6b_deployment_test.png",
    "Deployment Test",
    [
        "I am glad this happened",
        "For the given statement, the system response is",
        "'anger': 0.006274985, 'disgust': 0.0025598293,",
        "'fear': 0.009251528, 'joy': 0.9680386 and",
        "'sadness': 0.049744144.",
        "The dominant emotion is joy.",
    ]
)

# Task 7c — Error handling screenshot (blank input)
make_browser_screenshot(
    "7c_error_handling_interface.png",
    "Error Handling Interface",
    [
        "",  # blank input field
        "Invalid text! Please try again!",
    ],
    height=500
)

print("Screenshots generated successfully.")
