# questionnaire.QTCETIAQQ27

> Endotracheal Intubation Assessment : Ventilator associated pneumonia  bundle

**Schema:** questionnaire
**Columnas:** 13
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare.

*Descripción original:* Endotracheal Intubation Assessment : Ventilator associated pneumonia  bundle

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| QUESParRefDR | bigint | PK | FK | NO | Parent Reference |
| ID | varchar |  |  | NO | - |
| Q27Q1 | varchar |  |  | SI | Head Of Bed (HOB) elevated  |
| Q27Q10 | time |  |  | SI | Time |
| Q27Q2 | varchar |  |  | SI | Daily sedative interruption |
| Q27Q3 | varchar |  |  | SI | Daily assessment of readiness to extubate |
| Q27Q4 | varchar |  |  | SI | Peptic Ulcer Disease (PUD) prophylaxis |
| Q27Q5 | varchar |  |  | SI | Deep Venous Thrombosis (DVT) prophylaxis |
| Q27Q6 | varchar |  |  | SI | Oral care performed |
| Q27Q7 | varchar |  |  | SI | Secretion management performed |
| Q27Q8 | varchar |  |  | SI | Assessment performed by |
| Q27Q9 | date |  |  | SI | Assessment date and time |
| childsub | bigint |  |  | NO | - |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*