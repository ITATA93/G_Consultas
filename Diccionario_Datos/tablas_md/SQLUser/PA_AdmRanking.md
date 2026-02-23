# SQLUser.PA_AdmRanking

**Schema:** SQLUser
**Columnas:** 9
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Admisión de Pacientes**. Registra episodios de atención hospitalaria.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| RANKRowID | bigint | PK |  | NO | - |
| Q78Q1 | - |  |  | SI | Escort name |
| Q78Q2 | - |  |  | SI | Escort contact number |
| QUESParRefDR | - |  |  | SI | Parent Reference |
| RANKAdmDR | bigint |  | FK | NO | Des Ref PAAdm |
| RANKLocDR | bigint |  | FK | NO | Des Ref Location |
| RANKPriority | integer |  |  | NO | Ranking Priority |
| RANKTreatmentStreamDR | bigint |  | FK | NO | Des Ref PAC_TreatmentStream |
| RANKTriageCatDR | bigint |  | FK | NO | Des Ref Priority |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*