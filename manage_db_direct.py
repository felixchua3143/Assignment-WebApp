import shelve
import json
import codecs

def export_shelve_to_json(shelve_filename, json_filename):
    try:
        with shelve.open(shelve_filename) as db:
            data = dict(db)
            with codecs.open(json_filename, 'w', 'utf-8') as json_file:
                json.dump(data, json_file, indent=4, ensure_ascii=False)
            print(f"Data successfully exported to {json_filename}")
    except Exception as e:
        print(f"An error occurred: {e}")

def read_json(json_filename):
    try:
        with open(json_filename, 'r', encoding='utf-8') as json_file:
            data = json.load(json_file)
            print(json.dumps(data, indent=4, ensure_ascii=False))
    except FileNotFoundError:
        print("The JSON file does not exist.")
    except json.JSONDecodeError:
        print("Error decoding JSON file.")
    except Exception as e:
        print(f"An error occurred: {e}")

def import_json_to_shelve(json_filename, shelve_filename):
    try:
        with open(json_filename, 'r', encoding='utf-8') as json_file:
            data = json.load(json_file)
    except FileNotFoundError:
        data = {}
    except json.JSONDecodeError:
        data = {}
    except Exception as e:
        print(f"An error occurred while reading JSON: {e}")
        data = {}

    try:
        with shelve.open(shelve_filename, writeback=True) as db:
            db.update(data)
            db.sync()
        print(f"Data successfully imported from {json_filename} to {shelve_filename}")
    except Exception as e:
        print(f"An error occurred while writing to Shelve: {e}")

if __name__ == "__main__":
    action = "export"  # Change this to "export", "read", or "import"
    shelve_filename = 'products_shelve.db'
    json_filename = 'products.json'

    if action == 'export':
        export_shelve_to_json(shelve_filename, json_filename)
    elif action == 'read':
        read_json(json_filename)
    elif action == 'import':
        import_json_to_shelve(json_filename, shelve_filename)
