# questionnaire.QTCIVALQQ68

> "Intravascular Access Lines : Arterial Line Status	"

**Schema:** questionnaire
**Columnas:** 9
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare.

*Descripción original:* "Intravascular Access Lines : Arterial Line Status	"

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| QUESParRefDR | bigint | PK | FK | NO | Parent Reference |
| ID | varchar |  |  | NO | - |
| Q68Q1 | varchar |  |  | SI | Status |
| Q68Q2 | varchar |  |  | SI | Care / Troubleshoot	 |
| Q68Q3 | varchar |  |  | SI | Site Care	 |
| Q68Q4 | varchar |  |  | SI | Site Condition	 |
| Q68Q5 | varchar |  |  | SI | Dressing Condition	 |
| Q68Q6 | varchar |  |  | SI | Dressing |
| childsub | bigint |  |  | NO | - |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*