import streamlit as st
import os

# Set the title of the application
st.title("Understanding Networking for Local Applications")

# Section 1: Overview
st.header("Networking in Local Applications and Application Servers")
st.markdown(
    """
    Networking facilitates the communication between local applications (client-side software) 
    and application servers (server-side software) over a network, enabling multi-user 
    functionality for web platforms, multiplayer games, and collaborative tools.
    """
)

# Section 2: Key Components and Protocols
st.header("Key Components and Protocols")

st.subheader("Client-Side Application")
st.markdown(
    """
    The client serves as the interface for the user, sending requests to the server, receiving 
    responses, and rendering the user interface.
    """
)

st.subheader("Application Server")
st.markdown(
    """
    The server hosts the business logic, database, and resources required for the application, 
    processing requests and managing data.
    """
)

st.subheader("Networking Protocols")
st.markdown(
    """
    Protocols used include:
    - **HTTP/HTTPS**: For web applications.
    - **WebSockets**: For real-time communication.
    - **TCP/IP**: For reliable data delivery.
    - **UDP**: For fast, less reliable communication in gaming.
    - **REST/GraphQL APIs**: For structured client-server interactions.
    """
)

# Check if the image file exists before displaying it
image_path = "/mnt/data/A_detailed_conceptual_diagram_illustrating_network.png"

if os.path.exists(image_path):
    st.image(image_path, caption="Conceptual Diagram: Networking for Local Applications")
else:
    st.error(f"Image file not found at {image_path}")

# Section 3: How Networking Enables Multi-User Functionality
st.header("How Networking Enables Multi-User Functionality")

st.subheader("User Connections")
st.markdown(
    """
    The client establishes a connection to the application server using protocols like HTTP or 
    WebSocket. The server authenticates the user.
    """
)

st.subheader("Communication and Data Synchronization")
st.markdown(
    """
    - The client sends user actions as requests to the server.
    - The server processes requests and broadcasts updates to other clients as needed.
    """
)

st.subheader("Database Access")
st.markdown(
    """
    - Servers mediate between the application and database for consistent data updates.
    - Ensures concurrency and resolves conflicts.
    """
)

st.subheader("Scalability")
st.markdown(
    """
    Servers employ load balancers, cloud hosting, and database replication to handle multiple 
    users efficiently.
    """
)

# Section 4: Real-Time vs. Batch Communication
st.header("Real-Time vs. Batch Communication")

st.subheader("Real-Time Communication")
st.markdown(
    """
    Applications like chat systems or multiplayer games use WebSocket or UDP for instantaneous 
    updates.
    """
)

st.subheader("Batch Communication")
st.markdown(
    """
    Applications like email clients or e-commerce platforms use HTTP requests to fetch or submit 
    data on demand.
    """
)

# Section 5: Security Measures
st.header("Security Measures")
st.markdown(
    """
    - **Encryption (TLS/SSL)**: Secures data exchange.
    - **Authentication**: Verifies users with tokens or passwords.
    - **Firewalls and Rate Limiting**: Protect servers from unauthorized access.
    """
)

# Section 6: Example Use Cases
st.header("Example Use Cases")

st.subheader("Web Applications")
st.markdown(
    """
    A user posts a comment; the server updates the database and notifies others via WebSocket.
    """
)

st.subheader("Multiplayer Games")
st.markdown(
    """
    A client connects to the game server using TCP or UDP; game state changes are synchronized 
    across all players.
    """
)

st.subheader("Collaborative Tools")
st.markdown(
    """
    A collaborative editing tool synchronizes changes via WebSockets, reflecting updates for 
    all connected users.
    """
)
