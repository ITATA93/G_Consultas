# questionnaire.QTCOTTOCLQQ03

> Perioperative - Tourniquet and Clamp Details : Clamp

**Schema:** questionnaire
**Columnas:** 8
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare.

*Descripción original:* Perioperative - Tourniquet and Clamp Details : Clamp

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| QUESParRefDR | bigint | PK | FK | NO | Parent Reference |
| ID | varchar |  |  | NO | - |
| Q03Q1 | varchar |  |  | SI | Body site |
| Q03Q2 | varchar |  |  | SI | Side |
| Q03Q3 | time |  |  | SI | Time on |
| Q03Q4 | time |  |  | SI | Time off |
| Q03Q5 | varchar |  |  | SI | Comment |
| childsub | bigint |  |  | NO | - |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*