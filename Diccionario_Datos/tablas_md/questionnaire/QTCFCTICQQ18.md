# questionnaire.QTCFCTICQQ18

> Faecal Containment Tube Insertion and Care : Faecal containment device assessment

**Schema:** questionnaire
**Columnas:** 10
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare.

*Descripción original:* Faecal Containment Tube Insertion and Care : Faecal containment device assessment

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| QUESParRefDR | bigint | PK | FK | NO | Parent Reference |
| ID | varchar |  |  | NO | - |
| Q18Q1 | date |  |  | SI | Assessment date |
| Q18Q2 | time |  |  | SI | Assessment time |
| Q18Q3 | varchar |  |  | SI | Insertion site check |
| Q18Q4 | varchar |  |  | SI | Tube checks |
| Q18Q5 | varchar |  |  | SI | Actions performed |
| Q18Q6 | varchar |  |  | SI | Assessment notes |
| Q18Q7 | varchar |  |  | SI | Assessed by |
| childsub | bigint |  |  | NO | - |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*