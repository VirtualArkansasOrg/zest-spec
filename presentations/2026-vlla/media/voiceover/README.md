# Build recording voice-over

- `lines.json`: each narration line with the window (seconds) of the scene it belongs to in `zest-build-recording.mp4` (1:41.5).
- Voice: ElevenLabs v3 through WaveSpeed (`elevenlabs/eleven-v3/timing`, voice "Brian", stability 0.5), generated in one pass with `[pause]` between lines so the voice stays consistent.
- The character timestamps the model returned were used to cut each line out and place it at the start of its window (or 0.2 s after the previous line if that ran long). Nothing was sped up. The mix is loudness-normalized to -16 LUFS.
- The narrated video (`zest-build-recording-narrated.mp4`, 5.7 MB) is in Kyle's Drive and the kyle-presentations backup.
- The voice is synthetic; it is not Kyle's voice.
