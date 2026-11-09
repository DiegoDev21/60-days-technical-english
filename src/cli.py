import json
import argparse
import sys
import os

def load_lessons():
    """Carga el archivo centralizado de lecciones desde la carpeta data."""
    file_path = os.path.join("data", "lessons.json")
    try:
        with open(file_path, "r", encoding="utf-8") as f:
            return json.load(f)
    except FileNotFoundError:
        print("❌ Error: No se encontró el archivo data/lessons.json")
        sys.exit(1)

def run_lesson(day_number):
    lessons = load_lessons()
    day_key = f"day_{day_number:02d}"
    
    if day_key not in lessons:
        print(f"❌ La lección para el Día {day_number} aún no está disponible en el JSON.")
        return

    lesson = lessons[day_key]
    
    print(f"\n==========================================")
    print(f" 🚀 Day {day_number}: {lesson['title']}")
    print(f"==========================================")
    
    # Mostrar las 7 palabras del día
    if "daily_vocabulary" in lesson:
        print("\n📚 Vocabulario del día (7 palabras):")
        for idx, item in enumerate(lesson["daily_vocabulary"], 1):
            print(f"  {idx}. {item['word']} ({item['translation']}) ➔ Ex: \"{item['example']}\"")
            
    # Mostrar palabras de días anteriores a reciclar
    if "recycled_vocabulary" in lesson:
        print(f"\n🔄 Palabras a recordar hoy: {', '.join(lesson['recycled_vocabulary'])}")
        
    print("\n------------------------------------------")
    print(f"📝 Reto: {lesson['prompt']}\n")
    
    # Capturar respuesta completa del usuario
    user_answer = " ".join(input("Tu respuesta > ").strip().lower().split())
    
    # Validar respuesta
    valid_answers = [" ".join(ans.lower().split()) for ans in lesson["expected_answers"]]
    
    if user_answer in valid_answers:
        print("\n✅ ¡Correcto! Excelente redacción.")
    else:
        print("\n❌ Incorrecto.")
        print(f"💡 Explicación: {lesson['explanation']}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="CLI interactiva para el curso de Inglés Técnico")
    parser.add_argument("--day", type=int, required=True, help="Número de día que deseas practicar (ej. --day 1)")
    args = parser.parse_args()
    
    run_lesson(args.day)