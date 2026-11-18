        writer.close()


# DISPLAY GENERATED FILES

@app.route("/generated/<path:filename>")
def generated(filename):
    return send_from_directory(OUTPUT, filename)


# START WEBSITE

initialize_database()

if __name__ == "__main__":
    app.run(
        host="127.0.0.1",
        port=5000,
        debug=True
    )
