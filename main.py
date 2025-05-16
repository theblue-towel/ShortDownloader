from threader import Threader

# ─── CONFIG ────────────────────────────────────────────────────────────────
CHANNEL_HANDLES = [
    # Hyper-Optimized Algorithmic Shorts
    "channel/UCvEfbBrcYjO6QZRZcP5iJSw",  # LankyBox
    "@VladandNikiShorts",                # Vlad & Niki
    "channel/UC7Pq3Ko42YpkCB_Q4E981jw",  # Ryan's World
    "channel/UCdIj7Lzw0LbZ9-9x-d_GVhQ",  # Talking Tom
    "@Pencilmation",                     # Pencilmation

    # Satisfying Loops/ASMR
    "channel/UC7MlI9Qp0L7iY1RxtW5x9ZQ",  # Squishy Shorts
    "@MagicFingersVideos",               # Magic Fingers
    
    # AI-Generated/Slime Cat-like
    "@SlimeCatOfficial",                 # Slime Cat
    "channel/UCYjG8j8EFexBwt-x_5BEQ5A",  # Morphle
    
    # Brain Candy (No Plot)
    "@MoonbugShorts",                    # Moonbug
    "channel/UC6QWhGzHq7kzsy2J_Qk3PJg",  # Super JoJo
    
    # Backup Channels
    "@CocomelonShorts",                  # Cocomelon
    "@BlippiShorts",                     # Blippi
    "channel/UCGF2rFEnQkI1P6lD8oQzX6Q",  # Kids Diana Show
    "@LikeNastyaShorts",                 # Like Nastya
]    

t = Threader()

t.loop(CHANNEL_HANDLES=CHANNEL_HANDLES)
