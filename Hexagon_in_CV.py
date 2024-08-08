import cv2
import numpy as np

def draw_hexagon(image, center_x, center_y, radius, color=(255, 0, 0), thickness=3):
    """Draws a hexagon on a NumPy array image using OpenCV.

    Args:
        image: The NumPy array image to draw on.
        center_x: The x-coordinate of the hexagon's center.
        center_y: The y-coordinate of the hexagon's center.
        radius: The radius of the hexagon's circumcircle.
        color: The color of the hexagon in BGR format (default: blue).
        thickness: The thickness of the hexagon's lines (default: 3).

    Returns:
        The image with the hexagon drawn on it.
    """

    # Calculate hexagon vertices based on center and radius
    vertices = [
        (int(center_x + radius * np.cos(2 * np.pi * i / 6)),
         int(center_y + radius * np.sin(2 * np.pi * i / 6)))
        for i in range(6)
    ]

    # Ensure vertices are integers for cv2 compatibility
    vertices = np.array(vertices, np.int32)

    # Draw the hexagon
    cv2.polylines(image, [vertices], True, color, thickness)

    return image

# Example usage:

# Create a black image
image = np.zeros((400, 400, 3), np.uint8)

# Draw a hexagon in the center with a radius of 100 pixels
image = draw_hexagon(image, 200, 200, 100)

# Display the image
cv2.imshow("Hexagon", image)
cv2.waitKey(0)
cv2.destroyAllWindows()
