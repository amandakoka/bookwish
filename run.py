import os
from bookwish import app

# Check if the script is being run directly
if __name__ == "__main__":
    # Run the Flask application
    app.run(
        # Get the IP address from the environment variables
        host=os.environ.get("IP"),
        # Get the port number from the environment variables and convert it to an integer
        port=int(os.environ.get("PORT")),
        # Get the debug mode status from the environment variables and convert it to a boolean
        debug=os.environ.get("DEBUG")
    ) 
