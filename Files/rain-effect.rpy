

init python:
    renpy.music.register_channel("ambient","sfx",True,tight=True) 

define audio.rain = "<loop 0.0>/sfx/rain.ogg"
define audio.rainindoors = "<loop 0.0>/sfx/rain2.ogg"

label rain:
    play ambient rain fadein 5.0
    show rain zorder 5 with Dissolve(5.0)
    return

label instant_rain:
    play ambient rain
    show rain zorder 5
    return

label rain_stop:
    stop ambient fadeout 5.0
    hide rain with Dissolve(5.0)
    return

label instant_rain_stop:
    stop ambient
    hide rain
    return





define rain_alpha = .7
define rain_speed = .05
image rain:
    truecenter
    "/images/weather_system/rain/rain1.png"
    alpha rain_alpha
    rain_speed
    "/images/weather_system/rain/rain2.png"
    alpha rain_alpha
    rain_speed
    "/images/weather_system/rain/rain3.png"
    alpha rain_alpha
    rain_speed
    "/images/weather_system/rain/rain4.png"
    alpha rain_alpha
    rain_speed
    "/images/weather_system/rain/rain5.png"
    alpha rain_alpha
    rain_speed
    "/images/weather_system/rain/rain6.png"
    alpha rain_alpha
    rain_speed
    "/images/weather_system/rain/rain7.png"
    alpha rain_alpha
    rain_speed
    "/images/weather_system/rain/rain8.png"
    alpha rain_alpha
    rain_speed
    repeat
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
