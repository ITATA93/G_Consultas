# SQLUser.LB_SystemCounter

**Schema:** SQLUser
**Columnas:** 9
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Laboratorio**. Módulo de laboratorio clínico.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| LBSCNT_RowID | bigint | PK |  | NO | - |
| LBSCNT_AutoDateReset | date |  |  | SI | Auto Reset Date
will store last date counter get ... |
| LBSCNT_Configuration | bigint |  |  | SI | Configuration |
| LBSCNT_CounterNumber | integer |  |  | SI | Counter Number |
| Q08Q1 | - |  |  | SI | Factores de Riesgo |
| Q08Q2 | - |  |  | SI | Factores Protectores |
| Q08Q3 | - |  |  | SI | Fecha |
| Q08Q4 | - |  |  | SI | Profesional |
| QUESParRefDR | - |  |  | SI | Parent Reference |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*