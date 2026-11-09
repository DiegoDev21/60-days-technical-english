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
    print(f"📝 Reto: {lesson['prompt']}\n")
    
    # Capturar respuesta del usuario en la terminal
    user_answer = input("Tu respuesta > ").strip().lower()
    
    # Validar respuesta contra las opciones esperadas
    valid_answers = [ans.lower() for ans in lesson["expected_answers"]]
    
    if user_answer in valid_answers:
        print("\n✅ ¡Correcto! Buen trabajo.")
    else:
        print("\n❌ Incorrecto.")
        print(f"💡 Explicación: {lesson['explanation']}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="CLI interactiva para el curso de Inglés Técnico")
    parser.add_argument("--day", type=int, required=True, help="Número de día que deseas practicar (ej. --day 1)")
    args = parser.parse_args()
    
    run_lesson(args.day)