from faster_whisper import WhisperModel

model = WhisperModel('medium', device='cpu', compute_type='int8')

segments, info = model.transcribe(
    r'C:\Users\zeljk\13 10 2026 - 2. dio, 12. sjednica Hrvatskoga sabora, 11. saziv 2026-10-13 18_46 [N1BhDnXILqY].mp3',
    language='hr'
)

with open(r'C:\Users\zeljk\transkript_sabora.txt', 'w', encoding='utf-8') as f:
    for seg in segments:
        f.write(seg.text + '\n')

print("Gotovo! Transkript je spremljen u C:\\Users\\zeljk\\transkript_sabora.txt")