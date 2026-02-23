# questionnaire.QTCICDFUQQ13

> "Implantable Cardioverter Defibrillators (ICD) Follow up : Threshold test details	"

**Schema:** questionnaire
**Columnas:** 11
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare.

*Descripción original:* "Implantable Cardioverter Defibrillators (ICD) Follow up : Threshold test details	"

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| QUESParRefDR | bigint | PK | FK | NO | Parent Reference |
| ID | varchar |  |  | NO | - |
| Q13Q1 | varchar |  |  | SI | Lead used |
| Q13Q2 | numeric |  |  | SI | Pacing threshold (mv)	 |
| Q13Q3 | numeric |  |  | SI | Sensing threshold (mv)	 |
| Q13Q4 | numeric |  |  | SI | Lead impedance (ohm)	 |
| Q13Q5 | numeric |  |  | SI | Shock impedance used (ohm)	 |
| Q13Q6 | numeric |  |  | SI | At last shock (mv)	 |
| Q13Q7 | numeric |  |  | SI | Low energy (mv)	 |
| Q13Q8 | varchar |  |  | SI | Sense / pace issues	 |
| childsub | bigint |  |  | NO | - |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*