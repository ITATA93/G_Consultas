# questionnaire.QTCEVDCQQ09

> Extraventricular Drain (EVD) Insertion and Care : Extra ventricular drain assessment

**Schema:** questionnaire
**Columnas:** 10
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare.

*Descripción original:* Extraventricular Drain (EVD) Insertion and Care : Extra ventricular drain assessment

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| QUESParRefDR | bigint | PK | FK | NO | Parent Reference |
| ID | varchar |  |  | NO | - |
| Q09Q1 | date |  |  | SI | Date |
| Q09Q2 | time |  |  | SI | Time |
| Q09Q3 | varchar |  |  | SI | Dressing status |
| Q09Q4 | varchar |  |  | SI | Insertion site check |
| Q09Q5 | varchar |  |  | SI | Actions performed |
| Q09Q6 | varchar |  |  | SI | Assessment notes |
| Q09Q7 | varchar |  |  | SI | Assessment performed by |
| childsub | bigint |  |  | NO | - |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*