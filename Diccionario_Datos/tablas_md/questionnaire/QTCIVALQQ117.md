# questionnaire.QTCIVALQQ117

> "Intravascular Access Lines : CVC Site Assesst	"

**Schema:** questionnaire
**Columnas:** 11
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare.

*Descripción original:* "Intravascular Access Lines : CVC Site Assesst	"

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| QUESParRefDR | bigint | PK | FK | NO | Parent Reference |
| ID | varchar |  |  | NO | - |
| Q117Q1 | varchar |  |  | SI | Is CVC Required |
| Q117Q2 | varchar |  |  | SI | Line Status |
| Q117Q3 | varchar |  |  | SI | Site Condition |
| Q117Q4 | varchar |  |  | SI | Dressing	 |
| Q117Q5 | varchar |  |  | SI | Care |
| Q117Q6 | varchar |  |  | SI | Drainage Description |
| Q117Q7 | varchar |  |  | SI | Limb Temperature	 |
| Q117Q8 | varchar |  |  | SI | Pulse Distal To Insertion Site	 |
| childsub | bigint |  |  | NO | - |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*