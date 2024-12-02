from app import create_app, socketio

app = create_app()

if __name__ == "__main__":
    # app.run(debug=True)
    
    # Run the app using SocketIO
    socketio.run(app, debug=True)

