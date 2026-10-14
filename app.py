import streamlit as st
import math

# ---------------- PAGE SETTINGS ----------------

st.set_page_config(
    page_title="Smart Disaster Rescue City",
    page_icon="🚒",
    layout="centered"
)
# st.image("logo.png", width=250)
st.title("🚒 Smart Disaster Rescue City")
st.subheader("Emergency Distance and Nearest Location Calculator")

st.write("""
This application calculates the straight-line distance between locations
using the Coordinate Geometry Distance Formula.
""")


# ---------------- SCALE ----------------

SCALE_METERS = 10


# ---------------- CITY LOCATIONS ----------------

locations = {
    "Rescue Station": (9, 1),
    "Hospital": (7, 8),
    "Fire Station": (9, 6),
    "School": (1, 8),
    "Community Centre": (6, 2),
    "Park": (1, 1),
    "Water Tank": (6, 4),
    "Fire": (3, 6)
}


# ---------------- DISTANCE FUNCTION ----------------

def calculate_distance(x1, y1, x2, y2):
    return math.sqrt(
        (x2 - x1) ** 2 +
        (y2 - y1) ** 2
    )


# ---------------- SIDEBAR MENU ----------------

st.sidebar.header("📍 Select Operation")

option = st.sidebar.selectbox(
    "Choose what you want to calculate:",
    [
        "Distance Between Locations",
        "Distance Between Any Two Coordinates",
        "Find Nearest Location"
    ]
)


# ==================================================
# OPTION 1: DISTANCE BETWEEN TWO LOCATIONS
# ==================================================

if option == "Distance Between Locations":

    st.header("📏 Distance Between Two Locations")

    location1 = st.selectbox(
        "Select First Location:",
        list(locations.keys())
    )

    location2 = st.selectbox(
        "Select Second Location:",
        list(locations.keys()),
        index=1
    )

    x1, y1 = locations[location1]
    x2, y2 = locations[location2]

    distance = calculate_distance(x1, y1, x2, y2)

    real_distance = distance * SCALE_METERS

    st.write(f"📍 **{location1}:** ({x1}, {y1})")
    st.write(f"📍 **{location2}:** ({x2}, {y2})")

    st.subheader("🧮 Step-by-Step Calculation")

    st.latex(
        r"d = \sqrt{(x_2-x_1)^2+(y_2-y_1)^2}"
    )

    st.latex(
        f"d = \\sqrt{{({x2}-{x1})^2 + ({y2}-{y1})^2}}"
    )

    dx = x2 - x1
    dy = y2 - y1

    st.latex(
        f"d = \\sqrt{{({dx})^2 + ({dy})^2}}"
    )

    st.latex(
        f"d = \\sqrt{{{dx**2} + {dy**2}}}"
    )

    st.success(
        f"📏 Distance: {distance:.2f} units"
    )

    st.info(
        f"📏 Real Distance: {real_distance:.2f} meters"
    )


# ==================================================
# OPTION 2: DISTANCE BETWEEN ANY TWO COORDINATES
# ==================================================

elif option == "Distance Between Any Two Coordinates":

    st.header("📐 Distance Between Any Two Coordinates")

    st.subheader("First Coordinate")

    col1, col2 = st.columns(2)

    with col1:
        x1 = st.number_input(
            "Enter X1:",
            value=0.0,
            step=1.0
        )

    with col2:
        y1 = st.number_input(
            "Enter Y1:",
            value=0.0,
            step=1.0
        )

    st.subheader("Second Coordinate")

    col1, col2 = st.columns(2)

    with col1:
        x2 = st.number_input(
            "Enter X2:",
            value=0.0,
            step=1.0
        )

    with col2:
        y2 = st.number_input(
            "Enter Y2:",
            value=0.0,
            step=1.0
        )

    distance = calculate_distance(x1, y1, x2, y2)
    real_distance = distance * SCALE_METERS

    st.subheader("🧮 Calculation")

    st.latex(
        f"d = \\sqrt{{({x2}-{x1})^2 + ({y2}-{y1})^2}}"
    )

    dx = x2 - x1
    dy = y2 - y1

    st.latex(
        f"d = \\sqrt{{({dx})^2 + ({dy})^2}}"
    )

    st.latex(
        f"d = \\sqrt{{{dx**2} + {dy**2}}}"
    )

    st.success(
        f"📏 Distance: {distance:.2f} units"
    )

    st.info(
        f"📏 Real Distance: {real_distance:.2f} meters"
    )


# ==================================================
# OPTION 3: FIND NEAREST LOCATION
# ==================================================

elif option == "Find Nearest Location":

    st.header("🔍 Find Nearest Location")

    st.write(
        "Enter a coordinate, and the app will find "
        "the nearest available location."
    )

    col1, col2 = st.columns(2)

    with col1:
        user_x = st.number_input(
            "Enter X coordinate:",
            value=0.0,
            step=1.0
        )

    with col2:
        user_y = st.number_input(
            "Enter Y coordinate:",
            value=0.0,
            step=1.0
        )

    nearest_location = None
    nearest_distance = float("inf")
    all_distances = {}

    # Calculate distance to every location
    for name, coordinates in locations.items():

        x, y = coordinates

        distance = calculate_distance(
            user_x,
            user_y,
            x,
            y
        )

        all_distances[name] = distance

        # Find smallest distance
        if distance < nearest_distance:
            nearest_distance = distance
            nearest_location = name

    # Display nearest result
    st.subheader("📍 Result")

    st.write(
        f"Your coordinate: **({user_x}, {user_y})**"
    )

    st.success(
        f"🚨 Nearest Location: **{nearest_location}**"
    )

    st.success(
        f"📏 Nearest Distance: "
        f"**{nearest_distance:.2f} units**"
    )

    st.info(
        f"📏 Real Distance: "
        f"**{nearest_distance * SCALE_METERS:.2f} meters**"
    )

    # Display all distances
    st.subheader("📊 Distance to All Locations")

    for name, distance in sorted(
        all_distances.items(),
        key=lambda item: item[1]
    ):
        st.write(
            f"**{name}:** {distance:.2f} units"
        )