# esp32c6_wifi_sucks
A test of the board wifi antenna vs external antenna. esp32c3 results also compared.

The Seeed Xiao esp32c6 ships only with a board antenna. Xiao esp32c3 ships only with an external antenna. As you might suspect, the external antenna is much, much better than the board antenna. Also, esp32c3's wifi is much better than the esp32c6 (using the same external antenna). This is surprising as esp32c6 is advertised with wifi 6 (I am relying on the Micropython implementation to enable this). My wifi router is wifi 6 compliant. Additionally, I was hoping that the low-power core on esp32c6 would be avaialable from Micropython (it is not). If you are looking for a low-cost single core MCU with good wifi, my pick is esp32c3. 

Here are some numbers from the included micropython script. I ran 3 times and took the run with the highest SSID: 1 strength.

esp32c6 with external antenna:

SSID: 1  , strength: -51
SSID: 2  , strength: -68
SSID: 4  , strength: -85
SSID: 8  , strength: -87
SSID: 9  , strength: -87
SSID: 11 , strength: -89
SSID: 12 , strength: -89
SSID: 13 , strength: -90
SSID: 14 , strength: -91
SSID: 15 , strength: -91
SSID: 17 , strength: -92
SSID: 18 , strength: -92
SSID: 19 , strength: -93

esp32c6 with board antenna:

SSID: 1  , strength: -66
SSID: 2  , strength: -85
SSID: 3  , strength: -95
SSID: 4  , strength: -95

esp32c3 with external antenna

SSID: 1  , strength: -37
SSID: 2  , strength: -57
SSID: 3  , strength: -70
SSID: 4  , strength: -73
SSID: 8  , strength: -76
SSID: 9  , strength: -77
SSID: 10 , strength: -77
SSID: 11 , strength: -78
SSID: 12 , strength: -78
SSID: 14 , strength: -81
SSID: 15 , strength: -83
SSID: 16 , strength: -84
SSID: 17 , strength: -85
SSID: 20 , strength: -86
SSID: 25 , strength: -88
SSID: 27 , strength: -88
SSID: 28 , strength: -89
SSID: 30 , strength: -89
SSID: 33 , strength: -90
SSID: 34 , strength: -90
SSID: 35 , strength: -90
SSID: 36 , strength: -91

esp32s3 with external antenna

SSID: 1  , strength: -37
SSID: 6  , strength: -76
SSID: 7  , strength: -77
SSID: 8  , strength: -78
SSID: 9  , strength: -78
SSID: 10 , strength: -78
SSID: 11 , strength: -82
SSID: 13 , strength: -84
SSID: 14 , strength: -86
SSID: 15 , strength: -86
SSID: 16 , strength: -88
SSID: 20 , strength: -92
SSID: 21 , strength: -93
SSID: 22 , strength: -94
