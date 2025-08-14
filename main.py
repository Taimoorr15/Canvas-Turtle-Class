from turtlee import Turtle

if __name__ == "__main__":
    t = Turtle()

    print("\n--- Test Case 1: Move Forward ---")
    t.forward(100)

    print("\n--- Test Case 2: Turn Left & Move ---")
    t.left(90)
    t.forward(50)

    print("\n--- Test Case 3: Turn Right & Move Backward ---")
    t.right(45)
    t.backward(70)

    print("\n--- Final Position & Angle ---")
    print(f"Position: {t.position()}")
    print(f"Heading: {t.heading()}°")

    t.wait()  # Keep the window open

