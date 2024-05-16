import speedtest


def perform_speed_test():
    """
    Perform an internet speed test using the Speedtest library and return download and upload speeds in Mbps.
    """
    try:
        # Create a Speedtest object
        st = speedtest.Speedtest()

        # Get the best server based on latency
        st.get_best_server()

        # Retrieve details of the best server
        best_server = st.get_best_server()
        print(f"Connecting to server: {best_server['host']} ({best_server['name']})")

        # Perform download and upload speed tests
        download_speed = st.download() / 1048576  # Convert bytes to Mbps
        upload_speed = st.upload() / 1048576  # Convert bytes to Mbps

        # Return the results
        return download_speed, upload_speed
    except speedtest.SpeedtestException as e:
        # Handle exceptions if speed test fails
        print(f"An error occurred: {e}")
        return None, None


def main():
    try:
        # Perform the speed test
        download_speed, upload_speed = perform_speed_test()

        # Check if results are available
        if download_speed is not None and upload_speed is not None:
            # Print the results
            print(f"Download Speed: {download_speed:.2f} Mbps")
            print(f"Upload Speed: {upload_speed:.2f} Mbps")
        else:
            # Print a message if speed test failed
            print("Speed test failed. Please check your internet connection.")
    finally:
        pass


if __name__ == "__main__":
    main()
