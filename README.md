# Seeed Xiao esp32c6 wifi sucks

A test of the board wifi antenna vs external antenna. Xiao esp32c3 and Xiao esp32s3 results also compared.

The Seeed Xiao esp32c6 ships only with a board antenna. Xiao esp32c3 and esp32s3 ships only with an external antenna. As you might suspect, the external antenna is much, much better than the board antenna. Also, esp32c3/esp32s3 wifi is much better than the esp32c6 (using the same external antenna). 

This is surprising as esp32c6 is advertised with wifi 6 (I am relying on the Micropython implementation to enable this). My wifi router is wifi 6 compliant. Additionally, I was hoping that the low-power core on esp32c6 would be avaialable in Micropython (it is not, can only see the high-power core).

If you are looking for a low-cost single core MCU with good wifi, my pick is esp32c3. If you need a full dual-core MCU with good wifi, esp32s3.

Here are some numbers from the included micropython script. I ran 3 times and took the run with the highest first SSID strength.

External Antenna results:

| Xiao esp32c6 | Xiao esp32c3 | Xiao esp32s3 |
| :----------: | :----------: | :----------: |
| -51 | -37 | -37 |
| -68 | -57 | -76 |
| -85 | -70 | -77 |
| -87 | -73 | -78 |
| -87 | -76 | -78 |
| -89 | -77 | -78 |
| -89 | -77 | -82 |
| -90 | -78 | -84 |
| -91 | -78 | -86 |
| -91 | -81 | -86 |
| -92 | -83 | -88 |
| -92 | -84 | -92 |
| -93 | -85 | -93 |
|     | -86 | -94 |
|     | -88 |     |
|     | -88 |     |
|     | -89 |     |
|     | -89 |     |
|     | -90 |     |
|     | -90 |     |
|     | -90 |     |
|     | -91 |     |

Board Antenna results:

| Xiao esp32c6 |   Pico W   | Raspberry Pi 2W |
| :----------: | :--------: | :-------------: |
| -66 | -37 | -34 |
| -85 | -56 | -55 |
| -95 | -75 | -75 |
| -95 | -76 | -77 |
|     | -79 | -78 |
|     | -90 | -82 |
|     | -91 | -84 |
|     | -95 | -91 |
