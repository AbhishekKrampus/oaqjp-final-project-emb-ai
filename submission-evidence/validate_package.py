"""Validate the EmotionDetection package is importable."""
import sys
import os
# Ensure the project root is in path
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import EmotionDetection
from EmotionDetection import emotion_detector

print("=== Task 4: Package Validation ===")
print()
print("import EmotionDetection  --> OK")
print("from EmotionDetection import emotion_detector  --> OK")
print()
print("Package __file__:", EmotionDetection.__file__)
print("Function:", emotion_detector)
print("Available public names:", [n for n in dir(EmotionDetection) if not n.startswith("_")])
print()
print("Result: EmotionDetection is a valid Python package.")
print("        emotion_detector is importable from the package.")
