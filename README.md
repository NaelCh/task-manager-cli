# 📝 Task Manager CLI

Ένα απλό **Command Line Interface (CLI)** εργαλείο για διαχείριση εργασιών, γραμμένο σε Python.  
Αποθηκεύει τις εργασίες σε **JSON αρχείο**, ώστε να είναι διαθέσιμες ακόμα και μετά το κλείσιμο του προγράμματος.

---

## 🚀 Χαρακτηριστικά

- Δημιουργία νέων tasks με τίτλο & περιγραφή
- Προβολή όλων των tasks
- Σημείωση task ως ολοκληρωμένο
- Διαγραφή task
- Αυτόματη αποθήκευση σε `tasks.json`
- Καθαρή αρχιτεκτονική με OOP (`Task`, `TaskManager`)

---

## ⚙️ Εγκατάσταση

1. Βεβαιώσου ότι έχεις Python 3 εγκατεστημένο:
   python --version

2. Κάνε clone το repository:
   ```bash
   git clone https://github.com/NaelCh/task-manager-cli.git
   cd task-manager-cli

## 💻 Οδηγίες Χρήσης

Το πρόγραμμα τρέχει από το τερματικό με την εντολή:

```bash
python main.py <command> [options]

Για να δείς τις διαθέσημες λειτουργίες τρέξε την εντολή:

python main.py --help

Παράδειγμα χρήσης:

1. Προσθήκη δύο νέων εργασιών:
python main.py add "Διάβασμα" "Κεφάλαιο 1"
python main.py add "Ψώνια" "Να αγοράσω γάλα"

2. Εμφάνιση όλων των εργασιών:
python main.py list

3. Ολοκλήρωση μιας εργασίας:
python main.py done 123e4567-e89b-12d3-a456-426614174000

4. Διαγραφή μιας εργασίας:
python main.py remove 987e6543-e21b-12d3-a456-426614174111
