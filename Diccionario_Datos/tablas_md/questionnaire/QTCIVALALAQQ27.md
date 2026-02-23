# questionnaire.QTCIVALALAQQ27

> Arterial Line Assessment : Drainage assessment

**Schema:** questionnaire
**Columnas:** 5
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare.

*Descripción original:* Arterial Line Assessment : Drainage assessment

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| QUESParRefDR | bigint | PK | FK | NO | Parent Reference |
| ID | varchar |  |  | NO | - |
| Q27Q1 | varchar |  |  | SI | Drainage present |
| Q27Q2 | varchar |  |  | SI | Drainage description |
| childsub | bigint |  |  | NO | - |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*