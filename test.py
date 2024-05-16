import speedtest

def perform_speed_test():
    """
    Perform an internet speed test using the best server and return download and upload speeds in Mbps.
    """
    try:
        st = speedtest.Speedtest()
        st.get_best_server()

        best_server = st.get_best_server()
        print(f"Connecting to server: {best_server['host']} ({best_server['name']})")

        download_speed = st.download() / 1048576  # Convert bytes to Mbps
        upload_speed = st.upload() / 1048576  # Convert bytes to Mbps

        return download_speed, upload_speed
    except speedtest.SpeedtestException as e:
        print(f"An error occurred: {e}")
        return None, None

def main():
    download_speed, upload_speed = perform_speed_test()
    if download_speed is not None and upload_speed is not None:
        print(f"Download Speed: {download_speed:.2f} Mbps")
        print(f"Upload Speed: {upload_speed:.2f} Mbps")

if __name__ == "__main__":
    main()
