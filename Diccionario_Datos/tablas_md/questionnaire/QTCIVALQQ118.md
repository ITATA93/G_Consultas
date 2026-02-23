# questionnaire.QTCIVALQQ118

> "Intravascular Access Lines : Catheter position corrected / withdrawn	"

**Schema:** questionnaire
**Columnas:** 7
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare.

*Descripción original:* "Intravascular Access Lines : Catheter position corrected / withdrawn	"

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| QUESParRefDR | bigint | PK | FK | NO | Parent Reference |
| ID | varchar |  |  | NO | - |
| Q118Q1 | numeric |  |  | SI | Central IV CVP Catheter Withdrawn (cm)	 |
| Q118Q2 | numeric |  |  | SI | Central IV External Catheter Length (cm)	 |
| Q118Q3 | numeric |  |  | SI | Central Internal Catheter Length (cm)	 |
| Q118Q4 | numeric |  |  | SI | Central IV Mid Arm Circumference (cm)	 |
| childsub | bigint |  |  | NO | - |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*