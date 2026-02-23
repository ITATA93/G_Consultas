# questionnaire.QTCWOUNDMGTQQ73

> Wound Assessment and Care : Wound Edge and Periwound

**Schema:** questionnaire
**Columnas:** 11
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare.

*Descripción original:* Wound Assessment and Care : Wound Edge and Periwound

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| QUESParRefDR | bigint | PK | FK | NO | Parent Reference |
| ID | varchar |  |  | NO | - |
| Q73Q1 | date |  |  | SI | Date |
| Q73Q2 | varchar |  |  | SI | Wound edge / margin |
| Q73Q3 | varchar |  |  | SI | Wound edge comments |
| Q73Q4 | varchar |  |  | SI | Periwound |
| Q73Q5 | varchar |  |  | SI | Periwound comments |
| Q73Q6 | varchar |  |  | SI | Entered by |
| Q73Q7 | varchar |  |  | SI | Wound edge / margin |
| Q73Q8 | varchar |  |  | SI | Periwound |
| childsub | bigint |  |  | NO | - |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*