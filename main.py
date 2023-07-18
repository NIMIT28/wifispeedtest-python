import speedtest

st= speedtest.Speedtest()

d_speed = st.download() / 1000000
u_speed = st.upload() / 1000000

print("NET SPEED :")
print(f'Download speed: {d_speed:.2f} Mbps || Upload speed: {u_speed:.2f} Mbps\n')