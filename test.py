import speedtest


def perform_speed_test():
    """
  This function performs an internet speed test and returns download and upload speeds in Mbps.
  """
    # Create a Speedtest object
    st = speedtest.Speedtest()

    # Find the best server for the test
    server = st.get_best_server()
    print(f"Connecting to server: {server['host']} ({server['name']})")

    # Perform download speed test
    download_speed = st.download() / 1048576  # Convert bytes to Mbps

    # Perform upload speed test
    upload_speed = st.upload() / 1048576  # Convert bytes to Mbps

    # Return download and upload speeds
    return download_speed, upload_speed


if __name__ == "__main__":
    # Run the test and print results
    download_speed, upload_speed = perform_speed_test()
    print(f"Download Speed: {download_speed:.2f} Mbps")
    print(f"Upload Speed: {upload_speed:.2f} Mbps")
